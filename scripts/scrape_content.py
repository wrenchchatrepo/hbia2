#!/usr/bin/env python3
import os
import json
from pathlib import Path
from datetime import datetime
import re
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import time
import html2text
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.exceptions import Timeout, RequestException

class ContentScraper:
    def __init__(self, structure_file, output_dir, timeout=30, test_mode=False):
        self.structure_file = structure_file
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.timeout = timeout
        self.test_mode = test_mode
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

    def load_structure(self):
        """Load URL structure from JSON file."""
        with open(self.structure_file, 'r') as f:
            return json.load(f)

    def clean_filename(self, url):
        """Convert URL to a clean filename."""
        parsed = urlparse(url)
        path = parsed.path.strip('/')
        if not path:
            path = 'index'
        return re.sub(r'[^\w\-_.]', '_', path)

    def extract_content(self, html_content):
        """Extract main content from HTML, removing header and footer."""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove header, footer, and navigation
        for element in soup.find_all(['header', 'footer', 'nav']):
            element.decompose()
        
        # Find main content area - specific to Google Cloud docs
        main_content = None
        
        # Try to find the article body first
        article_body = soup.find('div', class_='devsite-article-body')
        if article_body:
            main_content = article_body
        else:
            # Fall back to other content areas
            for selector in [
                'main.devsite-main-content',
                'article.devsite-article',
                'div.content',
                'div.devsite-content'
            ]:
                main_content = soup.select_one(selector)
                if main_content:
                    break
        
        if not main_content:
            return None
        
        # Remove unwanted elements
        for element in main_content.find_all(['script', 'style', 'iframe', 'noscript', 'div', 'aside']):
            if element.get('class'):
                classes = element.get('class')
                if isinstance(classes, str):
                    classes = [classes]
                if any(cls in classes for cls in [
                    'devsite-sidebar', 'devsite-footer', 'devsite-top-logo-row',
                    'devsite-nav', 'devsite-nav-responsive', 'devsite-article-meta',
                    'devsite-floating-action-buttons', 'devsite-content-data',
                    'devsite-footer-utility', 'nocontent'
                ]):
                    element.decompose()
        
        # Convert to markdown
        markdown = self.h2t.handle(str(main_content))
        
        # Clean up markdown
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)  # Remove excessive newlines
        markdown = re.sub(r'\[([^\]]+)\]\(#\)', r'\1', markdown)  # Remove empty links
        markdown = re.sub(r'\[([^\]]+)\]\(/\)', r'\1', markdown)  # Remove root links
        markdown = re.sub(r'\[([^\]]+)\]\(https://cloud\.google\.com\)', r'\1', markdown)  # Remove cloud.google.com links
        
        return markdown.strip()

    def save_content(self, url, content, depth):
        """Save content to appropriate files."""
        if not content:
            return
        
        # Create filename
        filename = self.clean_filename(url)
        
        # Save markdown
        md_path = self.output_dir / f"{filename}.md"
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(f"# {url}\n\n")
            f.write(f"Depth: {depth}\n\n")
            f.write(content)
        
        # Save text
        txt_path = self.output_dir / f"{filename}.txt"
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(content)

    def scrape_node(self, node, pbar, start_time=None):
        """Scrape content from a single node."""
        if self.test_mode and start_time and (time.time() - start_time) > 60:  # 1 minute limit for tests
            print("\nTest time limit reached. Stopping content scraping.")
            return
        
        url = node['url']
        depth = node['depth']
        
        try:
            # Download the page with timeout
            response = self.session.get(url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            
            # Extract and save content
            content = self.extract_content(response.text)
            if content:
                self.save_content(url, content, depth)
            
            # Update progress bar
            pbar.update(1)
            
            # Process children
            for child in node['children']:
                self.scrape_node(child, pbar, start_time)
            
            time.sleep(self.delay)  # Be nice to the server
            
        except Timeout:
            print(f"\nTimeout processing {url}")
        except RequestException as e:
            print(f"\nNetwork error processing {url}: {str(e)}")
        except Exception as e:
            print(f"\nError processing {url}: {str(e)}")

    def scrape_all_content(self):
        """Scrape content from all URLs in the structure."""
        # Load URL structure
        structure = self.load_structure()
        
        # Count total nodes
        def count_nodes(node):
            return 1 + sum(count_nodes(child) for child in node['children'])
        
        total_nodes = count_nodes(structure)
        
        # Create progress bar
        with tqdm(total=total_nodes, desc="Scraping content", unit="pages") as pbar:
            # Start timing
            start_time = time.time()
            self.scrape_node(structure, pbar, start_time)
            print(f"\nTime taken: {time.time() - start_time:.2f} seconds")

def main():
    # Configuration
    structure_file = "url_structure.json"
    output_dir = "scraped_content"
    test_mode = False  # Set to False for production
    
    # Create scraper and run
    scraper = ContentScraper(structure_file, output_dir, timeout=30, test_mode=test_mode)
    print(f"Scraping content to: {output_dir}")
    print("This may take a while as we're processing all documentation pages...")
    scraper.scrape_all_content()
    print(f"\nContent saved to: {output_dir}")

if __name__ == "__main__":
    main() 