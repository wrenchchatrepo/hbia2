#!/usr/bin/env python3
"""
Script to securely retrieve organization details from macOS Keychain.
This script provides functions to access the credentials stored in the Keychain.
"""

import subprocess
from typing import Dict, Optional, Any, List, Union

# Service name for the keychain entries (as specified in your custom instructions)
SERVICE_NAME = "mcp-servers"

# Organization details keys
ORG_KEYS = [
    "COMPANY_OWNER_SSN",
    "BANK_ACCT",
    "BANK_ROUTING",
    "COMPANY_NAME",
    "COMPANY_EIN",
    "COMPANY_ADDRESS",
    "COMPANY_OWNER"
]

def get_from_keychain(service: str, account: str) -> Optional[str]:
    """
    Retrieve a password from the macOS Keychain.
    
    Args:
        service: The service name
        account: The account/key name
        
    Returns:
        str: The retrieved password/value, or None if not found
    """
    try:
        cmd = ["security", "find-generic-password", "-s", service, "-a", account, "-w"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            # Item not found or other error - return None silently
            return None
    except Exception as e:
        print(f"❌ Error retrieving {account}: {str(e)}")
        return None

def get_organization_details() -> Dict[str, str]:
    """
    Retrieve all organization details from the Keychain.
    
    Returns:
        Dict[str, str]: Dictionary of organization details
    """
    details = {}
    for key in ORG_KEYS:
        value = get_from_keychain(SERVICE_NAME, key)
        if value:
            details[key] = value
    return details

def get_specific_detail(key: str) -> Optional[str]:
    """
    Retrieve a specific organization detail from the Keychain.
    
    Args:
        key: The key to retrieve
        
    Returns:
        Optional[str]: The value, or None if not found
    """
    if key not in ORG_KEYS:
        print(f"❌ Unknown key: {key}")
        print(f"Available keys: {', '.join(ORG_KEYS)}")
        return None
    
    return get_from_keychain(SERVICE_NAME, key)

def main():
    """Main function to demonstrate retrieving organization details."""
    print("\n=== Organization Details Retrieval Utility ===")
    print("This utility demonstrates retrieving organization details from macOS Keychain.")
    print("The information is stored under the service name:", SERVICE_NAME)
    
    # Get all details
    details = get_organization_details()
    
    if not details:
        print("\n❌ No organization details found in the Keychain.")
        print("Please run store_credentials.py first to set up the credentials.")
        return
    
    # Display available keys
    print("\nAvailable organization details:")
    for key in details.keys():
        print(f"- {key}")
    
    # Example of retrieving a specific detail
    print("\nExample usage in your code:")
    print("```python")
    print("from scripts.utils.credentials.retrieve_credentials import get_specific_detail")
    print("")
    print("# Get company name")
    print("company_name = get_specific_detail('COMPANY_NAME')")
    print("print(f'Company: {company_name}')")
    print("```")
    
    print("\nSecurity note: Values are not displayed here for security reasons.")

if __name__ == "__main__":
    main() 