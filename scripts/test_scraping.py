#!/usr/bin/env python3
import os
import json
from pathlib import Path

# Test URLs with different depths
TEST_URLS = [
    # Looker Studio URLs (depth 0-2)
    "https://developers.google.com/looker-studio",
    "https://developers.google.com/looker-studio/integrate/embed",
    "https://developers.google.com/looker-studio/integrate/linking-api",
    
    # BigQuery URLs (depth 0-2)
    "https://cloud.google.com/bigquery/docs",
    "https://cloud.google.com/bigquery/docs/reference/standard-sql",
    "https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax",
    
    # DBT URLs (depth 0-2)
    "https://docs.getdbt.com/docs/introduction",
    "https://docs.getdbt.com/docs/build/models",
    "https://docs.getdbt.com/docs/build/snapshots"
]

def create_test_markdown():
    """Create a test markdown file with test URLs."""
    test_file = "test_urls.md"
    with open(test_file, 'w') as f:
        f.write("# Test URLs for Scraping\n\n")
        for url in TEST_URLS:
            f.write(f"- {url}\n")
    return test_file

def test_scraping():
    """Run a test of the scraping functionality."""
    print("Starting scraping test...")
    
    # Create test markdown file
    test_file = create_test_markdown()
    print(f"Created test file: {test_file}")
    
    # Modify the DOCS_FILE path in scrape_docs.py
    original_docs_file = "scripts/scrape_docs.py"
    with open(original_docs_file, 'r') as f:
        content = f.read()
    
    # Replace the DOCS_FILE path
    new_content = content.replace(
        'DOCS_FILE = "/Users/dionedge/dev/hbia2/urls_docs_data_store.md"',
        f'DOCS_FILE = "{os.path.abspath(test_file)}"'
    )
    
    with open(original_docs_file, 'w') as f:
        f.write(new_content)
    
    # Run the scraping script
    print("\nRunning scraping script...")
    os.system('python3 scripts/scrape_docs.py')
    
    # Restore original DOCS_FILE path
    with open(original_docs_file, 'w') as f:
        f.write(content)
    
    # Analyze results
    print("\nAnalyzing results...")
    analyze_results()

def analyze_results():
    """Analyze the scraping results."""
    metadata_file = "scraped_docs/scraping_metadata.json"
    if not os.path.exists(metadata_file):
        print("Error: No metadata file found!")
        return
    
    with open(metadata_file, 'r') as f:
        metadata = json.load(f)
    
    print("\nTest Results:")
    print(f"Total base URLs: {metadata['total_base_urls']}")
    print(f"Total processed files: {metadata['total_processed_files']}")
    print(f"Max depth: {metadata['max_depth']}")
    
    # Analyze by datastore
    datastores = {}
    for result in metadata['results']:
        datastore = result['datastore']
        if datastore not in datastores:
            datastores[datastore] = []
        datastores[datastore].append(result)
    
    print("\nFiles by datastore:")
    for datastore, files in datastores.items():
        print(f"\n{datastore}:")
        for file in files:
            print(f"  - {file['file']} (depth: {file['depth']})")
    
    # Check for any errors or issues
    print("\nChecking for potential issues...")
    for result in metadata['results']:
        if result['depth'] > metadata['max_depth']:
            print(f"Warning: File {result['file']} exceeds max depth!")
        if not os.path.exists(result['file']):
            print(f"Warning: File {result['file']} not found!")

if __name__ == "__main__":
    test_scraping() 