#!/usr/bin/env python3
import os
import json
import re
import shutil
from pathlib import Path
import markdown
from bs4 import BeautifulSoup

# Configuration
API_DOCS_DIR = "looker_api_docs"
MODELS_DIR = os.path.join(API_DOCS_DIR, "models")
OUTPUT_DIR = os.path.join("scraped_content", "looker_api")
PROCESSED_DIR = os.path.join("temp_processed", "looker")

def setup_directories():
    """Create necessary directories."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)

def extract_api_info(file_path):
    """Extract API information from a Markdown file."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract API name
    api_name = os.path.basename(file_path).replace('.md', '')
    
    # Extract methods using regex
    methods = []
    method_blocks = re.findall(r'## (.*?)\n(.*?)(?=## |$)', content, re.DOTALL)
    
    for method_name, method_content in method_blocks:
        method_name = method_name.strip()
        
        # Skip if not a method
        if not method_name or method_name.startswith('#'):
            continue
        
        # Extract endpoint
        endpoint_match = re.search(r'\*\*(GET|POST|PUT|DELETE|PATCH)\*\* (.*?)(?:\n|$)', method_content)
        endpoint = ""
        if endpoint_match:
            http_method = endpoint_match.group(1)
            path = endpoint_match.group(2).strip()
            endpoint = f"{http_method} {path}"
        
        # Extract description
        description = ""
        desc_match = re.search(r'(?:\*\*.*?\*\*.*?\n)(.*?)(?=\n\n|$)', method_content, re.DOTALL)
        if desc_match:
            description = desc_match.group(1).strip()
        
        methods.append({
            "name": method_name,
            "description": description,
            "endpoint": endpoint
        })
    
    return {
        "api_name": api_name,
        "methods": methods
    }

def extract_model_info(file_path):
    """Extract model information from a Markdown file."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract model name
    model_name = os.path.basename(file_path).replace('.md', '')
    
    # Extract properties using regex
    properties = []
    
    # Look for table with properties
    table_match = re.search(r'\| Name \| Type \| Description \|\n\|.*?\|(.*?)(?=\n\n|$)', content, re.DOTALL)
    
    if table_match:
        table_content = table_match.group(1)
        rows = re.findall(r'\| (.*?) \| (.*?) \| (.*?) \|', table_content)
        
        for name, data_type, description in rows:
            properties.append({
                "name": name.strip(),
                "type": data_type.strip(),
                "description": description.strip()
            })
    
    return {
        "model_name": model_name,
        "properties": properties
    }

def process_api_docs():
    """Process all API documentation files."""
    api_info = []
    
    for file_name in os.listdir(API_DOCS_DIR):
        if file_name.endswith('.md') and not os.path.isdir(os.path.join(API_DOCS_DIR, file_name)):
            file_path = os.path.join(API_DOCS_DIR, file_name)
            try:
                info = extract_api_info(file_path)
                api_info.append(info)
                print(f"Processed API: {info['api_name']} ({len(info['methods'])} methods)")
            except Exception as e:
                print(f"Error processing {file_name}: {str(e)}")
    
    # Save combined API info
    with open(os.path.join(OUTPUT_DIR, 'looker_api_methods.json'), 'w') as f:
        json.dump(api_info, f, indent=2)
    
    return api_info

def process_model_docs():
    """Process all model documentation files."""
    model_info = []
    
    for file_name in os.listdir(MODELS_DIR):
        if file_name.endswith('.md'):
            file_path = os.path.join(MODELS_DIR, file_name)
            try:
                info = extract_model_info(file_path)
                model_info.append(info)
                print(f"Processed Model: {info['model_name']} ({len(info['properties'])} properties)")
            except Exception as e:
                print(f"Error processing {file_name}: {str(e)}")
    
    # Save combined model info
    with open(os.path.join(OUTPUT_DIR, 'looker_api_types.json'), 'w') as f:
        json.dump(model_info, f, indent=2)
    
    return model_info

def generate_reference_markdown(api_info, model_info):
    """Generate a comprehensive Markdown reference."""
    md_content = "# Looker API Reference\n\n"
    
    # API Methods section
    md_content += "## API Methods\n\n"
    
    for api in api_info:
        md_content += f"### {api['api_name']}\n\n"
        
        for method in api['methods']:
            md_content += f"#### {method['name']}\n\n"
            if method['endpoint']:
                md_content += f"**Endpoint:** `{method['endpoint']}`\n\n"
            if method['description']:
                md_content += f"{method['description']}\n\n"
    
    # Type Definitions section
    md_content += "## Type Definitions\n\n"
    
    for model in model_info:
        md_content += f"### {model['model_name']}\n\n"
        
        if model['properties']:
            md_content += "| Property | Type | Description |\n"
            md_content += "|----------|------|-------------|\n"
            
            for prop in model['properties']:
                md_content += f"| {prop['name']} | {prop['type']} | {prop['description']} |\n"
            
            md_content += "\n"
    
    # Save reference markdown
    with open(os.path.join(OUTPUT_DIR, 'looker_api_reference.md'), 'w') as f:
        f.write(md_content)
    
    # Create processed version for data store
    processed_file = os.path.join(PROCESSED_DIR, 'looker_api_reference.layout.txt')
    with open(processed_file, 'w') as f:
        f.write(md_content)
    
    print(f"Generated reference markdown: {os.path.join(OUTPUT_DIR, 'looker_api_reference.md')}")
    print(f"Generated processed file for data store: {processed_file}")

def main():
    print("Starting Looker API documentation processing...")
    setup_directories()
    
    api_info = process_api_docs()
    model_info = process_model_docs()
    
    generate_reference_markdown(api_info, model_info)
    
    print("\nProcessing complete!")
    print(f"Processed files are in: {OUTPUT_DIR}")
    print(f"Files ready for data store upload are in: {PROCESSED_DIR}")

if __name__ == "__main__":
    main() 