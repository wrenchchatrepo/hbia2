#!/usr/bin/env python3
"""
List Organization Credentials

This script lists all organization credentials stored in the macOS Keychain
under the service name 'mcp-servers'.
"""

import subprocess
import sys
from retrieve_credentials import ORG_KEYS, SERVICE_NAME, get_from_keychain

def main():
    """List all organization credentials stored in the Keychain."""
    print(f"=== Organization Credentials in Keychain ===")
    print(f"Service name: {SERVICE_NAME}")
    print()
    
    found_any = False
    
    for key in ORG_KEYS:
        try:
            # Try to retrieve the credential
            value = get_from_keychain(SERVICE_NAME, key)
            
            if value is None:
                continue
                
            # Mask sensitive information
            if any(sensitive in key for sensitive in ['SSN', 'EIN', 'BANK', 'ACCT', 'ROUTING']):
                # Show only last 4 characters if available
                if len(value) > 4:
                    display_value = '*' * (len(value) - 4) + value[-4:]
                else:
                    display_value = '*' * len(value)
            else:
                display_value = value
                
            print(f"{key}: {display_value}")
            found_any = True
            
        except subprocess.CalledProcessError:
            # Credential not found
            pass
    
    if not found_any:
        print("No organization credentials found.")
        print("Run store_credentials.py to add organization details to the Keychain.")
    
    print()
    print("To store credentials, run: python3 store_credentials.py")
    print("To store a single credential, run: python3 store_single_credential.py --credential CREDENTIAL_NAME")
    print("To see available credential names, run: python3 store_single_credential.py --list")

if __name__ == "__main__":
    main() 