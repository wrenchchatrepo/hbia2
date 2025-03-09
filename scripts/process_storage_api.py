#!/usr/bin/env python3
import os
import json
import glob
import re
from pathlib import Path

# Configuration
INPUT_DIR = os.path.join("scraped_content", "storage_api")
OUTPUT_DIR = os.path.join("processed", "storage_api")

def setup_directories():
    """Create necessary directories."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def clean_text(text):
    """Clean and normalize text content."""
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove navigation elements and other common noise
    text = re.sub(r'Home\s+Cloud Storage\s+Documentation', '', text)
    # Trim whitespace
    text = text.strip()
    return text

def process_methods():
    """Process the Storage API methods."""
    print("Processing Storage API methods...")
    
    # Load the main methods file
    methods_file = os.path.join(INPUT_DIR, "storage_api_methods.json")
    if not os.path.exists(methods_file):
        print(f"Error: Methods file not found at {methods_file}")
        return
    
    with open(methods_file, 'r') as f:
        methods = json.load(f)
    
    # Process and enhance methods with additional information
    enhanced_methods = []
    
    for method in methods:
        name = method.get("name", "").strip()
        description = method.get("description", "").strip()
        
        # Skip empty or navigation-related entries
        if not name or name in ["Home", "Cloud Storage", "Documentation"]:
            continue
        
        # Extract resource type if present
        resource_type = None
        if name.startswith("REST Resource:") or name.endswith("resource representation"):
            resource_type = name.replace("REST Resource:", "").replace("resource representation", "").strip()
        
        enhanced_method = {
            "name": name,
            "description": description,
            "resource_type": resource_type
        }
        
        enhanced_methods.append(enhanced_method)
    
    # Save the enhanced methods
    output_file = os.path.join(OUTPUT_DIR, "storage_api_methods_processed.json")
    with open(output_file, 'w') as f:
        json.dump(enhanced_methods, f, indent=2)
    
    print(f"Processed {len(enhanced_methods)} methods and saved to {output_file}")
    return enhanced_methods

def process_endpoints():
    """Process the Storage API endpoints from individual method files."""
    print("Processing Storage API endpoints...")
    
    # Find all method JSON files
    method_files = glob.glob(os.path.join(INPUT_DIR, "*_methods.json"))
    
    all_endpoints = []
    
    for method_file in method_files:
        # Skip the main methods file
        if method_file.endswith("storage_api_methods.json"):
            continue
        
        # Extract endpoint name from filename
        filename = os.path.basename(method_file)
        endpoint_name = filename.replace("storage_api_", "").replace("_methods.json", "")
        
        # Load the method details
        with open(method_file, 'r') as f:
            method_details = json.load(f)
        
        # Extract HTTP request if available
        http_request = None
        parameters = []
        request_body = None
        response_body = None
        
        for detail in method_details:
            detail_name = detail.get("name", "").strip()
            detail_desc = detail.get("description", "").strip()
            
            if detail_name == "HTTP request":
                http_request = detail_desc
            elif detail_name == "Path parameters" and detail_desc:
                parameters.append({
                    "type": "path",
                    "description": detail_desc
                })
            elif detail_name == "Query parameters" and detail_desc:
                parameters.append({
                    "type": "query",
                    "description": detail_desc
                })
            elif detail_name == "Request body" and detail_desc:
                request_body = detail_desc
            elif detail_name == "Response body" and detail_desc:
                response_body = detail_desc
        
        # Create endpoint entry
        endpoint = {
            "name": endpoint_name,
            "http_request": http_request,
            "parameters": parameters,
            "request_body": request_body,
            "response_body": response_body,
            "details": method_details
        }
        
        all_endpoints.append(endpoint)
    
    # Save all endpoints
    output_file = os.path.join(OUTPUT_DIR, "storage_api_endpoints.json")
    with open(output_file, 'w') as f:
        json.dump(all_endpoints, f, indent=2)
    
    print(f"Processed {len(all_endpoints)} endpoints and saved to {output_file}")
    return all_endpoints

def create_reference_markdown():
    """Create a comprehensive reference markdown file."""
    print("Creating comprehensive reference markdown...")
    
    # Load processed methods and endpoints
    methods_file = os.path.join(OUTPUT_DIR, "storage_api_methods_processed.json")
    endpoints_file = os.path.join(OUTPUT_DIR, "storage_api_endpoints.json")
    
    if not os.path.exists(methods_file) or not os.path.exists(endpoints_file):
        print("Error: Processed files not found. Run process_methods() and process_endpoints() first.")
        return
    
    with open(methods_file, 'r') as f:
        methods = json.load(f)
    
    with open(endpoints_file, 'r') as f:
        endpoints = json.load(f)
    
    # Create the reference markdown
    markdown = "# Google Cloud Storage API Reference\n\n"
    
    # Add methods section
    markdown += "## API Resources\n\n"
    
    resource_methods = [m for m in methods if m.get("resource_type")]
    for method in resource_methods:
        markdown += f"### {method['name']}\n\n"
        if method['description']:
            markdown += f"{method['description']}\n\n"
    
    # Add endpoints section
    markdown += "## API Endpoints\n\n"
    
    for endpoint in endpoints:
        markdown += f"### {endpoint['name']}\n\n"
        
        if endpoint['http_request']:
            markdown += f"**HTTP Request:** `{endpoint['http_request']}`\n\n"
        
        if endpoint['parameters']:
            markdown += "**Parameters:**\n\n"
            for param in endpoint['parameters']:
                markdown += f"- **{param['type']} parameters:** {param['description']}\n\n"
        
        if endpoint['request_body']:
            markdown += f"**Request Body:** {endpoint['request_body']}\n\n"
        
        if endpoint['response_body']:
            markdown += f"**Response Body:** {endpoint['response_body']}\n\n"
        
        markdown += "**Details:**\n\n"
        for detail in endpoint['details']:
            if detail['name'] and detail['name'] not in ["HTTP request", "Path parameters", "Query parameters", "Request body", "Response body"]:
                markdown += f"- **{detail['name']}:** {detail['description']}\n\n"
    
    # Save the reference markdown
    output_file = os.path.join(OUTPUT_DIR, "storage_api_reference.md")
    with open(output_file, 'w') as f:
        f.write(markdown)
    
    print(f"Created comprehensive reference markdown at {output_file}")

def main():
    print("Starting Google Cloud Storage API data processing...")
    setup_directories()
    
    # Process methods and endpoints
    process_methods()
    process_endpoints()
    
    # Create comprehensive reference
    create_reference_markdown()
    
    print("\nProcessing complete!")
    print(f"Processed files are in: {OUTPUT_DIR}")

if __name__ == "__main__":
    main() 