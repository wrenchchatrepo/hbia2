#!/usr/bin/env python3
"""
Script to securely store organization details in macOS Keychain.
This script should be run once to set up the credentials and then deleted or secured.
"""

import subprocess
import getpass
import sys
import os
from typing import Dict, Any, Optional

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

def store_in_keychain(service: str, account: str, password: str) -> bool:
    """
    Store a password in the macOS Keychain.
    
    Args:
        service: The service name
        account: The account/key name
        password: The password/value to store
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Delete existing password if it exists
        subprocess.run(
            ["security", "delete-generic-password", "-s", service, "-a", account],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        
        # Add the new password
        cmd = ["security", "add-generic-password", "-s", service, "-a", account, "-w", password]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ Successfully stored {account} in Keychain")
            return True
        else:
            print(f"❌ Failed to store {account}: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error storing {account}: {str(e)}")
        return False

def get_input(prompt: str, sensitive: bool = False) -> str:
    """Get user input, with option for hidden input for sensitive data."""
    if sensitive:
        return getpass.getpass(prompt)
    else:
        return input(prompt)

def main():
    """Main function to collect and store organization details."""
    print("\n=== Organization Details Storage Utility ===")
    print("This utility will store your organization details securely in macOS Keychain.")
    print("The information will be stored under the service name:", SERVICE_NAME)
    print("\nWARNING: You will be prompted for sensitive information.")
    print("This script should be run in a secure environment.\n")
    
    # Confirm before proceeding
    confirm = input("Do you want to proceed? (y/n): ").lower()
    if confirm != 'y':
        print("Operation cancelled.")
        sys.exit(0)
    
    # Collect and store each piece of information
    details = {}
    
    # Define which fields are sensitive (to mask input)
    sensitive_fields = {
        "COMPANY_OWNER_SSN": True,
        "BANK_ACCT": True,
        "BANK_ROUTING": True,
        "COMPANY_EIN": True,
        "COMPANY_NAME": False,
        "COMPANY_ADDRESS": False,
        "COMPANY_OWNER": False
    }
    
    # Collect information
    for key in ORG_KEYS:
        is_sensitive = sensitive_fields.get(key, False)
        prompt_text = f"Enter {key}: "
        value = get_input(prompt_text, sensitive=is_sensitive)
        details[key] = value
    
    # Store in keychain
    success = True
    for key, value in details.items():
        if not store_in_keychain(SERVICE_NAME, key, value):
            success = False
    
    if success:
        print("\n✅ All organization details have been stored in the Keychain.")
        print("You can now access them using the retrieve_credentials.py script.")
    else:
        print("\n⚠️ Some details could not be stored. Please check the errors above.")
    
    # Security reminder
    print("\n⚠️ SECURITY REMINDER ⚠️")
    print("Consider deleting this script after use or storing it securely.")
    print("It contains code that handles sensitive information.")

if __name__ == "__main__":
    main() 