#!/usr/bin/env python3
import os
import shutil
from pathlib import Path
import json
from datetime import datetime

# Configuration
DATASTORES_DIR = "/Users/dionedge/dev/hbia2/datastores"
TEMP_DIR = "temp_processed"

# Parser configurations
PARSER_CONFIGS = {
    'ocr': {
        'extensions': ['.pdf'],
        'suffix': '.ocr.txt'
    },
    'digital': {
        'extensions': ['.lkml', '.py', '.js', '.ts'],
        'suffix': '.txt'
    },
    'layout': {
        'extensions': ['.html', '.docx', '.md'],
        'suffix': '.layout.txt'
    }
}

def setup_directories():
    """Create necessary directories."""
    os.makedirs(TEMP_DIR, exist_ok=True)
    for datastore in os.listdir(DATASTORES_DIR):
        datastore_path = os.path.join(DATASTORES_DIR, datastore)
        if os.path.isdir(datastore_path):
            os.makedirs(os.path.join(TEMP_DIR, datastore), exist_ok=True)

def determine_parser(file_path):
    """Determine which parser to use based on file extension."""
    ext = os.path.splitext(file_path)[1].lower()
    for parser, config in PARSER_CONFIGS.items():
        if ext in config['extensions']:
            return parser, config['suffix']
    return 'digital', '.txt'  # Default to digital parser

def process_file(source_path, target_dir):
    """Process a single file and copy it to the target directory with appropriate suffix."""
    parser, suffix = determine_parser(source_path)
    filename = os.path.basename(source_path)
    base_name = os.path.splitext(filename)[0]
    new_name = f"{base_name}{suffix}"
    target_path = os.path.join(target_dir, new_name)
    
    # Copy file with new name
    shutil.copy2(source_path, target_path)
    return {
        'original_name': filename,
        'processed_name': new_name,
        'parser': parser,
        'timestamp': datetime.now().isoformat()
    }

def process_datastore(datastore_dir):
    """Process all files in a datastore directory."""
    datastore_name = os.path.basename(datastore_dir)
    target_dir = os.path.join(TEMP_DIR, datastore_name)
    processed_files = []
    
    print(f"\nProcessing datastore: {datastore_name}")
    
    # Process all files in the datastore directory
    for root, _, files in os.walk(datastore_dir):
        for file in files:
            source_path = os.path.join(root, file)
            try:
                result = process_file(source_path, target_dir)
                processed_files.append(result)
                print(f"Processed: {file} → {result['processed_name']} ({result['parser']} parser)")
            except Exception as e:
                print(f"Error processing {file}: {str(e)}")
    
    # Save processing metadata
    metadata_file = os.path.join(target_dir, 'processing_metadata.json')
    with open(metadata_file, 'w') as f:
        json.dump({
            'datastore': datastore_name,
            'processed_files': processed_files,
            'timestamp': datetime.now().isoformat()
        }, f, indent=2)
    
    return processed_files

def main():
    print("Starting file processing for datastores...")
    setup_directories()
    
    total_processed = 0
    for item in os.listdir(DATASTORES_DIR):
        datastore_dir = os.path.join(DATASTORES_DIR, item)
        if os.path.isdir(datastore_dir):
            processed = process_datastore(datastore_dir)
            total_processed += len(processed)
    
    print(f"\nProcessing complete! Total files processed: {total_processed}")
    print(f"Processed files are in: {TEMP_DIR}")
    print("\nNext steps:")
    print("1. Review the processed files in the temp directory")
    print("2. Upload files to GCS buckets using the appropriate parser settings")
    print("3. Update the data stores with the new content")

if __name__ == "__main__":
    main() 