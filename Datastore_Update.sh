# Datastore Update Process
#!/bin/bash

# Configuration
PROJECT_ID="your-project-id"
BUCKET_BASE="gs://your-bucket-base"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Function to update datastore
update_datastore() {
    local name=$1
    local source_path=$2
    
    # Backup existing data
    gsutil cp -r "${BUCKET_BASE}/${name}" "${BUCKET_BASE}/backup/${name}_${TIMESTAMP}"
    
    # Upload new data
    gsutil -m cp -r "${source_path}/" "${BUCKET_BASE}/${name}/"
    
    # Update Vertex AI datastore
    gcloud ai datastores update "${name}" \
        --project="${PROJECT_ID}" \
        --source="${BUCKET_BASE}/${name}"
}

# Update each datastore
update_datastore "dbt_store" "/path/to/dbt/docs"
update_datastore "gcp_arch_store" "/path/to/gcp/docs"
update_datastore "omni_store" "/path/to/omni/docs"
update_datastore "looker_store" "/path/to/looker/docs"
update_datastore "bigquery_store" "/path/to/bq/docs"
update_datastore "lookerstudio_store" "/path/to/lookerstudio/docs"
