#!/usr/bin/env python3
"""
Store Single Organization Credential

This script stores a single organization credential in the macOS Keychain.
It allows you to specify which credential to store via command line arguments.
"""

import argparse
import getpass
import subprocess
import sys
from retrieve_credentials import ORG_KEYS, SERVICE_NAME

def store_in_keychain(service, account, password):
    """Store a password in the macOS Keychain."""
    try:
        # Delete any existing password for this service and account
        subprocess.run(
            ["security", "delete-generic-password", "-s", service, "-a", account],
            stderr=subprocess.DEVNULL,
            check=False,
        )
        
        # Add the new password
        subprocess.run(
            ["security", "add-generic-password", "-s", service, "-a", account, "-w", password],
            check=True,
            stderr=subprocess.DEVNULL,
        )
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    """Store a single organization credential in the Keychain."""
    parser = argparse.ArgumentParser(description="Store a single organization credential in the macOS Keychain.")
    
    # Create a mutually exclusive group for the credential and list arguments
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--credential", choices=ORG_KEYS, help="The credential to store")
    group.add_argument("--list", action="store_true", help="List available credentials")
    
    args = parser.parse_args()
    
    if args.list:
        print("Available credentials:")
        for key in ORG_KEYS:
            print(f"  - {key}")
        sys.exit(0)
    
    print(f"=== Store Organization Credential ===")
    print(f"Service name: {SERVICE_NAME}")
    print(f"Credential: {args.credential}")
    print()
    
    # Get the value for the credential
    value = getpass.getpass(f"Enter value for {args.credential}: ")
    
    if not value:
        print("Error: Value cannot be empty.")
        sys.exit(1)
    
    # Store the credential
    if store_in_keychain(SERVICE_NAME, args.credential, value):
        print(f"Successfully stored {args.credential} in Keychain.")
    else:
        print(f"Failed to store {args.credential} in Keychain.")
        sys.exit(1)

if __name__ == "__main__":
    main() 