#!/usr/bin/env python3
import os
import json
import re
from pathlib import Path

# Configuration
INPUT_FILE = os.path.join("scraped_content", "looker_api", "looker_api_methods.json")
OUTPUT_DIR = os.path.join("processed", "looker_api")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "looker_api_model_properties.json")

def setup_directories():
    """Create necessary directories."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_model_properties():
    """Extract model properties from the Looker API methods JSON file."""
    print(f"Extracting model properties from {INPUT_FILE}...")
    
    if not os.path.exists(INPUT_FILE):
        print(f"Error: Input file not found at {INPUT_FILE}")
        return []
    
    with open(INPUT_FILE, 'r') as f:
        api_methods = json.load(f)
    
    # Extract model names and properties from API methods
    models = {}
    
    for api in api_methods:
        api_name = api.get("api_name", "")
        methods = api.get("methods", [])
        
        for method in methods:
            method_name = method.get("name", "")
            method_desc = method.get("description", "")
            
            # Look for model definitions in method descriptions
            # Models are often mentioned in return types or parameters
            if "Return type" in method_name:
                # Extract model name from return type
                model_match = re.search(r'([A-Z][A-Za-z0-9]+)', method_desc)
                if model_match:
                    model_name = model_match.group(1)
                    if model_name not in models:
                        models[model_name] = {"name": model_name, "properties": []}
            
            # Look for parameter descriptions that might contain model properties
            if "Parameters" in method_name:
                # Extract parameter details
                param_matches = re.finditer(r'[-*]\s*`([^`]+)`\s*[:-]\s*([^\n]+)', method_desc)
                
                for param_match in param_matches:
                    param_name = param_match.group(1).strip()
                    param_desc = param_match.group(2).strip()
                    
                    # Try to extract type from description
                    type_match = re.search(r'\(([^)]+)\)', param_desc)
                    param_type = type_match.group(1) if type_match else "unknown"
                    
                    # If the parameter type looks like a model (starts with uppercase)
                    if re.match(r'^[A-Z]', param_type):
                        model_name = param_type
                        if model_name not in models:
                            models[model_name] = {"name": model_name, "properties": []}
    
    # Now look for model definitions in the API methods
    for api in api_methods:
        methods = api.get("methods", [])
        
        for method in methods:
            method_name = method.get("name", "")
            
            # If the method name looks like a model name (starts with uppercase)
            if re.match(r'^[A-Z][A-Za-z0-9]+$', method_name) and not method_name.endswith("Api"):
                model_name = method_name
                if model_name not in models:
                    models[model_name] = {"name": model_name, "properties": []}
                
                # Look for property definitions in the method description
                method_desc = method.get("description", "")
                
                # Format: - `property_name` - description (type)
                property_matches = re.finditer(r'[-*]\s*`([^`]+)`\s*-\s*([^\n]+)', method_desc)
                
                for property_match in property_matches:
                    property_name = property_match.group(1).strip()
                    property_description = property_match.group(2).strip()
                    
                    # Try to extract type from description
                    type_match = re.search(r'\(([^)]+)\)', property_description)
                    property_type = type_match.group(1) if type_match else "unknown"
                    
                    # Add property to model
                    models[model_name]["properties"].append({
                        "name": property_name,
                        "type": property_type,
                        "description": property_description
                    })
                
                # Format: - `property_name`: description
                property_matches = re.finditer(r'[-*]\s*`([^`]+)`\s*:\s*([^\n]+)', method_desc)
                
                for property_match in property_matches:
                    property_name = property_match.group(1).strip()
                    property_description = property_match.group(2).strip()
                    
                    # Try to extract type from description
                    type_match = re.search(r'\(([^)]+)\)', property_description)
                    property_type = type_match.group(1) if type_match else "unknown"
                    
                    # Add property to model
                    models[model_name]["properties"].append({
                        "name": property_name,
                        "type": property_type,
                        "description": property_description
                    })
    
    # Convert models dictionary to list
    model_list = list(models.values())
    
    # Sort models by name
    model_list.sort(key=lambda x: x["name"])
    
    return model_list

def main():
    print("Starting Looker API model properties extraction...")
    setup_directories()
    
    # Extract model properties
    models = extract_model_properties()
    
    # Save the model properties
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(models, f, indent=2)
    
    print(f"Extracted {len(models)} models with properties and saved to {OUTPUT_FILE}")
    
    # Create a markdown version of the model properties
    markdown = "# Looker API Model Properties\n\n"
    
    models_with_properties = [model for model in models if model['properties']]
    models_without_properties = [model for model in models if not model['properties']]
    
    # First list models with properties
    for model in models_with_properties:
        markdown += f"## {model['name']}\n\n"
        
        markdown += "| Property | Type | Description |\n"
        markdown += "|----------|------|-------------|\n"
        
        for prop in model['properties']:
            # Escape pipe characters in property values
            name = prop['name'].replace('|', '\\|')
            type_val = prop['type'].replace('|', '\\|')
            desc = prop['description'].replace('|', '\\|')
            
            markdown += f"| {name} | {type_val} | {desc} |\n"
        
        markdown += "\n"
    
    # Then list models without properties
    if models_without_properties:
        markdown += "## Models Without Extracted Properties\n\n"
        
        for model in models_without_properties:
            markdown += f"- {model['name']}\n"
        
        markdown += "\n"
    
    # Save the markdown
    markdown_file = os.path.join(OUTPUT_DIR, "looker_api_model_properties.md")
    with open(markdown_file, 'w') as f:
        f.write(markdown)
    
    print(f"Created markdown model properties at {markdown_file}")
    print(f"Found {len(models_with_properties)} models with properties and {len(models_without_properties)} models without properties")
    
    print("\nExtraction complete!")

if __name__ == "__main__":
    main() 