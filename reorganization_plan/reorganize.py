#!/usr/bin/env python3
"""
Repository Reorganization Script

This script reorganizes the repository structure to have six top-level product directories
with all scraped content properly organized within them.
"""

import os
import shutil
import glob
import re
from pathlib import Path
import argparse

# Define the products we're working with
PRODUCTS = ['bigquery', 'looker', 'dbt', 'gcp', 'omni', 'looker-studio']
CONTENT_TYPES = ['api', 'docs', 'github']

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.absolute()

def create_directory_structure():
    """Create the new directory structure."""
    print("Creating new directory structure...")
    
    # Create product directories
    for product in PRODUCTS:
        for content_type in CONTENT_TYPES:
            os.makedirs(os.path.join(PROJECT_ROOT, product, content_type, 'scraped'), exist_ok=True)
            os.makedirs(os.path.join(PROJECT_ROOT, product, content_type, 'processed'), exist_ok=True)
    
    # Create archive directories
    for product in PRODUCTS:
        os.makedirs(os.path.join(PROJECT_ROOT, 'archive', product), exist_ok=True)
    
    # Create script directories
    script_dirs = ['main', 'processors', 'scrapers', 'setup', 'update', 'utils']
    for script_dir in script_dirs:
        os.makedirs(os.path.join(PROJECT_ROOT, 'scripts', script_dir), exist_ok=True)
    
    # Additional directories
    os.makedirs(os.path.join(PROJECT_ROOT, 'config'), exist_ok=True)
    os.makedirs(os.path.join(PROJECT_ROOT, 'docs'), exist_ok=True)
    os.makedirs(os.path.join(PROJECT_ROOT, 'utils'), exist_ok=True)

def get_product_from_filename(filename):
    """Determine which product a file belongs to based on its name."""
    filename_lower = filename.lower()
    
    # Direct product matches
    for product in PRODUCTS:
        if product.lower().replace('-', '_') in filename_lower.replace('-', '_'):
            return product
    
    # Check for specific patterns
    if 'bigquery' in filename_lower or 'bq_' in filename_lower:
        return 'bigquery'
    elif 'looker' in filename_lower and 'studio' in filename_lower:
        return 'looker-studio'
    elif 'looker' in filename_lower:
        return 'looker'
    elif 'dbt' in filename_lower:
        return 'dbt'
    elif 'gcp' in filename_lower or 'cloud.google' in filename_lower:
        return 'gcp'
    elif 'omni' in filename_lower:
        return 'omni'
    
    # Check for URL patterns
    if 'cloud.google.com/bigquery' in filename_lower:
        return 'bigquery'
    elif 'cloud.google.com/looker-studio' in filename_lower or 'developers.google.com/looker-studio' in filename_lower:
        return 'looker-studio'
    elif 'cloud.google.com/looker' in filename_lower:
        return 'looker'
    elif 'docs.getdbt.com' in filename_lower:
        return 'dbt'
    elif 'cloud.google.com' in filename_lower:
        return 'gcp'
    elif 'bigquery/docs/omni' in filename_lower:
        return 'omni'
    
    # Default to GCP if we can't determine
    return None

def get_content_type_from_filename(filename, product):
    """Determine the content type for a file based on its name."""
    filename_lower = filename.lower()
    
    # Check for API indicators
    if 'api' in filename_lower or 'reference' in filename_lower:
        return 'api'
    
    # Check for GitHub indicators
    if 'github.com' in filename_lower or 'github' in filename_lower:
        return 'github'
    
    # Default to docs for everything else
    return 'docs'

def should_archive(filepath):
    """Determine if a file should be archived (duplicate TXT when MD exists)."""
    if filepath.endswith('.txt'):
        md_filepath = filepath[:-4] + '.md'
        if os.path.exists(md_filepath):
            return True
    return False

def move_file(src, dest, dry_run=False):
    """Move a file from source to destination, creating directories as needed."""
    if dry_run:
        print(f"Would move: {src} -> {dest}")
        return
    
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if os.path.exists(dest):
        # If destination exists, append a number to avoid overwriting
        base, ext = os.path.splitext(dest)
        counter = 1
        while os.path.exists(f"{base}_{counter}{ext}"):
            counter += 1
        dest = f"{base}_{counter}{ext}"
    
    try:
        shutil.move(src, dest)
        print(f"Moved: {src} -> {dest}")
    except Exception as e:
        print(f"Error moving {src} to {dest}: {e}")

def process_directory(source_dir, dry_run=False):
    """Process a directory, moving files to their appropriate locations."""
    if not os.path.exists(source_dir):
        print(f"Directory doesn't exist: {source_dir}")
        return
    
    print(f"Processing directory: {source_dir}")
    
    # Count total files for progress reporting
    total_files = sum([len(files) for _, _, files in os.walk(source_dir)])
    processed = 0
    moved = 0
    archived = 0
    skipped = 0
    
    # Process all files in the directory and its subdirectories
    for root, _, files in os.walk(source_dir):
        for filename in files:
            filepath = os.path.join(root, filename)
            
            # Skip non-content files
            if filename.startswith('.') or filename in ['README.md', 'structure.md', 'reorganize.py']:
                skipped += 1
                continue
            
            # Determine which product and content type this file belongs to
            product = get_product_from_filename(filepath)
            if not product:
                print(f"Couldn't determine product for: {filepath}")
                skipped += 1
                continue
                
            content_type = get_content_type_from_filename(filepath, product)
            
            # Determine destination
            if should_archive(filepath):
                dest = os.path.join(PROJECT_ROOT, 'archive', product, os.path.basename(filepath))
                archived += 1
            else:
                dest = os.path.join(PROJECT_ROOT, product, content_type, 'scraped', os.path.basename(filepath))
                moved += 1
            
            # Move the file
            move_file(filepath, dest, dry_run)
            
            processed += 1
            if processed % 50 == 0:
                print(f"Progress: {processed}/{total_files} files ({processed/total_files*100:.1f}%)")
    
    print(f"Directory summary for {source_dir}:")
    print(f"  - Total files: {total_files}")
    print(f"  - Moved to product directories: {moved}")
    print(f"  - Archived: {archived}")
    print(f"  - Skipped: {skipped}")
    
    return moved, archived, skipped

def reorganize_scripts(dry_run=False):
    """Reorganize scripts into their appropriate categories."""
    source_dir = os.path.join(PROJECT_ROOT, 'scripts')
    if not os.path.exists(source_dir):
        print("Scripts directory doesn't exist.")
        return
    
    print("Reorganizing scripts...")
    
    # Define patterns for different script categories
    script_patterns = {
        'main': [r'0\d_.*\.sh', r'main\.py'],
        'processors': [r'process.*\.py', r'.*_processor\.py'],
        'scrapers': [r'scrap.*\.py', r'.*_scraper\.py', r'download.*\.py'],
        'setup': [r'setup.*\.py', r'.*_setup\.py', r'install.*\.py'],
        'update': [r'update.*\.py', r'.*_update\.py'],
        'utils': [r'util.*\.py', r'.*_util\.py', r'track.*\.py', r'helper.*\.py']
    }
    
    # Process all Python and shell scripts in the scripts directory
    for root, _, files in os.walk(source_dir):
        for filename in files:
            if not (filename.endswith('.py') or filename.endswith('.sh')):
                continue
                
            filepath = os.path.join(root, filename)
            
            # Skip files already in organized directories
            if any(category in filepath for category in script_patterns.keys()):
                continue
            
            # Determine which category this script belongs to
            category = None
            for cat, patterns in script_patterns.items():
                if any(re.search(pattern, filename) for pattern in patterns):
                    category = cat
                    break
            
            if not category:
                # If we can't determine, default to 'utils'
                category = 'utils'
            
            # Determine destination
            dest = os.path.join(PROJECT_ROOT, 'scripts', category, filename)
            
            # Move the file
            move_file(filepath, dest, dry_run)

def main():
    """Main function to reorganize the repository."""
    parser = argparse.ArgumentParser(description='Reorganize the repository structure.')
    parser.add_argument('--dry-run', action='store_true', help='Print actions without executing them')
    parser.add_argument('--simulate', action='store_true', help='Only simulate the directory structure without processing files')
    args = parser.parse_args()
    
    # Create the new directory structure
    create_directory_structure()
    
    if args.simulate:
        print("Directory structure created. Skipping file processing (--simulate flag used).")
        return
    
    # Initialize counters for grand total
    total_moved = 0
    total_archived = 0
    total_skipped = 0
    
    # Process source directories
    source_dirs = [
        os.path.join(PROJECT_ROOT, 'scraped_content'),
        os.path.join(PROJECT_ROOT, 'scraped_docs'),
        os.path.join(PROJECT_ROOT, 'temp_docs'),
        os.path.join(PROJECT_ROOT, 'cloud.google.com')
    ]
    
    for source_dir in source_dirs:
        moved, archived, skipped = process_directory(source_dir, args.dry_run)
        total_moved += moved
        total_archived += archived
        total_skipped += skipped
    
    # Process data directories
    for product in PRODUCTS:
        for content_type in CONTENT_TYPES:
            source_dir = os.path.join(PROJECT_ROOT, 'data', product, content_type)
            if os.path.exists(source_dir):
                moved, archived, skipped = process_directory(source_dir, args.dry_run)
                total_moved += moved
                total_archived += archived
                total_skipped += skipped
    
    # Reorganize scripts
    reorganize_scripts(args.dry_run)
    
    print("\n=== Reorganization Summary ===")
    print(f"Total files moved to product directories: {total_moved}")
    print(f"Total files archived: {total_archived}")
    print(f"Total files skipped: {total_skipped}")
    print(f"Grand total: {total_moved + total_archived + total_skipped}")
    
    if not args.dry_run:
        print("\nYou may want to remove the following directories if they're now empty:")
        for dir_to_remove in ['scraped_content', 'scraped_docs', 'temp_docs', 'cloud.google.com']:
            print(f"  - {os.path.join(PROJECT_ROOT, dir_to_remove)}")

if __name__ == '__main__':
    main() 