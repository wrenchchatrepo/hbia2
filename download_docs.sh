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
