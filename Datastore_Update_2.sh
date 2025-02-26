# Implementation Script for Updating Datastores

#!/bin/bash

# Configuration
PROJECT_ID="your-project-id"
BUCKET_BASE="gs://your-bucket-base"
TEMP_DIR="/tmp/doc_processing"

# Create temporary directory
mkdir -p "${TEMP_DIR}"

# Function to download and process documentation
download_docs() {
    local name=$1
    local urls=$2
    local output_dir="${TEMP_DIR}/${name}"
    
    mkdir -p "${output_dir}"
    
    # Download content from each URL
    while IFS= read -r url; do
        # Extract domain for filename
        domain=$(echo "${url}" | awk -F[/:] '{print $4}')
        wget \
            --recursive \
            --no-clobber \
            --page-requisites \
            --html-extension \
            --convert-links \
            --restrict-file-names=windows \
            --domains "${domain}" \
            --no-parent \
            "${url}" -P "${output_dir}"
    done <<< "${urls}"
    
    # Process and clean up the downloaded content
    find "${output_dir}" -type f -name "*.html" -exec python3 html_to_text.py {} \;
}

# Process each datastore
for store in dbt gcp omni looker bigquery lookerstudio; do
    echo "Processing ${store} documentation..."
    urls=$(yq eval ".${store}_sources.primary[]" config.yaml)
    download_docs "${store}" "${urls}"
    
    # Upload to Cloud Storage
    gsutil -m cp -r "${TEMP_DIR}/${store}/*" "${BUCKET_BASE}/${store}/"
    
    # Update Vertex AI datastore
    gcloud ai datastores update "${store}" \
        --project="${PROJECT_ID}" \
        --source="${BUCKET_BASE}/${store}"
done

# Cleanup
rm -rf "${TEMP_DIR}"
