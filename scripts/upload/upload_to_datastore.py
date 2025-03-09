#!/usr/bin/env python3
import os
import json
import argparse
import subprocess
from pathlib import Path

# Configuration
CONFIG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "config")
DATASTORE_MAPPINGS_FILE = os.path.join(CONFIG_DIR, "datastore_mappings.json")
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")

def load_datastore_mappings():
    """Load datastore mappings from configuration file."""
    with open(DATASTORE_MAPPINGS_FILE, 'r') as f:
        return json.load(f)

def upload_to_datastore(product, content_type, source_type, dry_run=False):
    """Upload content to data store.
    
    Args:
        product (str): Product name (e.g., bigquery, looker)
        content_type (str): Content type (api, docs, github)
        source_type (str): Source type (scraped, processed)
        dry_run (bool): If True, only print commands without executing
    """
    # Load datastore mappings
    datastore_mappings = load_datastore_mappings()
    
    # Check if product exists in mappings
    if product not in datastore_mappings:
        print(f"Error: Product '{product}' not found in datastore mappings")
        return
    
    # Get datastore name
    datastore_name = datastore_mappings[product]
    
    # Construct source directory
    source_dir = os.path.join(DATA_DIR, product, content_type, source_type)
    
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' not found")
        return
    
    # Find all files in the source directory
    files = []
    for root, _, filenames in os.walk(source_dir):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    
    if not files:
        print(f"No files found in {source_dir}")
        return
    
    # Upload each file to the datastore
    for file_path in files:
        # Get relative path from source directory
        rel_path = os.path.relpath(file_path, source_dir)
        
        # Construct document ID
        doc_id = f"{product}_{content_type}_{source_type}_{rel_path.replace('/', '_')}"
        
        # Determine file type
        file_ext = os.path.splitext(file_path)[1].lower()
        
        # Construct upload command based on file type
        if file_ext in ['.json']:
            # For JSON files, use the JSON content directly
            command = f"python3 -m datastore upload --datastore {datastore_name} --id {doc_id} --file {file_path} --json"
        elif file_ext in ['.md', '.txt']:
            # For text files, use the text content
            command = f"python3 -m datastore upload --datastore {datastore_name} --id {doc_id} --file {file_path} --text"
        else:
            # For other files, use the binary content
            command = f"python3 -m datastore upload --datastore {datastore_name} --id {doc_id} --file {file_path} --binary"
        
        # Print command
        print(f"Uploading {file_path} to {datastore_name} with ID {doc_id}")
        print(f"Command: {command}")
        
        # Execute command if not dry run
        if not dry_run:
            try:
                subprocess.run(command, shell=True, check=True)
                print(f"Successfully uploaded {file_path} to {datastore_name}")
            except subprocess.CalledProcessError as e:
                print(f"Error uploading to datastore: {e}")
        else:
            print("Dry run, command not executed")

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Upload content to data stores")
    parser.add_argument("--product", required=True, help="Product name (e.g., bigquery, looker)")
    parser.add_argument("--content-type", required=True, choices=["api", "docs", "github"], help="Content type")
    parser.add_argument("--source-type", required=True, choices=["scraped", "processed"], help="Source type")
    parser.add_argument("--dry-run", action="store_true", help="Dry run, don't execute commands")
    
    args = parser.parse_args()
    
    upload_to_datastore(args.product, args.content_type, args.source_type, args.dry_run)

if __name__ == "__main__":
    main() 