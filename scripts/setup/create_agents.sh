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
