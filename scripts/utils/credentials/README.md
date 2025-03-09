# Secure Credential Management

This directory contains utilities for securely managing organization credentials using macOS Keychain.

## Overview

Instead of hardcoding sensitive information like SSNs, bank account details, and company information in your code, these utilities allow you to:

1. Securely store credentials in the macOS Keychain
2. Retrieve credentials when needed by your application
3. Keep sensitive information out of your codebase and version control

## Files

- `store_credentials.py`: Script to store all organization details in the Keychain
- `store_single_credential.py`: Script to store a single credential in the Keychain
- `list_credentials.py`: Script to list all stored organization credentials
- `retrieve_credentials.py`: Library to retrieve credentials from the Keychain
- `example_usage.py`: Example showing how to use the credentials in an application

## Usage

### Step 1: Store Credentials

You have two options for storing credentials:

#### Option 1: Store All Credentials at Once

Run the storage script to securely add all your organization details to the Keychain:

```bash
cd /Users/dionedge/dev/hbia2/scripts/utils/credentials
python3 store_credentials.py
```

You will be prompted to enter each piece of information. Sensitive fields like SSN and bank details will have masked input.

#### Option 2: Store Individual Credentials

To store a single credential at a time:

```bash
python3 store_single_credential.py CREDENTIAL_NAME
```

For example:
```bash
python3 store_single_credential.py COMPANY_NAME
```

To see a list of available credential names:
```bash
python3 store_single_credential.py --list
```

### Step 2: View Stored Credentials

To see what credentials are currently stored:

```bash
python3 list_credentials.py
```

This will display all stored credentials with sensitive information masked.

### Step 3: Use Credentials in Your Application

Import the retrieval functions in your application code:

```python
from scripts.utils.credentials.retrieve_credentials import get_specific_detail

# Get a specific credential
company_name = get_specific_detail("COMPANY_NAME")
company_ein = get_specific_detail("COMPANY_EIN")

# Use the credentials in your application
print(f"Processing data for {company_name} (EIN: {company_ein})")
```

### Example

To see a working example:

```bash
cd /Users/dionedge/dev/hbia2/scripts/utils/credentials
python3 example_usage.py
```

## Security Notes

1. The credential storage scripts should be run in a secure environment.
2. Never commit sensitive information to version control.
3. The macOS Keychain provides strong encryption for your credentials.
4. Access to the Keychain may require user authentication depending on your macOS security settings.

## Available Credential Keys

The following credential keys are available:

- `COMPANY_OWNER_SSN`: Social Security Number of the company owner
- `BANK_ACCT`: Bank account number
- `BANK_ROUTING`: Bank routing number
- `COMPANY_NAME`: Legal name of the company
- `COMPANY_EIN`: Employer Identification Number
- `COMPANY_ADDRESS`: Company's physical address
- `COMPANY_OWNER`: Name of the company owner

## Adding New Credentials

To add new types of credentials, modify the `ORG_KEYS` list in both `store_credentials.py` and `retrieve_credentials.py`. 