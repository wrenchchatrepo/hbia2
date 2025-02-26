#!/bin/bash

# Vertex AI Agent Builder Setup Script
# This script sets up the complete environment for your Vertex AI agents

# Exit on error
set -e

echo "Starting Vertex AI Agent Builder Setup..."

# Source environment variables
if [ -f .env ]; then
    echo "Loading environment variables..."
    source .env
else
    echo "Error: .env file not found. Please create it first."
    exit 1
fi

# Check if required variables are set
if [ -z "$PROJECT_ID" ] || [ -z "$REGION" ]; then
    echo "Error: Required environment variables are not set."
    echo "Please ensure PROJECT_ID and REGION are defined in your .env file."
    exit 1
fi

# Ensure gcloud is configured with the correct project
echo "Configuring gcloud for project: $PROJECT_ID"
gcloud config set project $PROJECT_ID

# Enable required APIs
echo "Enabling required APIs..."
gcloud services enable aiplatform.googleapis.com \
    storage.googleapis.com \
    artifactregistry.googleapis.com \
    cloudresourcemanager.googleapis.com \
    iam.googleapis.com \
    logging.googleapis.com \
    monitoring.googleapis.com

# Create directory structure
echo "Creating directory structure..."
mkdir -p vertex-config/{config/{assistants},scripts/{setup,update},datastores/{looker,bigquery,dbt,gcp,omni,lookerstudio},tests/agent_tests}

# Create base bucket
echo "Creating base storage bucket..."
if ! gsutil ls -b "${BUCKET_BASE}" &>/dev/null; then
    gsutil mb -l ${REGION} -b on ${BUCKET_BASE}
    echo "Created bucket: ${BUCKET_BASE}"
else
    echo "Bucket ${BUCKET_BASE} already exists."
fi

# Create datastore buckets
echo "Creating datastore buckets..."
for store in looker bigquery dbt gcp omni lookerstudio; do
    bucket="${BUCKET_BASE%/}-${store}"
    if ! gsutil ls -b "${bucket}" &>/dev/null; then
        gsutil mb -l ${REGION} -b on ${bucket}
        echo "Created bucket: ${bucket}"
    else
        echo "Bucket ${bucket} already exists."
    fi
done

# Clone and prepare repositories
echo "Setting up repository data..."
if [ ! -f "flatten_repos.sh" ]; then
    echo "Creating repository flattening script..."
    cat > flatten_repos.sh << 'EOF'
#!/bin/bash

# Configuration
INPUT_MD_FILE="repos.md"
OUTPUT_DIR="flattened_repos"
TEMP_DIR="temp_repos"
LOG_FILE="flatten_repos.log"

# Files to exclude (case insensitive)
EXCLUDE_FILES=(
    "license"
    "readme.md"
    "changelog.md"
    "contributing.md"
    "authors"
    "dockerfile"
    ".gitignore"
    ".editorconfig"
    "requirements.txt"
    "setup.py"
    "setup.cfg"
    "tox.ini"
    "pytest.ini"
    ".pylintrc"
    ".pre-commit-config.yaml"
    "package.json"
    "package-lock.json"
    "yarn.lock"
    ".npmignore"
    ".travis.yml"
    "appveyor.yml"
    "manifest.json"
    ".eslintrc"
    ".prettierrc"
    "tsconfig.json"
    ".env"
    ".env.example"
    "docker-compose.yml"
    "makefile"
)

# File extensions to exclude
EXCLUDE_EXTENSIONS=(
    ".pyc"
    ".pyo"
    ".pyd"
    ".so"
    ".dll"
    ".dylib"
    ".log"
    ".cache"
    ".DS_Store"
    ".git"
    ".idea"
    ".vscode"
    ".pytest_cache"
    "__pycache__"
    ".ipynb_checkpoints"
)

# Create necessary directories
mkdir -p "${OUTPUT_DIR}"
mkdir -p "${TEMP_DIR}"

# Initialize log file
echo "Repository flattening process started at $(date)" > "${LOG_FILE}"

# Function to check if file should be excluded
should_exclude_file() {
    local filename=$(basename "$1" | tr '[:upper:]' '[:lower:]')
    local extension="${filename##*.}"
    
    # Check against excluded files
    for exclude in "${EXCLUDE_FILES[@]}"; do
        if [[ "${filename}" == "$(echo ${exclude} | tr '[:upper:]' '[:lower:]')" ]]; then
            return 0
        fi
    done
    
    # Check against excluded extensions
    for ext in "${EXCLUDE_EXTENSIONS[@]}"; do
        if [[ "${filename}" == *"${ext}" ]]; then
            return 0
        fi
    done
    
    return 1
}

# Function to extract GitHub URLs from markdown file
extract_urls() {
    grep -o 'https://github.com/[^)"]*' "$1" | sort | uniq
}

# Function to sanitize filename
sanitize_filename() {
    echo "$1" | sed 's/[^a-zA-Z0-9._-]/_/g'
}

# Function to get next available filename
get_unique_filename() {
    local base_path="$1"
    local base_name="$2"
    local extension="${base_name##*.}"
    local name="${base_name%.*}"
    local counter=1
    local new_name="${base_name}"

    while [[ -f "${base_path}/${new_name}" ]]; do
        new_name="${name}_${counter}.${extension}"
        ((counter++))
    done

    echo "${new_name}"
}

# Function to flatten a directory
flatten_directory() {
    local source_dir="$1"
    local target_dir="$2"
    local repo_name="$3"
    local file_count=0
    local excluded_count=0
    
    # Find all files (excluding .git directory and other hidden files)
    find "${source_dir}" -type f -not -path '*/\.*' | while read -r file; do
        # Check if file should be excluded
        if should_exclude_file "$file"; then
            echo "Excluded: ${file}" >> "${LOG_FILE}"
            ((excluded_count++))
            continue
        fi
        
        # Get the original filename
        filename=$(basename "$file")
        
        # Create a unique name using repository name and original filename
        rel_path=${file#$source_dir/}
        flat_name=$(echo "${repo_name}_${rel_path}" | tr '/' '_')
        flat_name=$(sanitize_filename "$flat_name")
        
        # Handle duplicates
        flat_name=$(get_unique_filename "${target_dir}" "${flat_name}")
        
        # Copy file to target directory with new name
        cp "$file" "${target_dir}/${flat_name}"
        echo "Copied: ${file} -> ${target_dir}/${flat_name}" >> "${LOG_FILE}"
        ((file_count++))
    done
    
    echo "Processed ${file_count} files from ${repo_name} (excluded ${excluded_count} files)" >> "${LOG_FILE}"
}

# Function to show progress
show_progress() {
    local repo_url="$1"
    local current="$2"
    local total="$3"
    echo "Processing ($current/$total): ${repo_url}"
}

# Main process
echo "Starting repository processing..."

# Count total repositories
total_repos=$(extract_urls "${INPUT_MD_FILE}" | wc -l)
current_repo=0

# Extract URLs and process each repository
extract_urls "${INPUT_MD_FILE}" | while read -r repo_url; do
    ((current_repo++))
    show_progress "${repo_url}" "${current_repo}" "${total_repos}"
    echo "Processing repository: ${repo_url}" >> "${LOG_FILE}"
    
    # Extract repository name from URL
    repo_name=$(echo "${repo_url}" | awk -F'/' '{print $(NF-1)"_"$NF}')
    repo_name=$(sanitize_filename "${repo_name}")
    
    # Create temporary directory for this repository
    temp_repo_dir="${TEMP_DIR}/${repo_name}"
    mkdir -p "${temp_repo_dir}"
    
    # Clone repository
    if git clone --depth 1 "${repo_url}" "${temp_repo_dir}"; then
        echo "Successfully cloned ${repo_url}" >> "${LOG_FILE}"
        
        # Flatten the repository
        flatten_directory "${temp_repo_dir}" "${OUTPUT_DIR}" "${repo_name}"
        
        # Clean up temporary repository
        rm -rf "${temp_repo_dir}"
        echo "Cleaned up temporary files for ${repo_name}" >> "${LOG_FILE}"
    else
        echo "Failed to clone ${repo_url}" >> "${LOG_FILE}"
    fi
done

# Clean up temporary directory
rm -rf "${TEMP_DIR}"

# Generate summary
echo -e "\nProcess Summary:" >> "${LOG_FILE}"
echo "Total repositories processed: ${total_repos}" >> "${LOG_FILE}"
echo "Total files in output directory: $(find "${OUTPUT_DIR}" -type f | wc -l)" >> "${LOG_FILE}"
echo "Process completed at $(date)" >> "${LOG_FILE}"

echo "Repository flattening complete. Check ${LOG_FILE} for details."
EOF
    chmod +x flatten_repos.sh
fi

if [ ! -f "repos.md" ]; then
    echo "Creating repository list..."
    cat > repos.md << 'EOF'
# Repository List

## Looker
- https://github.com/looker/looker-sdk
- https://github.com/looker/lookml-pattern-library

## DBT
- https://github.com/dbt-labs/dbt-core
- https://github.com/dbt-labs/dbt-bigquery

## BigQuery
- https://github.com/GoogleCloudPlatform/bigquery-utils
EOF
fi

# Create documentation download script
echo "Creating documentation download script..."
cat > download_docs.sh << 'EOF'
#!/bin/bash

# Source environment variables
source .env

# Function to download and process documentation
download_documentation() {
    local name=$1
    local url=$2
    local output_dir="datastores/${name}"
    
    echo "Downloading documentation from ${url} to ${output_dir}"
    
    # Create output directory if it doesn't exist
    mkdir -p "${output_dir}"
    
    # Download content using wget
    wget --recursive --no-parent --no-host-directories --cut-dirs=3 \
         --reject="index.html*" --accept-regex=".*\.(html|pdf|md|txt)$" \
         --directory-prefix="${output_dir}" "${url}"
    
    echo "Downloaded documentation to ${output_dir}"
}

# Download documentation for each datastore
# Looker
download_documentation "looker" "https://cloud.google.com/looker/docs"
download_documentation "looker" "https://developers.looker.com"

# BigQuery
download_documentation "bigquery" "https://cloud.google.com/bigquery/docs"
download_documentation "bigquery" "https://cloud.google.com/bigquery/docs/best-practices"

# DBT
download_documentation "dbt" "https://docs.getdbt.com/docs"

# GCP
download_documentation "gcp" "https://cloud.google.com/architecture"
download_documentation "gcp" "https://cloud.google.com/docs/tutorials"

# Omni
download_documentation "omni" "https://docs.omni.co/docs"

# Looker Studio
download_documentation "lookerstudio" "https://support.google.com/looker-studio"

echo "Documentation download complete"
EOF
chmod +x download_docs.sh

# Create datastore update script
echo "Creating datastore update script..."
mkdir -p scripts/update
cat > scripts/update/update_datastores.sh << 'EOF'
#!/bin/bash

# Source environment variables
source .env

# Function to update datastore
update_datastore() {
    local name=$1
    local source_path=$2
    local bucket="${BUCKET_BASE%/}-${name}"
    
    echo "Updating datastore: ${name}"
    
    # Backup existing data
    backup_dir="${BUCKET_BASE}/backup/${name}_$(date +%Y%m%d_%H%M%S)"
    gsutil -m cp -r "${bucket}/*" "${backup_dir}/" 2>/dev/null || true
    
    # Upload new data
    gsutil -m cp -r "${source_path}/*" "${bucket}/"
    
    # Update Vertex AI datastore
    gcloud ai datastores update "${name}" \
        --project="${PROJECT_ID}" \
        --region="${REGION}" \
        --source="${bucket}/"
    
    echo "Updated datastore: ${name}"
}

# Update each datastore
update_datastore "looker-store" "datastores/looker"
update_datastore "bigquery-store" "datastores/bigquery"
update_datastore "dbt-store" "datastores/dbt"
update_datastore "gcp-store" "datastores/gcp"
update_datastore "omni-store" "datastores/omni"
update_datastore "lookerstudio-store" "datastores/lookerstudio"

echo "Datastore update complete"
EOF
chmod +x scripts/update/update_datastores.sh

# Create agent setup script
echo "Creating agent setup script..."
mkdir -p scripts/setup
cat > scripts/setup/create_agents.sh << 'EOF'
#!/bin/bash

# Source environment variables
source .env

# Function to create agent
create_agent() {
    local name=$1
    local display_name=$2
    local datastore=$3
    
    echo "Creating agent: ${name}"
    
    # Create agent
    gcloud ai agents create "${name}" \
        --display-name="${display_name}" \
        --project="${PROJECT_ID}" \
        --region="${REGION}"
    
    # Configure agent with datastore if provided
    if [ ! -z "${datastore}" ]; then
        gcloud ai agents update "${name}" \
            --project="${PROJECT_ID}" \
            --region="${REGION}" \
            --datastore="projects/${PROJECT_ID}/locations/${REGION}/datastores/${datastore}"
    fi
    
    echo "Created agent: ${name}"
}

# Create agents
create_agent "looker-assistant" "Looker Assistant" "looker-store"
create_agent "bigquery-assistant" "BigQuery Assistant" "bigquery-store"
create_agent "dbt-assistant" "DBT Assistant" "dbt-store"
create_agent "gcp-assistant" "GCP Architecture Assistant" "gcp-store"
create_agent "omni-assistant" "Omni Assistant" "omni-store"
create_agent "lookerstudio-assistant" "Looker Studio Assistant" "lookerstudio-store"
create_agent "generative-assistant" "Generative AI Router" ""

echo "Agent creation complete"
EOF
chmod +x scripts/setup/create_agents.sh

# Create datastore setup script
echo "Creating datastore setup script..."
cat > scripts/setup/create_datastores.sh << 'EOF'
#!/bin/bash

# Source environment variables
source .env

# Function to create datastore
create_datastore() {
    local name=$1
    local display_name=$2
    local bucket="${BUCKET_BASE%/}-${name#*/}"
    
    echo "Creating datastore: ${name}"
    
    # Create datastore
    gcloud ai datastores create "${name}" \
        --display-name="${display_name}" \
        --project="${PROJECT_ID}" \
        --region="${REGION}" \
        --corpus-type=ENTERPRISE_CORPUS \
        --source="${bucket}/"
    
    echo "Created datastore: ${name}"
}

# Create datastores
create_datastore "looker-store" "Looker Documentation Store"
create_datastore "bigquery-store" "BigQuery Documentation Store"
create_datastore "dbt-store" "DBT Documentation Store"
create_datastore "gcp-store" "GCP Architecture Documentation Store"
create_datastore "omni-store" "Omni Documentation Store"
create_datastore "lookerstudio-store" "Looker Studio Documentation Store"

echo "Datastore creation complete"
EOF
chmod +x scripts/setup/create_datastores.sh

echo "Setup scripts created successfully."

# Ask if user wants to run the setup now
read -p "Do you want to run the setup now? (y/n): " run_setup
if [[ $run_setup == "y" || $run_setup == "Y" ]]; then
    echo "Running repository flattening script..."
    ./flatten_repos.sh
    
    echo "Running documentation download script..."
    ./download_docs.sh
    
    echo "Creating datastores..."
    ./scripts/setup/create_datastores.sh
    
    echo "Creating agents..."
    ./scripts/setup/create_agents.sh
    
    echo "Setup complete!"
else
    echo "Setup scripts are ready. Run them manually when you're ready."
    echo "1. ./flatten_repos.sh"
    echo "2. ./download_docs.sh"
    echo "3. ./scripts/setup/create_datastores.sh"
    echo "4. ./scripts/setup/create_agents.sh"
fi

echo "Vertex AI Agent Builder setup completed successfully!" 