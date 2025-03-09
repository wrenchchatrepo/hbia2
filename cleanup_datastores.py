#!/usr/bin/env python3
import os
import json
import shutil
import hashlib
from pathlib import Path
from datetime import datetime

# Configuration
DATASTORES_DIR = "/Users/dionedge/dev/hbia2/datastores"

def calculate_file_hash(file_path):
    """Calculate MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def find_duplicates(directory):
    """Find duplicate files in a directory."""
    hash_dict = {}
    duplicates = []
    
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('_metadata.json'):
                continue
                
            file_path = os.path.join(root, filename)
            file_hash = calculate_file_hash(file_path)
            
            if file_hash in hash_dict:
                duplicates.append((file_path, hash_dict[file_hash]))
            else:
                hash_dict[file_hash] = file_path
                
    return duplicates

def remove_duplicates(duplicates):
    """Remove duplicate files, keeping the one with the shortest path."""
    for file1, file2 in duplicates:
        try:
            if len(file1) > len(file2):
                if os.path.exists(file1):
                    os.remove(file1)
                    print(f"Removed duplicate: {file1}")
            else:
                if os.path.exists(file2):
                    os.remove(file2)
                    print(f"Removed duplicate: {file2}")
        except FileNotFoundError:
            print(f"File already removed: {file1 if len(file1) > len(file2) else file2}")
        except Exception as e:
            print(f"Error removing file: {str(e)}")

def clean_empty_directories(directory):
    """Remove empty directories."""
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)
                    print(f"Removed empty directory: {dir_path}")
            except FileNotFoundError:
                print(f"Directory already removed: {dir_path}")
            except Exception as e:
                print(f"Error removing directory {dir_path}: {str(e)}")

def create_readme(datastore_dir, metadata_file):
    """Create a README.md file for the datastore."""
    try:
        with open(metadata_file, 'r') as f:
            metadata = json.load(f)
    except FileNotFoundError:
        metadata = {'repos': []}
    
    readme_content = f"""# {os.path.basename(datastore_dir).title()} Datastore

This directory contains repository files related to {os.path.basename(datastore_dir).title()}.

## Repository List

Total Repositories: {len(metadata['repos'])}

"""
    for repo in metadata['repos']:
        readme_content += f"- [{repo['name']}]({repo['url']})\n"
    
    readme_content += f"""
## Last Updated
{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    readme_path = os.path.join(datastore_dir, 'README.md')
    with open(readme_path, 'w') as f:
        f.write(readme_content)
    print(f"Created README for {datastore_dir}")

def cleanup_datastore(datastore_dir):
    """Clean up a single datastore directory."""
    print(f"\nCleaning up {datastore_dir}")
    
    # Find and remove duplicates
    duplicates = find_duplicates(datastore_dir)
    if duplicates:
        print(f"Found {len(duplicates)} duplicate files")
        remove_duplicates(duplicates)
    
    # Clean empty directories
    clean_empty_directories(datastore_dir)
    
    # Create README
    metadata_file = os.path.join(datastore_dir, f"{os.path.basename(datastore_dir)}_metadata.json")
    create_readme(datastore_dir, metadata_file)

def main():
    print("Starting datastores cleanup...")
    
    # Process each datastore directory
    for item in os.listdir(DATASTORES_DIR):
        datastore_dir = os.path.join(DATASTORES_DIR, item)
        if os.path.isdir(datastore_dir):
            cleanup_datastore(datastore_dir)
    
    print("\nCleanup complete!")

if __name__ == "__main__":
    main() 