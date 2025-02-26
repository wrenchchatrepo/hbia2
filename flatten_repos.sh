# clone and flatten repos

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