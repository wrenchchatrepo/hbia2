#!/usr/bin/env python3
import os
import json
from pathlib import Path
import time
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from tqdm import tqdm
import asyncio
from pyppeteer import connect

class LookerApiMapper:
    def __init__(self, base_url, output_dir, mcp_url):
        self.base_url = base_url
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.mcp_url = mcp_url
        self.api_docs = {}

    async def setup_browser(self):
        self.browser = await connect(browserWSEndpoint=self.mcp_url)
        self.page = await self.browser.newPage()

    async def get_page_content(self):
        print("Fetching content from {}".format(self.base_url))
        await self.page.goto(self.base_url, {'waitUntil': 'networkidle2'})
        content = await self.page.content()
        debug_file = self.output_dir / 'debug_output.html'
        with open(str(debug_file), 'w', encoding='utf-8') as f:
            f.write(content)
        print("Saved debug HTML to {}".format(debug_file))
        return content

    async def close_browser(self):
        await self.browser.close()

    def wait_for_devsite_content(self):
        """Wait for the devsite-content to be fully loaded."""
        try:
            # Wait for devsite-content to be present
            devsite_content = self.wait.until(
                EC.presence_of_element_located((By.TAG_NAME, 'devsite-content'))
            )
            print("Found devsite-content")
            
            # Wait for expandable elements to be present
            self.wait.until(
                EC.presence_of_element_located((By.TAG_NAME, 'devsite-expandable'))
            )
            print("Found expandable elements")
            
            return True
        except TimeoutException as e:
            print("Timeout waiting for content: {}".format(str(e)))
            return False

    def expand_section(self, expandable):
        """Expand a section if it's not already expanded."""
        try:
            # Find the control element
            control = expandable.find_element(By.CSS_SELECTOR, '.exw-control')
            if control:
                # Check if it's already expanded
                if control.get_attribute('aria-expanded') != 'true':
                    # Click to expand
                    control.click()
                    # Wait a bit for the content to load
                    time.sleep(0.5)
                return True
        except Exception as e:
            print("Error expanding section: {}".format(str(e)))
            return False

    def extract_methods(self, content):
        """Extract API methods from HTML content."""
        methods = []
        print("Extracting API methods...")
        
        try:
            # Get all expandable elements
            expandables = self.driver.find_elements(By.TAG_NAME, 'devsite-expandable')
            print("Found {} expandable elements".format(len(expandables)))
            
            for expandable in expandables:
                try:
                    # Expand the section
                    if not self.expand_section(expandable):
                        continue
                    
                    # Get the category name (in the showalways div)
                    category_elem = expandable.find_element(By.CSS_SELECTOR, '.showalways')
                    if not category_elem:
                        continue
                    
                    category_name = category_elem.text.strip()
                    if not category_name:
                        continue
                    
                    print("Processing category: {}".format(category_name))
                    
                    # Create category entry
                    category_dict = {
                        'category': category_name,
                        'methods': []
                    }
                    
                    # Get all method links in this category
                    method_links = expandable.find_elements(By.TAG_NAME, 'li')
                    for li in method_links:
                        try:
                            link = li.find_element(By.TAG_NAME, 'a')
                            method_name = link.text.strip()
                            method_url = link.get_attribute('href')
                            
                            if method_name and method_url:
                                category_dict['methods'].append({
                                    'name': method_name,
                                    'url': method_url
                                })
                        except:
                            continue
                    
                    if category_dict['methods']:
                        print("Found {} methods in {}".format(len(category_dict['methods']), category_name))
                        methods.append(category_dict)
                    
                except Exception as e:
                    print("Error processing expandable element: {}".format(str(e)))
                    continue
            
        except Exception as e:
            print("Error finding expandable elements: {}".format(str(e)))
        
        return methods

    def extract_types(self, content):
        """Extract type definitions from HTML content."""
        return []

    def scrape_method_page(self, url):
        """Scrape the documentation content from a method's page."""
        try:
            print("\nScraping {}".format(url))
            self.driver.get(url)
            time.sleep(2)  # Give the page time to load
            
            # Wait for the main content
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'devsite-content')))
            
            # Wait for method content to load
            try:
                self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'devsite-content article')))
                time.sleep(1)  # Additional wait for dynamic content
            except:
                print("Warning: Method content section not found")
            
            # Extract method details
            doc = {
                'url': url,
                'http_method': None,
                'endpoint': None,
                'description': None,
                'parameters': [],
                'response': None,
                'examples': [],
                'notes': []
            }
            
            try:
                # Get HTTP method and endpoint
                method_header = self.driver.find_element(By.CSS_SELECTOR, 'h1.devsite-page-title')
                if method_header:
                    header_text = method_header.text.strip()
                    parts = header_text.split(' ', 1)
                    if len(parts) == 2:
                        doc['http_method'] = parts[0].strip()
                        doc['endpoint'] = parts[1].strip()
                    print("Found method: {}".format(header_text))
            except Exception as e:
                print("Error getting HTTP method: {}".format(str(e)))
            
            try:
                # Get description
                desc_elems = self.driver.find_elements(By.CSS_SELECTOR, 'devsite-content article > p')
                if desc_elems:
                    # Get all paragraphs until we hit a heading
                    description = []
                    for elem in desc_elems:
                        if elem.find_elements(By.XPATH, "./preceding-sibling::h2"):
                            break
                        description.append(elem.text.strip())
                    doc['description'] = '\n\n'.join(filter(None, description))
                    if doc['description']:
                        print("Found description")
            except Exception as e:
                print("Error getting description: {}".format(str(e)))
            
            try:
                # Get parameters
                param_sections = self.driver.find_elements(By.CSS_SELECTOR, 'devsite-content article table')
                for table in param_sections:
                    try:
                        # Check if this is a parameters table by looking at the previous h2
                        header = table.find_element(By.XPATH, "./preceding::h2[1]")
                        if not header or 'Parameters' not in header.text:
                            continue
                        
                        rows = table.find_elements(By.TAG_NAME, 'tr')
                        for row in rows[1:]:  # Skip header row
                            cols = row.find_elements(By.TAG_NAME, 'td')
                            if len(cols) >= 3:
                                param = {
                                    'name': cols[0].text.strip(),
                                    'type': cols[1].text.strip(),
                                    'description': cols[2].text.strip(),
                                    'required': 'required' in cols[2].text.lower()
                                }
                                doc['parameters'].append(param)
                        print("Found {} parameters".format(len(doc['parameters'])))
                        break
                    except Exception as e:
                        print("Error processing parameter section: {}".format(str(e)))
            except Exception as e:
                print("Error getting parameters: {}".format(str(e)))
            
            try:
                # Get response structure
                response_sections = self.driver.find_elements(By.CSS_SELECTOR, 'devsite-content article table')
                for table in response_sections:
                    try:
                        # Check if this is a response table by looking at the previous h2
                        header = table.find_element(By.XPATH, "./preceding::h2[1]")
                        if not header or 'Response' not in header.text:
                            continue
                        
                        # Get the entire response section
                        response_section = header.find_element(By.XPATH, "following-sibling::*[1]")
                        doc['response'] = response_section.text.strip()
                        print("Found response structure")
                        break
                    except:
                        continue
            except Exception as e:
                print("Error getting response: {}".format(str(e)))
            
            try:
                # Get examples
                example_sections = self.driver.find_elements(By.CSS_SELECTOR, 'devsite-code')
                for section in example_sections:
                    example = {
                        'title': None,
                        'code': None,
                        'language': None
                    }
                    
                    try:
                        # Get example title from previous h3 or h4
                        title_elem = section.find_element(By.XPATH, "./preceding::*[self::h3 or self::h4][1]")
                        if title_elem:
                            example['title'] = title_elem.text.strip()
                    except:
                        pass
                    
                    try:
                        # Get code and language
                        pre_elem = section.find_element(By.CSS_SELECTOR, 'pre')
                        example['code'] = pre_elem.text.strip()
                        example['language'] = section.get_attribute('language') or section.get_attribute('data-lang')
                    except:
                        pass
                    
                    if example['code']:
                        doc['examples'].append(example)
                print("Found {} examples".format(len(doc['examples'])))
            except Exception as e:
                print("Error getting examples: {}".format(str(e)))
            
            try:
                # Get notes and warnings
                note_sections = self.driver.find_elements(By.CSS_SELECTOR, 'devsite-content article aside')
                for section in note_sections:
                    note_type = 'note'
                    class_attr = section.get_attribute('class') or ''
                    
                    if 'warning' in class_attr:
                        note_type = 'warning'
                    elif 'caution' in class_attr:
                        note_type = 'caution'
                    elif 'special' in class_attr:
                        note_type = 'special'
                    
                    doc['notes'].append({
                        'type': note_type,
                        'text': section.text.strip()
                    })
                if doc['notes']:
                    print("Found {} notes/warnings".format(len(doc['notes'])))
            except Exception as e:
                print("Error getting notes: {}".format(str(e)))
            
            return doc
            
        except Exception as e:
            print("Error scraping method page {}: {}".format(url, str(e)))
            return None

    def scrape_api_docs(self, structure, limit_percent=None):
        """Scrape documentation for all API methods."""
        print("\nScraping API documentation...")
        
        # Create a flat list of all methods to scrape
        methods_to_scrape = []
        for category in structure['sections']['methods']:
            for method in category['methods']:
                methods_to_scrape.append((category['category'], method))
        
        # Calculate limit if specified
        total_methods = len(methods_to_scrape)
        limit = total_methods
        if limit_percent:
            limit = int(total_methods * limit_percent / 100)
            print("\nProcessing {}% of methods ({}/{})".format(limit_percent, limit, total_methods))
        
        # Setup progress bar
        pbar = tqdm(total=limit, desc="Scraping methods")
        
        # Scrape each method
        for idx, (category_name, method) in enumerate(methods_to_scrape):
            if idx >= limit:
                break
                
            try:
                # Add some delay between requests
                time.sleep(1)
                
                # Scrape the method page
                doc = self.scrape_method_page(method['url'])
                if doc:
                    # Store the documentation
                    if category_name not in self.api_docs:
                        self.api_docs[category_name] = {}
                    self.api_docs[category_name][method['name']] = doc
                
            except Exception as e:
                print("\nError scraping {}: {}".format(method['name'], str(e)))
            finally:
                pbar.update(1)
        
        pbar.close()
        
        # Save the documentation with progress indicator
        docs_file = self.output_dir / 'looker_api_docs_{}.json'.format(limit_percent if limit_percent else 100)
        with open(str(docs_file), 'w') as f:
            json.dump(self.api_docs, f, indent=2)
        print("\nAPI documentation has been saved to {}".format(docs_file))
        
        return docs_file

    def verify_docs(self, file_path):
        """Verify the scraped documentation."""
        print("\nVerifying documentation from {}".format(file_path))
        
        with open(str(file_path)) as f:
            docs = json.load(f)
        
        # Collect statistics
        stats = {
            'total_categories': len(docs),
            'total_methods': 0,
            'methods_with_content': 0,
            'methods_with_description': 0,
            'methods_with_parameters': 0,
            'methods_with_response': 0,
            'methods_with_examples': 0,
            'methods_with_notes': 0
        }
        
        # Sample of methods with missing content
        missing_content = []
        
        # Analyze each category and method
        for category, methods in docs.items():
            stats['total_methods'] += len(methods)
            
            for method_name, method_doc in methods.items():
                has_content = False
                
                if method_doc.get('description'):
                    stats['methods_with_description'] += 1
                    has_content = True
                
                if method_doc.get('parameters'):
                    stats['methods_with_parameters'] += 1
                    has_content = True
                
                if method_doc.get('response'):
                    stats['methods_with_response'] += 1
                    has_content = True
                
                if method_doc.get('examples'):
                    stats['methods_with_examples'] += 1
                    has_content = True
                
                if method_doc.get('notes'):
                    stats['methods_with_notes'] += 1
                    has_content = True
                
                if has_content:
                    stats['methods_with_content'] += 1
                else:
                    missing_content.append("{}/{}".format(category, method_name))
                    if len(missing_content) <= 5:  # Only show first 5 examples
                        print("No content found for: {}/{}".format(category, method_name))
        
        # Print statistics
        print("\nDocumentation Statistics:")
        print("Categories: {}".format(stats['total_categories']))
        print("Total Methods: {}".format(stats['total_methods']))
        print("Methods with any content: {} ({:.1f}%)".format(
            stats['methods_with_content'],
            stats['methods_with_content']/stats['total_methods']*100
        ))
        print("Methods with description: {} ({:.1f}%)".format(
            stats['methods_with_description'],
            stats['methods_with_description']/stats['total_methods']*100
        ))
        print("Methods with parameters: {} ({:.1f}%)".format(
            stats['methods_with_parameters'],
            stats['methods_with_parameters']/stats['total_methods']*100
        ))
        print("Methods with response: {} ({:.1f}%)".format(
            stats['methods_with_response'],
            stats['methods_with_response']/stats['total_methods']*100
        ))
        print("Methods with examples: {} ({:.1f}%)".format(
            stats['methods_with_examples'],
            stats['methods_with_examples']/stats['total_methods']*100
        ))
        print("Methods with notes: {} ({:.1f}%)".format(
            stats['methods_with_notes'],
            stats['methods_with_notes']/stats['total_methods']*100
        ))
        
        if len(missing_content) > 5:
            print("\nAnd {} more methods with no content".format(len(missing_content) - 5))
        
        return stats

    def map_api_structure(self):
        """Map the API documentation structure."""
        structure = {
            "url": self.base_url,
            "type": "root",
            "version": "4.0.25.2",
            "sections": {
                "methods": [],
                "types": []
            }
        }
        
        try:
            # Get page content
            content = asyncio.get_event_loop().run_until_complete(self.get_page_content())
            if not content:
                raise Exception("Failed to fetch page content")
            
            # Extract API methods and types
            methods = self.extract_methods(content)
            types = self.extract_types(content)
            
            structure["sections"]["methods"] = methods
            structure["sections"]["types"] = types
            
            # Save the structure
            output_file = self.output_dir / 'looker_api_structure.json'
            with open(str(output_file), 'w') as f:
                json.dump(structure, f, indent=2)
            
            print("API structure has been mapped and saved to {}".format(output_file))
            
            # Save markdown version
            self.save_markdown(structure)
            
            # Scrape and verify at different percentages
            for percent in [1, 10, 50, 100]:
                docs_file = self.scrape_api_docs(structure, percent)
                self.verify_docs(docs_file)
                
                if percent < 100:
                    proceed = input("\nContinue to {}%? (y/n): ".format(min(percent * 2, 100)))
                    if proceed.lower() != 'y':
                        break
            
            return structure
            
        except Exception as e:
            print("Error mapping API structure: {}".format(str(e)))
            raise
        finally:
            asyncio.get_event_loop().run_until_complete(self.close_browser())

    def save_markdown(self, structure):
        """Save the API structure in markdown format."""
        md_file = self.output_dir / 'looker_api_structure.md'
        with open(str(md_file), 'w') as f:
            f.write('# Looker API Structure\n\n')
            f.write('Version: {}\n\n'.format(structure["version"]))
            
            f.write('## API Methods\n\n')
            for method_category in structure["sections"]["methods"]:
                f.write('### {}\n\n'.format(method_category["category"]))
                for method in method_category["methods"]:
                    f.write('- [{}]({})\n'.format(method["name"], method["url"]))
                f.write('\n')
            
            f.write('## Type Definitions\n\n')
            for type_category in structure["sections"]["types"]:
                f.write('### {}\n\n'.format(type_category["category"]))
                for type_def in type_category["types"]:
                    f.write('- [{}]({})\n'.format(type_def["name"], type_def["url"]))
                f.write('\n')

def main():
    # Configuration
    base_url = "https://cloud.google.com/looker/docs/reference/looker-api/latest"
    output_dir = "../scraped_content/looker_api_reference"
    mcp_url = "ws://localhost:3000"
    
    # Create and run mapper
    mapper = LookerApiMapper(base_url, output_dir, mcp_url)
    mapper.map_api_structure()

if __name__ == "__main__":
    main() 