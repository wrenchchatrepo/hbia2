#!/usr/bin/env python3
"""
URL Tracking Utility

This script tracks URLs that have been scraped and identifies URLs that are yet to be scraped,
organized by product (BigQuery, Looker, DBT, GCP, Omni, Looker Studio) and content type
(API documentation, general documentation, GitHub repositories).
"""

import os
import json
import glob
import pandas as pd
from datetime import datetime
from typing import Dict, List, Set, Tuple
from pathlib import Path
import argparse
import yaml

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent.absolute()

# Define the products we're tracking
PRODUCTS = ['bigquery', 'looker', 'dbt', 'gcp', 'omni', 'looker-studio']
CONTENT_TYPES = ['api', 'docs', 'github']

class URLTracker:
    def __init__(self, config_path: str = None):
        """Initialize the URL tracker with the given configuration file."""
        self.config_path = config_path or os.path.join(PROJECT_ROOT, 'data', 'url_config.yml')
        self.config = self._load_config()
        self.data_dir = os.path.join(PROJECT_ROOT, 'data')
        self.scraped_dir = os.path.join(PROJECT_ROOT, 'scraped_content')
        self.results = self._initialize_results()
        
    def _load_config(self) -> Dict:
        """Load configuration from YAML file."""
        try:
            with open(self.config_path, 'r') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"Error loading config: {e}")
            return {
                'github_repos': {'batch_size': 5},
                'documentation_sites': {'batch_size': 3},
                'output': {'reference_dir': 'references', 'content_dir': 'content', 'text_dir': 'text'}
            }
            
    def _initialize_results(self) -> Dict:
        """Initialize the results dictionary with all products and content types."""
        results = {}
        for product in PRODUCTS:
            results[product] = {}
            for content_type in CONTENT_TYPES:
                results[product][content_type] = {
                    'urls_to_scrape': [],
                    'urls_scraped': [],
                    'last_updated': None,
                    'total_urls': 0,
                    'scraped_count': 0,
                    'pending_count': 0
                }
        return results
        
    def _load_target_urls(self) -> Dict[str, Dict[str, List[str]]]:
        """Load target URLs from URL configuration files for each product and content type."""
        target_urls = {}
        
        # Check for product-specific URL files
        for product in PRODUCTS:
            target_urls[product] = {'api': [], 'docs': [], 'github': []}
            
            # Load API URLs
            api_url_file = os.path.join(self.data_dir, product, 'api', 'urls.txt')
            if os.path.exists(api_url_file):
                with open(api_url_file, 'r') as f:
                    target_urls[product]['api'] = [line.strip() for line in f 
                                                 if line.strip() 
                                                 and not line.strip().startswith('#')]
                    
            # Load docs URLs
            docs_url_file = os.path.join(self.data_dir, product, 'docs', 'urls.txt')
            if os.path.exists(docs_url_file):
                with open(docs_url_file, 'r') as f:
                    target_urls[product]['docs'] = [line.strip() for line in f 
                                                  if line.strip() 
                                                  and not line.strip().startswith('#')]
                    
            # Load GitHub URLs
            github_url_file = os.path.join(self.data_dir, product, 'github', 'urls.txt')
            if os.path.exists(github_url_file):
                with open(github_url_file, 'r') as f:
                    target_urls[product]['github'] = [line.strip() for line in f 
                                                    if line.strip() 
                                                    and not line.strip().startswith('#')]
        
        return target_urls
        
    def _scan_scraped_content(self) -> Dict[str, Dict[str, Set[str]]]:
        """Scan the scraped content directory to identify scraped URLs."""
        scraped_urls = {}
        
        for product in PRODUCTS:
            scraped_urls[product] = {'api': set(), 'docs': set(), 'github': set()}
            
            # Check API scraped content
            api_dir = os.path.join(self.data_dir, product, 'api', 'scraped')
            if os.path.exists(api_dir):
                # Find all .md and .txt files in the API directory
                api_files = glob.glob(os.path.join(api_dir, '*.md')) + glob.glob(os.path.join(api_dir, '*.txt'))
                for file_path in api_files:
                    # Extract URL from file content (usually in the first few lines)
                    try:
                        with open(file_path, 'r') as f:
                            content = f.read(500)  # Read first 500 chars
                            # Look for URL patterns in the content
                            if 'http://' in content or 'https://' in content:
                                lines = content.split('\n')
                                for line in lines:
                                    if line.startswith('Source:') and ('http://' in line or 'https://' in line):
                                        url = line.replace('Source:', '').strip()
                                        scraped_urls[product]['api'].add(url)
                                        break
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")
            
            # Check docs scraped content
            docs_dir = os.path.join(self.data_dir, product, 'docs', 'scraped')
            if os.path.exists(docs_dir):
                docs_files = glob.glob(os.path.join(docs_dir, '*.md')) + glob.glob(os.path.join(docs_dir, '*.txt'))
                for file_path in docs_files:
                    try:
                        with open(file_path, 'r') as f:
                            content = f.read(500)
                            if 'http://' in content or 'https://' in content:
                                lines = content.split('\n')
                                for line in lines:
                                    if line.startswith('Source:') and ('http://' in line or 'https://' in line):
                                        url = line.replace('Source:', '').strip()
                                        scraped_urls[product]['docs'].add(url)
                                        break
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")
            
            # Check GitHub scraped content
            github_dir = os.path.join(self.data_dir, product, 'github', 'scraped')
            if os.path.exists(github_dir):
                github_files = glob.glob(os.path.join(github_dir, '*.md')) + glob.glob(os.path.join(github_dir, '*.txt'))
                for file_path in github_files:
                    try:
                        with open(file_path, 'r') as f:
                            content = f.read(500)
                            if 'http://' in content or 'https://' in content:
                                lines = content.split('\n')
                                for line in lines:
                                    if line.startswith('Source:') and ('http://' in line or 'https://' in line):
                                        url = line.replace('Source:', '').strip()
                                        scraped_urls[product]['github'].add(url)
                                        break
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")
                        
        return scraped_urls
        
    def _extract_url_from_filename(self, filename: str) -> str:
        """Extract the original URL from a filename (if possible)."""
        # Try to reverse-engineer the URL from the filename
        # This is an approximation, as the exact logic depends on how the files were named
        base_name = os.path.basename(filename).split('.')[0]
        
        if 'github.com' in base_name:
            # GitHub repository URL
            parts = base_name.split('github.com_')
            if len(parts) > 1:
                return f"https://github.com/{parts[1].replace('_', '/')}"
                
        elif 'docs' in base_name or 'documentation' in base_name:
            # Documentation URL
            for product in PRODUCTS:
                if product in base_name.lower():
                    return f"https://cloud.google.com/{product}/docs"
                    
        return None
        
    def generate_report(self) -> Dict:
        """Generate a report of URLs scraped and yet to be scraped."""
        # Load target URLs for each product and content type
        target_urls = self._load_target_urls()
        
        # Scan scraped content for each product and content type
        scraped_urls = self._scan_scraped_content()
        
        # Process results
        for product in PRODUCTS:
            for content_type in CONTENT_TYPES:
                target_set = set(target_urls[product][content_type])
                scraped_set = scraped_urls[product][content_type]
                
                # Find URLs that are yet to be scraped
                to_scrape = target_set - scraped_set
                
                # Update the results
                self.results[product][content_type]['urls_to_scrape'] = list(to_scrape)
                self.results[product][content_type]['urls_scraped'] = list(scraped_set)
                self.results[product][content_type]['last_updated'] = datetime.now().isoformat()
                self.results[product][content_type]['total_urls'] = len(target_set)
                self.results[product][content_type]['scraped_count'] = len(scraped_set)
                self.results[product][content_type]['pending_count'] = len(to_scrape)
                
        return self.results
        
    def save_report(self, output_file: str = None):
        """Save the report to a JSON file."""
        if output_file is None:
            output_file = os.path.join(self.data_dir, 'url_tracking_report.json')
            
        with open(output_file, 'w') as f:
            json.dump(self.results, f, indent=2)
            
        print(f"Report saved to {output_file}")
        
    def generate_markdown_report(self, output_file: str = None):
        """Generate a markdown report of URLs scraped and yet to be scraped."""
        if output_file is None:
            output_file = os.path.join(self.data_dir, 'url_tracking_report.md')
            
        with open(output_file, 'w') as f:
            f.write("# URL Tracking Report\n\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            for product in PRODUCTS:
                f.write(f"## {product.upper()}\n\n")
                
                for content_type in CONTENT_TYPES:
                    result = self.results[product][content_type]
                    f.write(f"### {content_type.upper()}\n\n")
                    
                    # Write summary
                    f.write(f"**Summary**:\n")
                    f.write(f"- Total URLs: {result['total_urls']}\n")
                    f.write(f"- Scraped: {result['scraped_count']} ({result['scraped_count']/max(1, result['total_urls'])*100:.1f}%)\n")
                    f.write(f"- Pending: {result['pending_count']} ({result['pending_count']/max(1, result['total_urls'])*100:.1f}%)\n")
                    f.write(f"- Last Updated: {result['last_updated']}\n\n")
                    
                    # Write URLs yet to be scraped
                    if result['urls_to_scrape']:
                        f.write("**URLs to Scrape**:\n")
                        for url in sorted(result['urls_to_scrape']):
                            f.write(f"- {url}\n")
                        f.write("\n")
                    else:
                        f.write("**All URLs have been scraped**\n\n")
                        
                    # Write scraped URLs
                    if result['urls_scraped']:
                        f.write("**Scraped URLs**:\n")
                        for url in sorted(result['urls_scraped']):
                            f.write(f"- {url}\n")
                        f.write("\n")
                    else:
                        f.write("**No URLs have been scraped yet**\n\n")
                        
        print(f"Markdown report saved to {output_file}")
        
    def print_summary(self):
        """Print a summary of the URL tracking results."""
        print("\n=== URL Tracking Summary ===\n")
        
        # Create a DataFrame for a nicer display
        data = []
        
        for product in PRODUCTS:
            for content_type in CONTENT_TYPES:
                result = self.results[product][content_type]
                data.append({
                    'Product': product.upper(),
                    'Type': content_type.upper(),
                    'Total': result['total_urls'],
                    'Scraped': result['scraped_count'],
                    'Pending': result['pending_count'],
                    'Progress': f"{result['scraped_count']/max(1, result['total_urls'])*100:.1f}%"
                })
                
        df = pd.DataFrame(data)
        print(df.to_string(index=False))
        
        # Calculate totals
        total_urls = sum(data_row['Total'] for data_row in data)
        scraped_urls = sum(data_row['Scraped'] for data_row in data)
        pending_urls = sum(data_row['Pending'] for data_row in data)
        
        print("\nOverall Progress:")
        print(f"- Total URLs: {total_urls}")
        print(f"- Scraped: {scraped_urls} ({scraped_urls/max(1, total_urls)*100:.1f}%)")
        print(f"- Pending: {pending_urls} ({pending_urls/max(1, total_urls)*100:.1f}%)")

def main():
    """Main function to run the URL tracker."""
    parser = argparse.ArgumentParser(description='Track URLs that have been scraped and identify URLs yet to be scraped.')
    parser.add_argument('--config', help='Path to configuration file')
    parser.add_argument('--output', help='Path to output file')
    parser.add_argument('--markdown', action='store_true', help='Generate markdown report')
    args = parser.parse_args()
    
    tracker = URLTracker(args.config)
    tracker.generate_report()
    
    # Save report in desired format
    if args.markdown:
        tracker.generate_markdown_report(args.output)
    else:
        tracker.save_report(args.output)
        
    # Print summary
    tracker.print_summary()

if __name__ == '__main__':
    main() 