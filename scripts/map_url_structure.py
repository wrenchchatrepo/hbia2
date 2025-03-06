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
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.exceptions import Timeout, RequestException
import subprocess

class URLMapper:
    def __init__(self, base_url, max_depth=3):
        """Initialize the URL mapper with a base URL and maximum depth."""
        self.base_url = base_url
        self.max_depth = max_depth
        self.visited_urls = set()
        self.url_structure = {}
        self.start_time = time.time()
        self.processed_urls = set()
        self.failed_urls = set()
        
        # Initialize session with retry strategy
        self.session = requests.Session()
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        
        # Initialize URL structure
        self.url_structure = {
            'url': base_url,
            'depth': 0,
            'children': []
        }
        
    def is_valid_url(self, url):
        """Check if URL is valid and belongs to the same domain."""
        try:
            parsed = urlparse(url)
            base_parsed = urlparse(self.base_url)
            
            # Check if URL belongs to the same domain
            if parsed.netloc != base_parsed.netloc:
                return False
                
            # Exclude URLs with query parameters
            if parsed.query:
                return False
                
            # Exclude URLs with specific file extensions
            if re.search(r'\.(jpg|jpeg|png|gif|pdf|zip|tar|gz)$', url.lower()):
                return False
                
            # Exclude URLs with specific patterns
            if any(pattern in url.lower() for pattern in ['/api/', '/auth/', '/login/', '/logout/']):
                return False
                
            return True
        except:
            return False
            
    def get_nav_links(self, url):
        """Extract links from the left-hand navigation menu using Puppeteer."""
        nav_links = []
        
        try:
            # Create a temporary JavaScript file for Puppeteer
            script_content = f"""
            const puppeteer = require('puppeteer');
            
            async function scrapeNav() {{
                const browser = await puppeteer.launch({{ headless: true }});
                const page = await browser.newPage();
                
                try {{
                    // Set viewport to ensure all content is visible
                    await page.setViewport({{ width: 1280, height: 800 }});
                    
                    // Set a timeout for navigation
                    await page.setDefaultNavigationTimeout(30000);
                    
                    // Navigate to the page
                    await page.goto('{url}', {{ waitUntil: 'networkidle0' }});
                    
                    // Wait for the navigation menu to load
                    await page.waitForSelector('.devsite-nav', {{ timeout: 10000 }});
                    
                    // Wait for dynamic content to load
                    await new Promise(resolve => setTimeout(resolve, 5000));
                    
                    // Get all links in the navigation
                    const links = await page.evaluate(() => {{
                        const links = [];
                        
                        // Get all links in the navigation
                        const navLinks = document.querySelectorAll('a[href*="/looker/"]');
                        navLinks.forEach(link => {{
                            if (link.href && !link.href.includes('#')) {{
                                links.push(link.href);
                            }}
                        }});
                        
                        // Remove duplicates
                        return [...new Set(links)];
                    }});
                    
                    console.log(JSON.stringify(links));
                }} catch (error) {{
                    console.error('Error in Puppeteer:', error.message);
                    console.log('[]');
                }} finally {{
                    await browser.close();
                }}
            }}
            
            scrapeNav();
            """
            
            # Write the script to a temporary file
            with open('temp_scrape.js', 'w') as f:
                f.write(script_content)
            
            # Run the script with Node.js
            result = subprocess.run(['node', 'temp_scrape.js'], capture_output=True, text=True, timeout=60)
            
            # Clean up the temporary file
            os.remove('temp_scrape.js')
            
            # Parse the results
            if result.stdout:
                try:
                    links = json.loads(result.stdout)
                    for link in links:
                        if self.is_valid_url(link):
                            nav_links.append(link)
                except json.JSONDecodeError:
                    print(f"Debug: Could not parse JSON output for {url}")
                    
        except subprocess.TimeoutExpired:
            print(f"Debug: Puppeteer script timed out for {url}")
            self.failed_urls.add(url)
        except Exception as e:
            print(f"Debug: Error getting navigation links for {url}: {str(e)}")
            self.failed_urls.add(url)
            
        return nav_links
        
    def map_url_structure(self, url, current_depth=0):
        """Map the URL structure recursively."""
        if current_depth > self.max_depth:
            return
            
        if url in self.processed_urls:
            return
            
        self.processed_urls.add(url)
        print(f"Processing URL: {url} (Depth: {current_depth})")
        
        try:
            # Get navigation links using Puppeteer
            nav_links = self.get_nav_links(url)
            
            # Create node for current URL
            node = {
                'url': url,
                'depth': current_depth,
                'children': []
            }
            
            # Add to structure
            if current_depth == 0:
                self.url_structure['children'].append(node)
            else:
                # Find parent node and add as child
                parent = self.find_parent_node(self.url_structure, url)
                if parent:
                    parent['children'].append(node)
            
            # Process navigation links
            for link in nav_links:
                if link not in self.processed_urls:
                    self.map_url_structure(link, current_depth + 1)
                    
            # Add a small delay between requests
            time.sleep(0.5)
            
        except Exception as e:
            print(f"Error processing URL {url}: {str(e)}")
            self.failed_urls.add(url)
            
    def find_parent_node(self, structure, child_url):
        """Find the parent node for a given URL in the structure."""
        if 'children' in structure:
            for child in structure['children']:
                if child['url'] in child_url:
                    return structure
                result = self.find_parent_node(child, child_url)
                if result:
                    return result
        return None
        
    def save_structure(self, filename='url_structure.json'):
        """Save the URL structure to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.url_structure, f, indent=2)
            
def main():
    # Test with Looker docs
    base_url = "https://cloud.google.com/looker/docs/"
    
    # Create URL mapper
    mapper = URLMapper(base_url, max_depth=3)
    
    print(f"Starting URL mapping for {base_url}")
    print("This may take some time...")
    
    try:
        # Map the URL structure
        mapper.map_url_structure(base_url)
        
        # Save the structure
        mapper.save_structure()
        
        # Print summary
        elapsed_time = time.time() - mapper.start_time
        print("\nURL Structure Summary:")
        print(f"Base URL: {base_url}")
        print(f"Total unique URLs found: {len(mapper.processed_urls)}")
        print(f"Failed URLs: {len(mapper.failed_urls)}")
        print(f"Time taken: {elapsed_time:.2f} seconds")
        print(f"Results saved to url_structure.json")
        
    except KeyboardInterrupt:
        print("\nMapping interrupted by user. Saving current progress...")
        mapper.save_structure()
        print("Progress saved to url_structure.json")
    except Exception as e:
        print(f"\nError during mapping: {str(e)}")
        print("Saving current progress...")
        mapper.save_structure()
        print("Progress saved to url_structure.json")

if __name__ == "__main__":
    main() 