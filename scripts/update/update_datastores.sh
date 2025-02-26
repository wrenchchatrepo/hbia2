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
