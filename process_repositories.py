#!/usr/bin/env python3
import os
import json
import subprocess
import shutil
from tqdm import tqdm
from dotenv import load_dotenv
import time
import re
from pathlib import Path

# Load environment variables
load_dotenv()

# Configuration
TEMP_DIR = "temp_repos"
DATASTORES_DIR = "/Users/dionedge/dev/hbia2/datastores"

# Datastore definitions with their corresponding folder names
DATASTORES = {
    'looker': {
        'keywords': ['looker', 'lookml', 'looker studio'],
        'repos': []
    },
    'looker-studio': {
        'keywords': ['looker studio', 'data studio', 'google data studio'],
        'repos': []
    },
    'bigquery': {
        'keywords': ['bigquery', 'bq', 'big query'],
        'repos': []
    },
    'gcpp': {
        'keywords': ['gcp', 'google cloud', 'cloud platform', 'vertex ai', 'composer'],
        'repos': []
    },
    'dbt': {
        'keywords': ['dbt', 'data build tool', 'data modeling'],
        'repos': []
    },
    'omni': {
        'keywords': ['omni', 'omni.co'],
        'repos': []
    }
}

# Files to exclude
EXCLUDED_FILES = {
    'LICENSE', '.gitignore', '.DS_Store', 'package.json',
    'package-lock.json', 'yarn.lock', 'requirements.txt', 'setup.py',
    'Makefile', 'Dockerfile', '.dockerignore', '.env', '.env.example',
    '*.pyc', '__pycache__', 'node_modules', 'dist', 'build', '.git',
    'CONTRIBUTING.md', 'CHANGELOG.md', 'AUTHORS', '*.ini', '*.cfg',
    '*.yml', '*.yaml', '*.json', '*.lock', '*.md', '*.rst', '*.txt'
}

def setup_directories():
    """Create necessary directories."""
    os.makedirs(TEMP_DIR, exist_ok=True)
    os.makedirs(DATASTORES_DIR, exist_ok=True)
    for datastore in DATASTORES:
        os.makedirs(os.path.join(DATASTORES_DIR, datastore), exist_ok=True)

def clean_url(url):
    """Clean URL by removing markdown formatting and whitespace."""
    url = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\2', url)
    url = url.strip()
    url = url.rstrip('.')
    github_match = re.search(r'https://github\.com/[^/]+/[^/\s]+', url)
    if github_match:
        url = github_match.group(0)
    return url

def clone_repository(repo_url, repo_name):
    """Clone a repository to the temp directory."""
    try:
        repo_path = os.path.join(TEMP_DIR, repo_name)
        if os.path.exists(repo_path):
            shutil.rmtree(repo_path)
        
        subprocess.run(['git', 'clone', '--depth', '1', repo_url, repo_path], 
                      check=True, capture_output=True)
        return repo_path
    except subprocess.CalledProcessError as e:
        print(f"Error cloning {repo_url}: {e.stderr.decode()}")
        return None

def should_exclude_file(filename):
    """Check if file should be excluded based on patterns."""
    return any(
        re.match(pattern.replace('*', '.*'), filename)
        for pattern in EXCLUDED_FILES
    )

def copy_repository_files(repo_path, repo_name, target_dir):
    """Copy files from repository to target directory."""
    for root, _, files in os.walk(repo_path):
        for file in files:
            if not should_exclude_file(file):
                source_path = os.path.join(root, file)
                # Create relative path from repo root
                rel_path = os.path.relpath(source_path, repo_path)
                target_path = os.path.join(target_dir, repo_name, rel_path)
                
                # Create target directory if it doesn't exist
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                
                try:
                    shutil.copy2(source_path, target_path)
                except Exception as e:
                    print(f"Error copying {source_path}: {str(e)}")

def determine_datastore(repo_url, repo_name):
    """Determine which datastore a repository belongs to."""
    text_to_check = f"{repo_url} {repo_name}".lower()
    matches = {}
    for datastore, config in DATASTORES.items():
        matches[datastore] = sum(
            1 for keyword in config['keywords']
            if keyword.lower() in text_to_check
        )
    return max(matches.items(), key=lambda x: x[1])[0]

def process_repository(repo_url):
    """Process a single repository."""
    repo_name = repo_url.split('/')[-1]
    repo_path = clone_repository(repo_url, repo_name)
    
    if not repo_path:
        return
    
    try:
        datastore = determine_datastore(repo_url, repo_name)
        target_dir = os.path.join(DATASTORES_DIR, datastore)
        
        # Copy files to appropriate datastore directory
        copy_repository_files(repo_path, repo_name, target_dir)
        
        # Add to appropriate datastore metadata
        DATASTORES[datastore]['repos'].append({
            'url': repo_url,
            'name': repo_name
        })
        
        # Save metadata to JSON file
        output_file = os.path.join(target_dir, f"{datastore}_metadata.json")
        with open(output_file, 'w') as f:
            json.dump(DATASTORES[datastore], f, indent=2)
            
    finally:
        # Clean up cloned repository
        if os.path.exists(repo_path):
            shutil.rmtree(repo_path)

def process_batch(repo_urls, batch_number, total_batches):
    """Process a batch of repositories."""
    print(f"\nProcessing batch {batch_number}/{total_batches}")
    for repo_url in tqdm(repo_urls, desc=f"Batch {batch_number}"):
        process_repository(repo_url)
        time.sleep(5)  # Small delay between repositories

def cleanup():
    """Clean up temporary directory."""
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)

def main():
    # Setup directories
    setup_directories()
    
    # Get all repositories from merged_urls_datastore.md
    with open('merged_urls_datastore.md', 'r') as f:
        content = f.read()
    
    # Extract GitHub repository URLs
    repo_urls = re.findall(r'https://github\.com/[^/]+/[^/\s]+', content)
    repo_urls = [clean_url(url) for url in repo_urls]
    repo_urls = list(set(repo_urls))  # Remove duplicates
    
    if not repo_urls:
        print("No repositories found to process!")
        return
    
    print(f"Found {len(repo_urls)} repositories to process")
    
    # Process repositories in batches
    BATCH_SIZE = 5
    total_batches = (len(repo_urls) + BATCH_SIZE - 1) // BATCH_SIZE
    
    try:
        for i in range(0, len(repo_urls), BATCH_SIZE):
            batch = repo_urls[i:i + BATCH_SIZE]
            batch_number = (i // BATCH_SIZE) + 1
            process_batch(batch, batch_number, total_batches)
            
            if batch_number < total_batches:
                print(f"\nCompleted batch {batch_number}. Waiting 30 seconds before next batch...")
                time.sleep(30)
        
        # Print summary
        print("\nProcessing complete! Summary:")
        for datastore, data in DATASTORES.items():
            print(f"{datastore}: {len(data['repos'])} repositories")
            
    finally:
        # Clean up temporary directory
        cleanup()

if __name__ == "__main__":
    main() 