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
