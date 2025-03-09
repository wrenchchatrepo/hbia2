#!/usr/bin/env python3
import json
from pathlib import Path
from typing import Dict, Optional
from datetime import datetime

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent.absolute()

class URLAnnotator:
    def __init__(self, urls_file: str):
        self.urls_file = Path(urls_file)
        self.status_file = self.urls_file.with_suffix('.md.status.json')
        self.annotated_file = self.urls_file.with_suffix('.md.annotated.md')
        self.statuses = self._load_statuses()
        
    def _load_statuses(self) -> Dict[str, Dict]:
        """Load existing statuses from JSON file."""
        try:
            with open(self.status_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
            
    def _save_statuses(self):
        """Save current statuses to JSON file."""
        with open(self.status_file, 'w') as f:
            json.dump(self.statuses, f, indent=2)
            
    def _get_key(self, url: str) -> str:
        """Generate a unique key for a URL."""
        return url.strip()
        
    def update_status(self, url: str, status: str, details: Optional[Dict] = None):
        """Update the status of a URL."""
        key = self._get_key(url)
        self.statuses[key] = {
            'status': status,
            'details': details or {},
            'updated_at': str(datetime.now())
        }
        self._save_statuses()
        
    def _get_status_badge(self, status: str) -> str:
        """Generate a markdown badge for a status."""
        colors = {
            'pending': 'grey',
            'mapped': 'blue',
            'scraped': 'green',
            'crawled': 'green',
            'converted': 'green',
            'skipped': 'yellow',
            'error': 'red'
        }
        color = colors.get(status, 'grey')
        return f'![{status}](https://img.shields.io/badge/status-{status}-{color})'
        
    def _format_details(self, details: Dict) -> str:
        """Format details into markdown comments."""
        if not details:
            return ''
            
        formatted = []
        for key, value in details.items():
            if isinstance(value, dict):
                value = json.dumps(value)
            formatted.append(f'{key}:{value}')
            
        return '|'.join(formatted)
        
    def annotate_markdown(self):
        """Generate an annotated version of the markdown file."""
        try:
            # Read original file
            with open(self.urls_file, 'r') as f:
                lines = f.readlines()
                
            # Process each line
            annotated_lines = []
            for line in lines:
                line = line.strip()
                if not line or line.startswith('#'):
                    annotated_lines.append(line)
                    continue
                    
                key = self._get_key(line)
                status_info = self.statuses.get(key, {'status': 'pending', 'details': {}})
                
                # Add status badge and details
                annotated_line = f"{line} <!-- status:{status_info['status']} -->"
                if status_info['details']:
                    annotated_line += f" <!-- details:{self._format_details(status_info['details'])} -->"
                    
                annotated_lines.append(annotated_line)
                
            # Write annotated file
            with open(self.annotated_file, 'w') as f:
                f.write('\n'.join(annotated_lines))
                
        except Exception as e:
            print(f"Error annotating markdown: {str(e)}")

def main():
    annotator = URLAnnotator('urls_data_store.md')
    annotator.annotate_markdown()
    print(f"Created annotated version: urls_data_store.md.annotated.md")

if __name__ == '__main__':
    main() 