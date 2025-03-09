#!/usr/bin/env python3
import os
import json
import argparse
import subprocess
from pathlib import Path

# Configuration
CONFIG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "config")
BUCKET_MAPPINGS_FILE = os.path.join(CONFIG_DIR, "bucket_mappings.json")
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data")

def load_bucket_mappings():
    """Load bucket mappings from configuration file."""
    with open(BUCKET_MAPPINGS_FILE, 'r') as f:
        return json.load(f)

def upload_to_bucket(product, content_type, source_type, dry_run=False):
    """Upload content to GS bucket.
    
    Args:
        product (str): Product name (e.g., bigquery, looker)
        content_type (str): Content type (api, docs, github)
        source_type (str): Source type (scraped, processed)
        dry_run (bool): If True, only print commands without executing
    """
    # Load bucket mappings
    bucket_mappings = load_bucket_mappings()
    
    # Check if product exists in mappings
    if product not in bucket_mappings:
        print(f"Error: Product '{product}' not found in bucket mappings")
        return
    
    # Get bucket name
    bucket_name = bucket_mappings[product]
    
    # Construct source directory
    source_dir = os.path.join(DATA_DIR, product, content_type, source_type)
    
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' not found")
        return
    
    # Construct destination path
    destination_path = f"{bucket_name}/{content_type}/{source_type}/"
    
    # Construct gsutil command
    command = f"gsutil -m cp -r {source_dir}/* {destination_path}"
    
    # Print command
    print(f"Uploading {source_dir} to {destination_path}")
    print(f"Command: {command}")
    
    # Execute command if not dry run
    if not dry_run:
        try:
            subprocess.run(command, shell=True, check=True)
            print(f"Successfully uploaded {source_dir} to {destination_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error uploading to bucket: {e}")
    else:
        print("Dry run, command not executed")

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Upload content to GS buckets")
    parser.add_argument("--product", required=True, help="Product name (e.g., bigquery, looker)")
    parser.add_argument("--content-type", required=True, choices=["api", "docs", "github"], help="Content type")
    parser.add_argument("--source-type", required=True, choices=["scraped", "processed"], help="Source type")
    parser.add_argument("--dry-run", action="store_true", help="Dry run, don't execute commands")
    
    args = parser.parse_args()
    
    upload_to_bucket(args.product, args.content_type, args.source_type, args.dry_run)

if __name__ == "__main__":
    main() 