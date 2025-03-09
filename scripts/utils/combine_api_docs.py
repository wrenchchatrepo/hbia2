#!/usr/bin/env python3
import os
import json
import glob
from pathlib import Path

# Configuration
OUTPUT_DIR = os.path.join("processed", "combined")
LOOKER_DIR = os.path.join("processed", "looker_api")
BIGQUERY_DIR = os.path.join("processed", "bigquery_api")
STORAGE_DIR = os.path.join("processed", "storage_api")

def setup_directories():
    """Create necessary directories."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def combine_api_docs():
    """Combine all API documentation into a single comprehensive reference file."""
    print("Combining API documentation...")
    
    # Create the combined markdown
    markdown = "# Google Cloud API Reference\n\n"
    markdown += "This document combines reference documentation for multiple Google Cloud APIs.\n\n"
    
    # Add table of contents
    markdown += "## Table of Contents\n\n"
    markdown += "1. [Looker API](#looker-api)\n"
    markdown += "2. [BigQuery API](#bigquery-api)\n"
    markdown += "3. [Cloud Storage API](#cloud-storage-api)\n\n"
    
    # Add Looker API section
    markdown += "## Looker API\n\n"
    looker_ref_file = os.path.join(LOOKER_DIR, "looker_api_reference.md")
    if os.path.exists(looker_ref_file):
        with open(looker_ref_file, 'r') as f:
            # Skip the first line (title) as we already have our own title
            lines = f.readlines()
            if len(lines) > 1:
                markdown += "".join(lines[1:])
    else:
        markdown += "Looker API documentation not found.\n\n"
    
    # Add Looker API model properties
    looker_models_file = os.path.join(LOOKER_DIR, "looker_api_model_properties.md")
    if os.path.exists(looker_models_file):
        with open(looker_models_file, 'r') as f:
            # Skip the first line (title) as we already have our own title
            lines = f.readlines()
            if len(lines) > 1:
                markdown += "### Looker API Models\n\n"
                markdown += "".join(lines[1:])
    
    # Add BigQuery API section
    markdown += "## BigQuery API\n\n"
    bigquery_ref_file = os.path.join(BIGQUERY_DIR, "bigquery_api_reference.md")
    if os.path.exists(bigquery_ref_file):
        with open(bigquery_ref_file, 'r') as f:
            # Skip the first line (title) as we already have our own title
            lines = f.readlines()
            if len(lines) > 1:
                markdown += "".join(lines[1:])
    else:
        markdown += "BigQuery API documentation not found.\n\n"
    
    # Add Cloud Storage API section
    markdown += "## Cloud Storage API\n\n"
    storage_ref_file = os.path.join(STORAGE_DIR, "storage_api_reference.md")
    if os.path.exists(storage_ref_file):
        with open(storage_ref_file, 'r') as f:
            # Skip the first line (title) as we already have our own title
            lines = f.readlines()
            if len(lines) > 1:
                markdown += "".join(lines[1:])
    else:
        markdown += "Cloud Storage API documentation not found.\n\n"
    
    # Save the combined reference markdown
    output_file = os.path.join(OUTPUT_DIR, "google_cloud_api_reference.md")
    with open(output_file, 'w') as f:
        f.write(markdown)
    
    print(f"Created combined API reference at {output_file}")

def create_api_index():
    """Create an index of all API methods and endpoints."""
    print("Creating API index...")
    
    all_apis = {
        "looker": {
            "name": "Looker API",
            "methods": [],
            "endpoints": [],
            "models": []
        },
        "bigquery": {
            "name": "BigQuery API",
            "methods": [],
            "endpoints": []
        },
        "storage": {
            "name": "Cloud Storage API",
            "methods": [],
            "endpoints": []
        }
    }
    
    # Load Looker API methods
    looker_methods_file = os.path.join(LOOKER_DIR, "looker_api_methods.json")
    if os.path.exists(looker_methods_file):
        with open(looker_methods_file, 'r') as f:
            try:
                methods = json.load(f)
                for method in methods:
                    api_name = method.get("api_name", "")
                    api_methods = method.get("methods", [])
                    for api_method in api_methods:
                        all_apis["looker"]["methods"].append({
                            "api_name": api_name,
                            "name": api_method.get("name", ""),
                            "description": api_method.get("description", ""),
                            "endpoint": api_method.get("endpoint", ""),
                            "api": "looker"
                        })
            except json.JSONDecodeError:
                print(f"Error: Could not parse {looker_methods_file}")
    
    # Load Looker API model properties
    looker_models_file = os.path.join(LOOKER_DIR, "looker_api_model_properties.json")
    if os.path.exists(looker_models_file):
        with open(looker_models_file, 'r') as f:
            try:
                models = json.load(f)
                for model in models:
                    all_apis["looker"]["models"].append({
                        "name": model.get("name", ""),
                        "properties": model.get("properties", []),
                        "api": "looker"
                    })
            except json.JSONDecodeError:
                print(f"Error: Could not parse {looker_models_file}")
    
    # Load BigQuery API methods
    bigquery_methods_file = os.path.join(BIGQUERY_DIR, "bigquery_api_methods_processed.json")
    if os.path.exists(bigquery_methods_file):
        with open(bigquery_methods_file, 'r') as f:
            try:
                methods = json.load(f)
                for method in methods:
                    all_apis["bigquery"]["methods"].append({
                        "name": method.get("name", ""),
                        "description": method.get("description", ""),
                        "resource_type": method.get("resource_type", ""),
                        "api": "bigquery"
                    })
            except json.JSONDecodeError:
                print(f"Error: Could not parse {bigquery_methods_file}")
    
    # Load BigQuery API endpoints
    bigquery_endpoints_file = os.path.join(BIGQUERY_DIR, "bigquery_api_endpoints.json")
    if os.path.exists(bigquery_endpoints_file):
        with open(bigquery_endpoints_file, 'r') as f:
            try:
                endpoints = json.load(f)
                for endpoint in endpoints:
                    all_apis["bigquery"]["endpoints"].append({
                        "name": endpoint.get("name", ""),
                        "http_request": endpoint.get("http_request", ""),
                        "api": "bigquery"
                    })
            except json.JSONDecodeError:
                print(f"Error: Could not parse {bigquery_endpoints_file}")
    
    # Load Storage API methods
    storage_methods_file = os.path.join(STORAGE_DIR, "storage_api_methods_processed.json")
    if os.path.exists(storage_methods_file):
        with open(storage_methods_file, 'r') as f:
            try:
                methods = json.load(f)
                for method in methods:
                    all_apis["storage"]["methods"].append({
                        "name": method.get("name", ""),
                        "description": method.get("description", ""),
                        "resource_type": method.get("resource_type", ""),
                        "api": "storage"
                    })
            except json.JSONDecodeError:
                print(f"Error: Could not parse {storage_methods_file}")
    
    # Load Storage API endpoints
    storage_endpoints_file = os.path.join(STORAGE_DIR, "storage_api_endpoints.json")
    if os.path.exists(storage_endpoints_file):
        with open(storage_endpoints_file, 'r') as f:
            try:
                endpoints = json.load(f)
                for endpoint in endpoints:
                    all_apis["storage"]["endpoints"].append({
                        "name": endpoint.get("name", ""),
                        "http_request": endpoint.get("http_request", ""),
                        "api": "storage"
                    })
            except json.JSONDecodeError:
                print(f"Error: Could not parse {storage_endpoints_file}")
    
    # Save the API index
    output_file = os.path.join(OUTPUT_DIR, "api_index.json")
    with open(output_file, 'w') as f:
        json.dump(all_apis, f, indent=2)
    
    print(f"Created API index at {output_file}")
    
    # Create a markdown version of the index
    markdown = "# Google Cloud API Index\n\n"
    
    for api_key, api_data in all_apis.items():
        markdown += f"## {api_data['name']}\n\n"
        
        if api_data['methods']:
            markdown += "### Methods\n\n"
            for method in api_data['methods']:
                markdown += f"- **{method['name']}**"
                if method.get('description'):
                    markdown += f": {method['description']}"
                markdown += "\n"
            markdown += "\n"
        
        if api_data['endpoints']:
            markdown += "### Endpoints\n\n"
            for endpoint in api_data['endpoints']:
                markdown += f"- **{endpoint['name']}**"
                if endpoint.get('http_request'):
                    markdown += f": `{endpoint['http_request']}`"
                markdown += "\n"
            markdown += "\n"
        
        if api_key == 'looker' and api_data['models']:
            markdown += "### Models\n\n"
            for model in api_data['models']:
                markdown += f"- **{model['name']}**"
                if model.get('properties'):
                    markdown += f" ({len(model['properties'])} properties)"
                markdown += "\n"
            markdown += "\n"
    
    # Save the markdown index
    output_md_file = os.path.join(OUTPUT_DIR, "api_index.md")
    with open(output_md_file, 'w') as f:
        f.write(markdown)
    
    print(f"Created markdown API index at {output_md_file}")

def main():
    print("Starting API documentation combination...")
    setup_directories()
    
    # Combine API docs
    combine_api_docs()
    
    # Create API index
    create_api_index()
    
    print("\nCombination complete!")
    print(f"Combined files are in: {OUTPUT_DIR}")

if __name__ == "__main__":
    main() 