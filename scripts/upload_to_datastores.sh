#!/bin/bash

# Source environment variables
source .env

# Configuration
PROCESSED_DIR="temp_processed"
BUCKET_PREFIX="hbia2"

# Function to upload files with specific parser settings
upload_with_parser() {
    local datastore=$1
    local bucket="${BUCKET_PREFIX}-${datastore}"
    local source_dir="${PROCESSED_DIR}/${datastore}"
    local parser=$2
    
    echo "Uploading files to ${bucket} with ${parser} parser..."
    
    # Upload files with appropriate parser settings
    case $parser in
        "ocr")
            # Upload PDFs with OCR parser
            gsutil -m cp "${source_dir}/*.ocr.txt" "gs://${bucket}/"
            gcloud ai datastores update "${datastore}" \
                --project="${PROJECT_ID}" \
                --region="${REGION}" \
                --ocr-parser-enabled
            ;;
        "layout")
            # Upload HTML/DOCX/MD with layout parser
            gsutil -m cp "${source_dir}/*.layout.txt" "gs://${bucket}/"
            gcloud ai datastores update "${datastore}" \
                --project="${PROJECT_ID}" \
                --region="${REGION}" \
                --layout-parser-enabled
            ;;
        "digital")
            # Upload code files with digital parser
            gsutil -m cp "${source_dir}/*.txt" "gs://${bucket}/"
            gcloud ai datastores update "${datastore}" \
                --project="${PROJECT_ID}" \
                --region="${REGION}" \
                --digital-parser-enabled
            ;;
    esac
}

# Process each datastore
for datastore in $(ls "${PROCESSED_DIR}"); do
    echo "Processing datastore: ${datastore}"
    
    # Read processing metadata
    metadata_file="${PROCESSED_DIR}/${datastore}/processing_metadata.json"
    if [ -f "$metadata_file" ]; then
        # Process files by parser type
        for parser in "ocr" "layout" "digital"; do
            upload_with_parser "$datastore" "$parser"
        done
    else
        echo "Warning: No metadata file found for ${datastore}"
    fi
done

echo "Upload complete!" 