#!/usr/bin/env python3
import os
import subprocess
import json
from pathlib import Path
from datetime import datetime
import re
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
import time

# Configuration
DOCS_FILE = "/Users/dionedge/dev/hbia2/urls_docs_data_store.md"
TEMP_DIR = "temp_docs"
OUTPUT_DIR = "scraped_docs"
MAX_DEPTH = 5
DELAY = 1  # Delay between requests in seconds

def setup_directories():
    """Create necessary directories."""
    os.makedirs(TEMP_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def read_urls_from_markdown(file_path):
    """Extract URLs from markdown file."""
    urls = []
    with open(file_path, 'r') as f:
        for line in f:
            # Match URLs in markdown format
            matches = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', line)
            for _, url in matches:
                urls.append(url)
            # Match plain URLs
            matches = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', line)
            urls.extend(matches)
    return list(set(urls))  # Remove duplicates

def get_url_depth(base_url, current_url):
    """Calculate the depth of a URL relative to the base URL."""
    base_path = urlparse(base_url).path.strip('/').split('/')
    current_path = urlparse(current_url).path.strip('/').split('/')
    
    # Count common path segments
    depth = 0
    for i in range(min(len(base_path), len(current_path))):
        if base_path[i] == current_path[i]:
            depth += 1
        else:
            break
    
    return len(current_path) - depth

def is_valid_url(url, base_url):
    """Check if URL is valid and within the same domain as base_url."""
    try:
        parsed_url = urlparse(url)
        parsed_base = urlparse(base_url)
        return (
            parsed_url.netloc == parsed_base.netloc and
            parsed_url.scheme in ['http', 'https']
        )
    except:
        return False

def extract_links(html_file):
    """Extract links from an HTML file using BeautifulSoup."""
    if not os.path.exists(html_file):
        print(f"Warning: HTML file not found: {html_file}")
        return []
    
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        
        links = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            if href.startswith('http'):
                links.append(href)
            elif href.startswith('/'):
                # Convert relative URL to absolute
                parsed = urlparse(html_file)
                base_url = f"{parsed.scheme}://{parsed.netloc}"
                links.append(urljoin(base_url, href))
        
        return list(set(links))  # Remove duplicates
    except Exception as e:
        print(f"Error extracting links from {html_file}: {str(e)}")
        return []

def scrape_url(url, base_url, depth=0):
    """Scrape a single URL and its nested pages up to MAX_DEPTH."""
    if depth > MAX_DEPTH:
        return []
    
    try:
        # Create a safe filename from URL
        safe_name = re.sub(r'[^\w\-_.]', '_', url)
        output_file = os.path.join(TEMP_DIR, f"{safe_name}.html")
        
        # Use requests to download the page
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Save the HTML content
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        # Add delay between requests
        time.sleep(DELAY)
        
        # Process nested links
        nested_files = []
        try:
            links = extract_links(output_file)
            for link in links:
                if is_valid_url(link, base_url) and get_url_depth(base_url, link) <= MAX_DEPTH:
                    nested_files.extend(scrape_url(link, base_url, depth + 1))
        except Exception as e:
            print(f"Error extracting links from {url}: {str(e)}")
        
        return [output_file] + nested_files
    except Exception as e:
        print(f"Error processing {url}: {str(e)}")
        return []

def convert_to_text(html_file):
    """Convert HTML to text using lynx."""
    try:
        text_file = html_file.replace('.html', '.txt')
        cmd = ['lynx', '-dump', html_file]
        with open(text_file, 'w') as f:
            subprocess.run(cmd, stdout=f, check=True)
        return True, text_file
    except subprocess.CalledProcessError as e:
        return False, str(e)

def determine_datastore(url):
    """Determine which datastore a URL belongs to based on content."""
    url_lower = url.lower()
    
    # Looker Studio patterns
    if 'looker-studio' in url_lower or 'data studio' in url_lower:
        return 'looker-studio'
    
    # BigQuery patterns
    if 'bigquery' in url_lower or 'bq' in url_lower:
        return 'bigquery'
    
    # DBT patterns
    if 'dbt' in url_lower or 'getdbt' in url_lower:
        return 'dbt'
    
    # GCP patterns
    if 'cloud.google.com' in url_lower:
        return 'gcp'
    
    # Looker patterns
    if 'looker' in url_lower:
        return 'looker'
    
    # Default to looker if no match
    return 'looker'

def main():
    print("Starting documentation scraping process...")
    setup_directories()
    
    # Read URLs from markdown file
    urls = read_urls_from_markdown(DOCS_FILE)
    print(f"Found {len(urls)} base URLs to process")
    
    results = []
    for base_url in urls:
        print(f"\nProcessing base URL: {base_url}")
        
        # Scrape URL and its nested pages
        html_files = scrape_url(base_url, base_url)
        print(f"Found {len(html_files)} pages to process")
        
        for html_file in html_files:
            # Convert to text
            success, text_file = convert_to_text(html_file)
            if not success:
                print(f"Failed to convert {html_file}: {text_file}")
                continue
            
            # Determine datastore
            datastore = determine_datastore(html_file)
            
            # Move to appropriate directory
            target_dir = os.path.join(OUTPUT_DIR, datastore)
            os.makedirs(target_dir, exist_ok=True)
            target_file = os.path.join(target_dir, os.path.basename(text_file))
            os.rename(text_file, target_file)
            
            results.append({
                'url': base_url,
                'file': target_file,
                'datastore': datastore,
                'depth': get_url_depth(base_url, html_file),
                'timestamp': datetime.now().isoformat()
            })
            
            print(f"Successfully processed {html_file}")
    
    # Save processing metadata
    metadata_file = os.path.join(OUTPUT_DIR, 'scraping_metadata.json')
    with open(metadata_file, 'w') as f:
        json.dump({
            'total_base_urls': len(urls),
            'total_processed_files': len(results),
            'max_depth': MAX_DEPTH,
            'results': results,
            'timestamp': datetime.now().isoformat()
        }, f, indent=2)
    
    print(f"\nProcessing complete! Processed {len(results)} files")
    print(f"Results are in: {OUTPUT_DIR}")
    print("\nNext steps:")
    print("1. Review the scraped content")
    print("2. Run process_files_for_datastores.py to prepare for upload")
    print("3. Run upload_to_datastores.sh to upload to GCS")

if __name__ == "__main__":
    main() 