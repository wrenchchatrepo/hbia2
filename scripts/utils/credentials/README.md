# Secure Credential Management

This directory contains utilities for securely managing organization credentials using macOS Keychain.

## Overview

Instead of hardcoding sensitive information like SSNs, bank account details, and company information in your code, these utilities allow you to:

1. Securely store credentials in the macOS Keychain
2. Retrieve credentials when needed by your application
3. Keep sensitive information out of your codebase and version control

## Files

- `store_credentials.py`: Script to store organization details in the Keychain
- `retrieve_credentials.py`: Library to retrieve credentials from the Keychain
- `example_usage.py`: Example showing how to use the credentials in an application

## Usage

### Step 1: Store Credentials

Run the storage script to securely add your organization details to the Keychain:

```bash
cd /Users/dionedge/dev/hbia2/scripts/utils/credentials
python3 store_credentials.py
```

You will be prompted to enter each piece of information. Sensitive fields like SSN and bank details will have masked input.

### Step 2: Use Credentials in Your Application

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

1. The `store_credentials.py` script should be run once to set up credentials and then secured or deleted.
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