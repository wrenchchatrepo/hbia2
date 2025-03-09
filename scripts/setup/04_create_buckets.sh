#!/bin/bash

# 03_create_buckets.sh
# Creates Google Cloud Storage buckets for datastores

# Exit on error
set -e

# Source environment variables
source .env

echo "=== Creating Google Cloud Storage buckets ==="

# Function to create a bucket if it doesn't exist
create_bucket() {
    local bucket_name=$1
    echo "Creating bucket: $bucket_name"
    
    if gsutil ls -b "$bucket_name" &>/dev/null; then
        echo "Bucket $bucket_name already exists."
    else
        gsutil mb -l $REGION -b on "$bucket_name"
        echo "Created bucket: $bucket_name"
    fi
}

# Create base bucket
echo "Creating base bucket..."
create_bucket "$BUCKET_BASE"

# Create datastore buckets
echo "Creating datastore buckets..."
for store in looker bigquery dbt gcp omni looker_studio; do
    bucket="${BUCKET_BASE%/}-${store}"
    create_bucket "$bucket"
done

echo "=== Bucket creation completed ==="
echo "You can now proceed to the next script: 04_upload_to_buckets.sh" 