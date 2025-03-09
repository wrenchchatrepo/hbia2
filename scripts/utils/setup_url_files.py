#!/usr/bin/env python3
"""
URL File Setup Utility

This script ensures that URL files are correctly set up for each product and content type.
It creates the necessary directory structure and default URL files where they don't exist.
"""

import os
import json
import yaml
from pathlib import Path
import argparse
from typing import Dict, List

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent.absolute()

# Define the products we're tracking
PRODUCTS = ['bigquery', 'looker', 'dbt', 'gcp', 'omni', 'looker-studio']
CONTENT_TYPES = ['api', 'docs', 'github']

# Default URLs for each product and content type
DEFAULT_URLS = {
    'bigquery': {
        'api': [
            'https://cloud.google.com/bigquery/docs/reference',
            'https://cloud.google.com/bigquery/docs/reference/rest',
            'https://cloud.google.com/bigquery/docs/reference/libraries'
        ],
        'docs': [
            'https://cloud.google.com/bigquery/docs',
            'https://cloud.google.com/bigquery/docs/introduction',
            'https://cloud.google.com/bigquery/docs/quickstarts'
        ],
        'github': [
            'https://github.com/GoogleCloudPlatform/bigquery-utils',
            'https://github.com/GoogleCloudPlatform/professional-services/tree/main/examples/bigquery-cross-project-slot-monitoring',
            'https://github.com/GoogleCloudPlatform/professional-services/tree/main/examples/bigquery-audit-log'
        ]
    },
    'looker': {
        'api': [
            'https://cloud.google.com/looker/docs/reference',
            'https://cloud.google.com/looker/docs/reference/looker-api',
            'https://cloud.google.com/looker/docs/reference/param-reference'
        ],
        'docs': [
            'https://cloud.google.com/looker/docs',
            'https://cloud.google.com/looker/docs/intro',
            'https://cloud.google.com/looker/docs/getting-started'
        ],
        'github': [
            'https://github.com/looker-open-source/actions',
            'https://github.com/looker-open-source/components',
            'https://github.com/looker-open-source/sdk-codegen'
        ]
    },
    'dbt': {
        'api': [
            'https://docs.getdbt.com/reference/dbt-jinja-functions',
            'https://docs.getdbt.com/reference/commands'
        ],
        'docs': [
            'https://docs.getdbt.com/',
            'https://docs.getdbt.com/docs/introduction',
            'https://docs.getdbt.com/docs/build/projects'
        ],
        'github': [
            'https://github.com/dbt-labs/dbt-core',
            'https://github.com/dbt-labs/dbt-utils',
            'https://github.com/dbt-labs/dbt-bigquery'
        ]
    },
    'gcp': {
        'api': [
            'https://cloud.google.com/apis',
            'https://cloud.google.com/apis/docs',
            'https://cloud.google.com/api-gateway/docs'
        ],
        'docs': [
            'https://cloud.google.com/docs',
            'https://cloud.google.com/products',
            'https://cloud.google.com/docs/overview'
        ],
        'github': [
            'https://github.com/GoogleCloudPlatform/cloud-foundation-toolkit',
            'https://github.com/GoogleCloudPlatform/professional-services',
            'https://github.com/GoogleCloudPlatform/sample-apps'
        ]
    },
    'omni': {
        'api': [
            'https://cloud.google.com/bigquery/docs/omni-api-reference'
        ],
        'docs': [
            'https://cloud.google.com/bigquery/docs/omni-overview',
            'https://cloud.google.com/bigquery/docs/omni-aws-introduction',
            'https://cloud.google.com/bigquery/docs/omni-azure-introduction'
        ],
        'github': [
            'https://github.com/GoogleCloudPlatform/professional-services/tree/main/examples/bigquery-omni'
        ]
    },
    'looker-studio': {
        'api': [
            'https://developers.google.com/looker-studio/reference',
            'https://developers.google.com/looker-studio/connector/reference'
        ],
        'docs': [
            'https://support.google.com/looker-studio',
            'https://developers.google.com/looker-studio',
            'https://developers.google.com/looker-studio/connector'
        ],
        'github': [
            'https://github.com/googledatastudio/community-connectors',
            'https://github.com/googledatastudio/tooling',
            'https://github.com/googledatastudio/experimental-visualizations'
        ]
    }
}

class URLFileSetup:
    def __init__(self, config_path: str = None):
        """Initialize the URL file setup with the given configuration."""
        self.config_path = config_path or os.path.join(PROJECT_ROOT, 'data', 'url_config.yml')
        self.config = self._load_config()
        self.data_dir = os.path.join(PROJECT_ROOT, 'data')
        
    def _load_config(self) -> Dict:
        """Load configuration from YAML file."""
        try:
            if not os.path.exists(self.config_path):
                # Create default config
                default_config = {
                    'github_repos': {'batch_size': 5},
                    'documentation_sites': {'batch_size': 3},
                    'output': {'reference_dir': 'references', 'content_dir': 'content', 'text_dir': 'text'}
                }
                
                # Ensure directory exists
                os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
                
                # Save default config
                with open(self.config_path, 'w') as f:
                    yaml.dump(default_config, f, default_flow_style=False)
                
                return default_config
            
            with open(self.config_path, 'r') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"Error loading config: {e}")
            return {
                'github_repos': {'batch_size': 5},
                'documentation_sites': {'batch_size': 3},
                'output': {'reference_dir': 'references', 'content_dir': 'content', 'text_dir': 'text'}
            }
            
    def _ensure_directory_exists(self, directory: str):
        """Ensure that the given directory exists."""
        os.makedirs(directory, exist_ok=True)
        
    def setup_url_files(self, overwrite: bool = False):
        """Set up URL files for each product and content type."""
        # Ensure data directory exists
        self._ensure_directory_exists(self.data_dir)
        
        for product in PRODUCTS:
            product_dir = os.path.join(self.data_dir, product)
            self._ensure_directory_exists(product_dir)
            
            for content_type in CONTENT_TYPES:
                # Ensure content type directory exists
                content_dir = os.path.join(product_dir, content_type)
                self._ensure_directory_exists(content_dir)
                
                # Ensure scraped directory exists
                scraped_dir = os.path.join(content_dir, 'scraped')
                self._ensure_directory_exists(scraped_dir)
                
                # Ensure processed directory exists
                processed_dir = os.path.join(content_dir, 'processed')
                self._ensure_directory_exists(processed_dir)
                
                # Set up URL file
                url_file = os.path.join(content_dir, 'urls.txt')
                if not os.path.exists(url_file) or overwrite:
                    # Get default URLs for this product and content type
                    default_urls = DEFAULT_URLS.get(product, {}).get(content_type, [])
                    
                    # Write URLs to file
                    with open(url_file, 'w') as f:
                        f.write('# URLs for {0} {1}\n'.format(product, content_type))
                        f.write('# Add one URL per line. Lines starting with # are comments.\n\n')
                        for url in default_urls:
                            f.write(f"{url}\n")
                    
                    print(f"Created URL file: {url_file}")
                    
    def generate_url_report(self, output_file: str = None):
        """Generate a report of all URL files."""
        if output_file is None:
            output_file = os.path.join(self.data_dir, 'url_file_report.md')
        
        # Collect information about URL files
        url_files = {}
        for product in PRODUCTS:
            url_files[product] = {}
            for content_type in CONTENT_TYPES:
                url_file = os.path.join(self.data_dir, product, content_type, 'urls.txt')
                if os.path.exists(url_file):
                    with open(url_file, 'r') as f:
                        lines = f.readlines()
                        # Count non-comment, non-empty lines
                        urls = [line.strip() for line in lines if line.strip() and not line.strip().startswith('#')]
                        url_files[product][content_type] = urls
                else:
                    url_files[product][content_type] = []
        
        # Generate report
        with open(output_file, 'w') as f:
            f.write("# URL File Report\n\n")
            
            for product in PRODUCTS:
                f.write(f"## {product.upper()}\n\n")
                
                for content_type in CONTENT_TYPES:
                    urls = url_files[product][content_type]
                    f.write(f"### {content_type.upper()}\n\n")
                    f.write(f"URL file: `data/{product}/{content_type}/urls.txt`\n\n")
                    f.write(f"Total URLs: {len(urls)}\n\n")
                    
                    if urls:
                        f.write("URLs:\n")
                        for url in urls:
                            f.write(f"- {url}\n")
                        f.write("\n")
                    else:
                        f.write("No URLs found in this file.\n\n")
        
        print(f"URL file report saved to {output_file}")

def main():
    """Main function to run the URL file setup."""
    parser = argparse.ArgumentParser(description='Set up URL files for each product and content type.')
    parser.add_argument('--config', help='Path to configuration file')
    parser.add_argument('--overwrite', action='store_true', help='Overwrite existing URL files')
    parser.add_argument('--report', action='store_true', help='Generate a report of URL files')
    parser.add_argument('--output', help='Path to output report file')
    args = parser.parse_args()
    
    setup = URLFileSetup(args.config)
    
    # Set up URL files
    setup.setup_url_files(args.overwrite)
    
    # Generate report if requested
    if args.report:
        setup.generate_url_report(args.output)

if __name__ == '__main__':
    main() 