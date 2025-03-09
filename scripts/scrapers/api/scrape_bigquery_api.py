#!/usr/bin/env python3
import os
import json
import time
import requests
from bs4 import BeautifulSoup
from pathlib import Path

# Configuration
OUTPUT_DIR = os.path.join("scraped_content", "bigquery_api")
PROCESSED_DIR = os.path.join("temp_processed", "bigquery")
BIGQUERY_API_URL = "https://cloud.google.com/bigquery/docs/reference/rest"

def setup_directories():
    """Create necessary directories."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)

def scrape_bigquery_api():
    """Scrape the BigQuery API documentation using requests and BeautifulSoup."""
    print(f"Scraping BigQuery API documentation from {BIGQUERY_API_URL}...")
    
    try:
        # Send a GET request to the BigQuery API reference
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
        }
        response = requests.get(BIGQUERY_API_URL, headers=headers)
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the main content
        main_content = soup.find('article')
        content = main_content.get_text() if main_content else 'Content not found'
        
        # Extract API methods (h2 and h3 elements)
        methods = []
        for heading in soup.find_all(['h2', 'h3']):
            name = heading.get_text().strip()
            description = ''
            next_elem = heading.find_next_sibling()
            if next_elem and next_elem.name in ['p', 'div']:
                description = next_elem.get_text().strip()
            methods.append({'name': name, 'description': description})
        
        # Extract links to resource pages
        resource_links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if '/bigquery/docs/reference/rest/' in href:
                # Make sure we have absolute URLs
                if not href.startswith('http'):
                    if href.startswith('/'):
                        href = f"https://cloud.google.com{href}"
                    else:
                        href = f"https://cloud.google.com/{href}"
                
                resource_links.append({
                    'text': link.get_text().strip(),
                    'href': href
                })
        
        # Save the main content
        with open(os.path.join(OUTPUT_DIR, "bigquery_api_overview.md"), "w") as f:
            f.write("# BigQuery API Reference\n\n")
            f.write(content)
        
        # Save the methods
        with open(os.path.join(OUTPUT_DIR, "bigquery_api_methods.json"), "w") as f:
            json.dump(methods, f, indent=2)
        
        # Save the resource links
        with open(os.path.join(OUTPUT_DIR, "bigquery_api_resources.json"), "w") as f:
            json.dump(resource_links, f, indent=2)
        
        # Create processed version for data store
        with open(os.path.join(PROCESSED_DIR, "bigquery_api_overview.layout.txt"), "w") as f:
            f.write("# BigQuery API Reference\n\n")
            f.write(content)
        
        print(f"Saved BigQuery API documentation to {OUTPUT_DIR}")
        print(f"Files ready for data store upload are in: {PROCESSED_DIR}")
        
        return resource_links
    except Exception as e:
        print(f"Error scraping BigQuery API: {e}")
        return None

def scrape_resource_page(resource_url, resource_name):
    """Scrape a resource page using requests and BeautifulSoup."""
    print(f"Scraping resource: {resource_name} ({resource_url})")
    
    try:
        # Send a GET request to the resource page
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
        }
        response = requests.get(resource_url, headers=headers)
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the main content
        main_content = soup.find('article')
        content = main_content.get_text() if main_content else 'Content not found'
        
        # Extract methods (h2 and h3 elements)
        methods = []
        for heading in soup.find_all(['h2', 'h3']):
            name = heading.get_text().strip()
            description = ''
            next_elem = heading.find_next_sibling()
            if next_elem and next_elem.name in ['p', 'div']:
                description = next_elem.get_text().strip()
            methods.append({'name': name, 'description': description})
        
        # Create a safe filename
        safe_name = resource_name.replace(" ", "_").replace("/", "_").replace(".", "_").lower()
        
        # Save the main content
        with open(os.path.join(OUTPUT_DIR, f"bigquery_api_{safe_name}.md"), "w") as f:
            f.write(f"# BigQuery API: {resource_name}\n\n")
            f.write(content)
        
        # Save the methods
        with open(os.path.join(OUTPUT_DIR, f"bigquery_api_{safe_name}_methods.json"), "w") as f:
            json.dump(methods, f, indent=2)
        
        # Create processed version for data store
        with open(os.path.join(PROCESSED_DIR, f"bigquery_api_{safe_name}.layout.txt"), "w") as f:
            f.write(f"# BigQuery API: {resource_name}\n\n")
            f.write(content)
        
        print(f"Saved resource documentation to {OUTPUT_DIR}/bigquery_api_{safe_name}.md")
        return True
    except Exception as e:
        print(f"Error scraping resource {resource_name}: {e}")
        return False

def main():
    print("Starting BigQuery API documentation scraping...")
    setup_directories()
    
    resource_links = scrape_bigquery_api()
    
    if resource_links:
        print(f"Scraping {len(resource_links)} resource pages...")
        
        for i, link in enumerate(resource_links):
            resource_url = link["href"]
            resource_name = link["text"]
            
            print(f"Scraping resource {i+1}/{len(resource_links)}: {resource_name}")
            success = scrape_resource_page(resource_url, resource_name)
            
            if not success:
                print(f"Failed to scrape resource: {resource_name}")
            
            # Sleep to avoid rate limiting
            time.sleep(2)
    
    print("\nScraping complete!")
    print(f"Scraped files are in: {OUTPUT_DIR}")
    print(f"Files ready for data store upload are in: {PROCESSED_DIR}")

if __name__ == "__main__":
    main() 