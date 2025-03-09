#!/usr/bin/env python3
import os
import json
from pathlib import Path
import time
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import html2text
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class LookerApiScraper:
    def __init__(self, base_url, output_dir, timeout=30):
        self.base_url = base_url
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.timeout = timeout
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.delay = 1  # Delay between requests in seconds
        self.h2t = html2text.HTML2Text()
        self.h2t.ignore_links = False
        self.h2t.ignore_images = False
        self.h2t.body_width = 0  # No wrapping
        
        # Set up retry logic
        self.session = requests.Session()
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def extract_api_methods(self, soup):
        """Extract API methods and their details."""
        methods = {}
        
        # Find the API Methods section
        api_methods = soup.find('h2', string='Looker Application API Methods')
        if not api_methods:
            return methods
            
        current = api_methods.find_next_sibling()
        current_category = None
        
        while current:
            if current.name == 'h2':  # End of API Methods section
                break
                
            # Look for method categories (like Alert, ApiAuth, etc.)
            if current.name in ['h3', 'strong']:
                current_category = current.get_text().strip()
                if current_category and not current_category.startswith('Why') and not current_category.startswith('Products'):
                    methods[current_category] = []
                    
                    # Get the list of methods if it exists
                    method_list = current.find_next('ul')
                    if method_list:
                        for method in method_list.find_all('li'):
                            method_text = method.get_text().strip()
                            if method_text:
                                methods[current_category].append({
                                    'name': method_text,
                                    'description': ''
                                })
            
            current = current.find_next_sibling()
        
        # Remove empty categories
        methods = {k: v for k, v in methods.items() if v}
        return methods

    def extract_type_definitions(self, soup):
        """Extract type definitions and models."""
        types = {}
        
        # Find all type definition sections
        for category in ['Config', 'Connection', 'Content', 'Dashboard', 'DataAction',
                        'Datagroup', 'DerivedTable', 'Folder', 'Group', 'Homepage',
                        'Integration', 'Look', 'LookmlModel', 'Metadata', 'Project',
                        'Query', 'RenderTask', 'Role', 'ScheduledPlan', 'Session',
                        'SqlInterfaceQuery', 'Theme', 'User', 'UserAttribute', 'Workspace']:
            
            # Find the category header
            category_header = soup.find(['h2', 'h3', 'strong'], string=category)
            if category_header:
                types[category] = []
                
                # Get the list of types if it exists
                type_list = category_header.find_next('ul')
                if type_list:
                    for type_item in type_list.find_all('li'):
                        type_text = type_item.get_text().strip()
                        if type_text:
                            types[category].append({
                                'name': type_text,
                                'description': ''
                            })
        
        # Remove empty categories
        types = {k: v for k, v in types.items() if v}
        return types

    def save_api_documentation(self, methods, types):
        """Save the extracted API documentation."""
        # Save methods
        methods_file = self.output_dir / 'looker_api_methods.json'
        with open(methods_file, 'w') as f:
            json.dump(methods, f, indent=2)
        
        # Save type definitions
        types_file = self.output_dir / 'looker_api_types.json'
        with open(types_file, 'w') as f:
            json.dump(types, f, indent=2)
        
        # Create markdown version
        md_file = self.output_dir / 'looker_api_reference.md'
        with open(md_file, 'w') as f:
            f.write('# Looker API Reference\n\n')
            f.write('Version 4.0.25.2 (latest)\n\n')
            
            # Write methods
            f.write('## API Methods\n\n')
            for category, category_methods in methods.items():
                f.write(f'### {category}\n\n')
                for method in category_methods:
                    f.write(f"- {method['name']}\n")
                    if method.get('description'):
                        f.write(f"  {method['description']}\n")
                f.write('\n')
            
            # Write types
            f.write('## Type Definitions\n\n')
            for category, category_types in types.items():
                f.write(f'### {category}\n\n')
                for type_def in category_types:
                    f.write(f"- {type_def['name']}\n")
                    if type_def.get('description'):
                        f.write(f"  {type_def['description']}\n")
                f.write('\n')

    def scrape_api_reference(self):
        """Main method to scrape the API reference."""
        try:
            print(f"Fetching API reference from {self.base_url}")
            response = self.session.get(self.base_url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract methods and types
            methods = self.extract_api_methods(soup)
            types = self.extract_type_definitions(soup)
            
            # Save the documentation
            self.save_api_documentation(methods, types)
            
            print("API reference documentation has been successfully scraped and saved.")
            
        except Exception as e:
            print(f"Error scraping API reference: {str(e)}")
            raise

def main():
    # Configuration
    base_url = "https://cloud.google.com/looker/docs/reference/looker-api/latest"
    output_dir = "../scraped_content/looker_api_reference"
    
    # Create and run scraper
    scraper = LookerApiScraper(base_url, output_dir)
    scraper.scrape_api_reference()

if __name__ == "__main__":
    main() 