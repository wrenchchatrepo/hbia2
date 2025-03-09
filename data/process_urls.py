#!/usr/bin/env python3
import yaml
import json
import os
import time
from pathlib import Path
from typing import List, Dict
import requests
from datetime import datetime
import logging
from annotate_urls import URLAnnotator
from dotenv import load_dotenv
from tqdm import tqdm
from tenacity import retry, stop_after_attempt, wait_exponential

# Load environment variables
load_dotenv()

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent.absolute()

class URLProcessor:
    def __init__(self, config_path: str):
        self.config = self._load_config(config_path)
        self._setup_logging()
        self._create_directories()
        self.annotator = URLAnnotator(str(SCRIPT_DIR / 'urls_data_store.md'))
        self.api_key = self._load_api_key()
        if not self.api_key:
            raise ValueError("API key not found in credentials")
        self.api_base = "https://api.firecrawl.dev/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        self.summary = {
            'total_urls': 0,
            'github_repos': {'success': 0, 'failed': 0, 'skipped': 0},
            'doc_sites': {'success': 0, 'failed': 0, 'skipped': 0},
            'files_processed': 0,
            'errors': []
        }
        
    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from YAML file."""
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
            
    def _setup_logging(self):
        """Setup logging configuration."""
        log_file = SCRIPT_DIR / self.config['output']['log_file']
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        
    def _create_directories(self):
        """Create necessary output directories."""
        for dir_path in [
            SCRIPT_DIR / self.config['output']['reference_dir'],
            SCRIPT_DIR / self.config['output']['content_dir'],
            SCRIPT_DIR / self.config['output']['text_dir']
        ]:
            Path(dir_path).mkdir(parents=True, exist_ok=True)
            
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    def _make_request(self, method: str, endpoint: str, data: Dict = None) -> Dict:
        """Make a request to the Firecrawl API with retry logic."""
        url = f"{self.api_base}/{endpoint}"
        try:
            response = requests.request(method, url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"API request failed: {str(e)}")
            raise
            
    def _review_github_files(self, files: List[str]) -> List[str]:
        """Review GitHub files and filter out low-value files."""
        valuable_files = []
        skipped_files = []
        
        for file in files:
            # Skip binary files
            if any(file.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.ico', '.pdf', '.zip', '.tar', '.gz']):
                skipped_files.append((file, 'binary_file'))
                continue
                
            # Skip generated files
            if any(pattern in file.lower() for pattern in ['node_modules', 'dist', 'build', '.git', 'coverage', 'tmp']):
                skipped_files.append((file, 'generated_file'))
                continue
                
            # Skip test files unless they're documentation
            if 'test' in file.lower() and not any(doc in file.lower() for doc in ['readme', 'docs', 'documentation']):
                skipped_files.append((file, 'test_file'))
                continue
                
            # Skip configuration files unless they're documentation
            if any(file.lower().endswith(ext) for ext in ['.json', '.yaml', '.yml', '.toml', '.ini', '.conf']) and not any(doc in file.lower() for doc in ['readme', 'docs', 'documentation']):
                skipped_files.append((file, 'config_file'))
                continue
                
            valuable_files.append(file)
            
        return valuable_files, skipped_files
        
    def process_github_repos(self, urls: List[str]):
        """Process GitHub repositories using map and scrape APIs."""
        batch_size = self.config['github_repos']['batch_size']
        self.summary['total_urls'] += len(urls)
        
        for i in tqdm(range(0, len(urls), batch_size), desc="Processing GitHub Repos"):
            batch = urls[i:i + batch_size]
            
            for url in batch:
                try:
                    # Map the repository
                    reference_file = self._map_repository(url)
                    if not reference_file:
                        self.annotator.update_status(url, 'error', {'error': 'Mapping failed'})
                        self.summary['github_repos']['failed'] += 1
                        continue
                        
                    self.annotator.update_status(url, 'mapped', {'reference_file': reference_file})
                    
                    # Review files before scraping
                    with open(reference_file, 'r') as f:
                        reference_data = json.load(f)
                        valuable_files, skipped_files = self._review_github_files(reference_data.get('files', []))
                        
                    if not valuable_files:
                        self.annotator.update_status(url, 'skipped', {'reason': 'no_valuable_files', 'skipped': len(skipped_files)})
                        self.summary['github_repos']['skipped'] += 1
                        continue
                    
                    # Scrape priority files
                    success = self._scrape_priority_files(url, valuable_files)
                    if success:
                        self.annotator.update_status(url, 'scraped', {
                            'files_scraped': len(success),
                            'files_skipped': len(skipped_files)
                        })
                        self.summary['github_repos']['success'] += 1
                        self.summary['files_processed'] += len(success)
                    else:
                        self.annotator.update_status(url, 'error', {'error': 'Scraping failed'})
                        self.summary['github_repos']['failed'] += 1
                    
                    # Rate limiting
                    time.sleep(2)
                    
                except Exception as e:
                    logging.error(f"Error processing {url}: {str(e)}")
                    self.annotator.update_status(url, 'error', {'error': str(e)})
                    self.summary['github_repos']['failed'] += 1
                    self.summary['errors'].append(f"GitHub {url}: {str(e)}")
                    
    def process_documentation_sites(self, urls: List[str]):
        """Process documentation sites using map and crawl APIs."""
        batch_size = self.config['documentation_sites']['batch_size']
        
        for i in range(0, len(urls), batch_size):
            batch = urls[i:i + batch_size]
            logging.info(f"Processing batch {i//batch_size + 1} of {(len(urls) + batch_size - 1)//batch_size}")
            
            for url in batch:
                try:
                    # Map the documentation site
                    reference_file = self._map_documentation(url)
                    if not reference_file:
                        self.annotator.update_status(url, 'error', {'error': 'Mapping failed'})
                        continue
                        
                    self.annotator.update_status(url, 'mapped', {'reference_file': reference_file})
                    
                    # Crawl the entire site
                    success = self._crawl_documentation(url)
                    if success:
                        self.annotator.update_status(url, 'crawled', {'pages_crawled': len(success)})
                    else:
                        self.annotator.update_status(url, 'error', {'error': 'Crawling failed'})
                    
                    # Rate limiting
                    time.sleep(5)
                    
                except Exception as e:
                    logging.error(f"Error processing {url}: {str(e)}")
                    self.annotator.update_status(url, 'error', {'error': str(e)})
                    
    def _map_repository(self, url: str) -> str:
        """Map a GitHub repository using Firecrawl map API."""
        logging.info(f"Mapping repository: {url}")
        
        try:
            # Call Firecrawl map API
            response = self._make_request('POST', 'map', {
                'url': url,
                'options': {
                    'include_patterns': self.config['github_repos']['priority_files'],
                    'exclude_patterns': self.config['github_repos']['exclude_patterns']
                }
            })
            
            # Save reference file
            reference_file = f"data/references/{url.replace('/', '_')}_map.json"
            with open(reference_file, 'w') as f:
                json.dump(response, f, indent=2)
                
            return reference_file
            
        except Exception as e:
            logging.error(f"Failed to map repository {url}: {str(e)}")
            return None
        
    def _scrape_priority_files(self, url: str, files: List[str]) -> List[str]:
        """Scrape priority files from a repository."""
        logging.info(f"Scraping priority files from: {url}")
        
        try:
            scraped_files = []
            
            for file_url in tqdm(files, desc=f"Scraping {url}", leave=False):
                response = self._make_request('POST', 'scrape', {
                    'url': file_url,
                    'formats': ['markdown']
                })
                
                if response.get('success'):
                    content_file = f"data/content/{file_url.replace('/', '_')}.md"
                    with open(content_file, 'w') as f:
                        f.write(response['data']['markdown'])
                    scraped_files.append(content_file)
                    
            return scraped_files
            
        except Exception as e:
            logging.error(f"Failed to scrape files from {url}: {str(e)}")
            return []
        
    def _map_documentation(self, url: str) -> str:
        """Map a documentation site using Firecrawl map API."""
        logging.info(f"Mapping documentation site: {url}")
        
        try:
            # Call Firecrawl map API
            response = self._make_request('POST', 'map', {
                'url': url,
                'options': {
                    'include_patterns': self.config['documentation_sites']['include_patterns'],
                    'exclude_patterns': self.config['documentation_sites']['exclude_patterns']
                }
            })
            
            # Save reference file
            reference_file = f"data/references/{url.replace('/', '_')}_map.json"
            with open(reference_file, 'w') as f:
                json.dump(response, f, indent=2)
                
            return reference_file
            
        except Exception as e:
            logging.error(f"Failed to map documentation site {url}: {str(e)}")
            return None
        
    def _crawl_documentation(self, url: str) -> List[str]:
        """Crawl a documentation site using Firecrawl crawl API."""
        logging.info(f"Crawling documentation site: {url}")
        
        try:
            # Start crawl job
            response = self._make_request('POST', 'crawl', {
                'url': url,
                'options': {
                    'include_patterns': self.config['documentation_sites']['include_patterns'],
                    'exclude_patterns': self.config['documentation_sites']['exclude_patterns'],
                    'formats': ['markdown']
                }
            })
            
            if not response.get('success'):
                return []
                
            crawl_id = response['id']
            crawled_files = []
            
            # Poll for results
            while True:
                status_response = self._make_request('GET', f'crawl/{crawl_id}')
                
                if status_response['status'] == 'completed':
                    # Save all crawled content
                    for page in status_response.get('data', []):
                        content_file = f"data/content/{page['metadata']['sourceURL'].replace('/', '_')}.md"
                        with open(content_file, 'w') as f:
                            f.write(page['markdown'])
                        crawled_files.append(content_file)
                    break
                    
                elif status_response['status'] == 'error':
                    logging.error(f"Crawl failed for {url}: {status_response.get('error')}")
                    break
                    
                time.sleep(30)  # Wait before polling again
                
            return crawled_files
            
        except Exception as e:
            logging.error(f"Failed to crawl documentation site {url}: {str(e)}")
            return []
        
    def convert_to_text(self):
        """Convert markdown content to plain text."""
        logging.info("Converting markdown to text")
        
        try:
            import markdown
            from bs4 import BeautifulSoup
            
            # Process all markdown files
            for md_file in Path(self.config['output']['content_dir']).glob('*.md'):
                try:
                    # Read markdown
                    with open(md_file, 'r') as f:
                        md_content = f.read()
                        
                    # Convert to HTML
                    html = markdown.markdown(md_content)
                    
                    # Extract text
                    soup = BeautifulSoup(html, 'html.parser')
                    text = soup.get_text(separator='\n', strip=True)
                    
                    # Save text file
                    text_file = Path(self.config['output']['text_dir']) / f"{md_file.stem}.txt"
                    with open(text_file, 'w') as f:
                        f.write(text)
                        
                except Exception as e:
                    logging.error(f"Failed to convert {md_file}: {str(e)}")
                    
        except Exception as e:
            logging.error(f"Failed to convert markdown to text: {str(e)}")
        
    def _load_api_key(self) -> str:
        """Load API key from credentials file."""
        try:
            with open(SCRIPT_DIR.parent.parent / '.credentials' / 'hbia2' / 'credentials.yml', 'r') as f:
                credentials = yaml.safe_load(f)
                return credentials.get('firecrawl_api_key')
        except Exception as e:
            logging.error(f"Failed to load API key: {str(e)}")
            return None
        
    def print_summary(self):
        """Print a summary of the processing results."""
        print("\nProcessing Summary:")
        print("-" * 50)
        print(f"Total URLs: {self.summary['total_urls']}")
        print("\nGitHub Repositories:")
        print(f"  Success: {self.summary['github_repos']['success']}")
        print(f"  Failed: {self.summary['github_repos']['failed']}")
        print(f"  Skipped: {self.summary['github_repos']['skipped']}")
        print("\nDocumentation Sites:")
        print(f"  Success: {self.summary['doc_sites']['success']}")
        print(f"  Failed: {self.summary['doc_sites']['failed']}")
        print(f"  Skipped: {self.summary['doc_sites']['skipped']}")
        print(f"\nTotal Files Processed: {self.summary['files_processed']}")
        
        if self.summary['errors']:
            print("\nErrors:")
            for error in self.summary['errors']:
                print(f"  - {error}")
                
def main():
    # Load URLs from markdown file
    urls_file = SCRIPT_DIR / 'urls_data_store.md'
    with open(urls_file, 'r') as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith('#') and not line.startswith('<!--')]
        
    # Separate URLs into repos and docs
    github_repos = [url for url in urls if 'github.com' in url]
    doc_sites = [url for url in urls if 'github.com' not in url]
    
    # Initialize processor
    processor = URLProcessor(str(SCRIPT_DIR / 'url_config.yml'))
    
    # Process repositories
    logging.info(f"Processing {len(github_repos)} GitHub repositories")
    processor.process_github_repos(github_repos)
    
    # Process documentation sites
    logging.info(f"Processing {len(doc_sites)} documentation sites")
    processor.process_documentation_sites(doc_sites)
    
    # Convert to text
    processor.convert_to_text()
    
    # Update annotations
    processor.annotator.annotate_markdown()
    
    # Print summary
    processor.print_summary()
    
    logging.info("Processing complete!")

if __name__ == '__main__':
    main() 