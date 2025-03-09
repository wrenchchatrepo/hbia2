#!/usr/bin/env python3
"""
Example script demonstrating how to use organization details from the Keychain.
This is a safe way to access sensitive information without hardcoding it.
"""

from retrieve_credentials import get_specific_detail, get_organization_details

def generate_company_info():
    """Generate a formatted company information string."""
    # Get specific details
    company_name = get_specific_detail("COMPANY_NAME")
    company_address = get_specific_detail("COMPANY_ADDRESS")
    company_owner = get_specific_detail("COMPANY_OWNER")
    company_ein = get_specific_detail("COMPANY_EIN")
    
    # Check if we have the necessary information
    if not all([company_name, company_address, company_owner, company_ein]):
        print("❌ Missing some company information. Please check the Keychain.")
        return None
    
    # Format the information
    info = f"""
Company Information:
-------------------
Name: {company_name}
Owner: {company_owner}
EIN: {company_ein}
Address: {company_address}
"""
    return info

def generate_payment_info():
    """Generate a masked payment information string."""
    # Get banking details
    bank_acct = get_specific_detail("BANK_ACCT")
    bank_routing = get_specific_detail("BANK_ROUTING")
    
    # Check if we have the necessary information
    if not all([bank_acct, bank_routing]):
        print("❌ Missing banking information. Please check the Keychain.")
        return None
    
    # Mask sensitive information for display
    masked_acct = f"****{bank_acct[-4:]}" if bank_acct else "Not available"
    masked_routing = f"****{bank_routing[-4:]}" if bank_routing else "Not available"
    
    # Format the information
    info = f"""
Payment Information:
-------------------
Account: {masked_acct}
Routing: {masked_routing}
"""
    return info

def main():
    """Main function demonstrating credential usage."""
    print("\n=== Organization Details Usage Example ===")
    print("This example shows how to safely use organization details in your application.")
    
    # Check if we have any details stored
    details = get_organization_details()
    if not details:
        print("\n❌ No organization details found in the Keychain.")
        print("Please run store_credentials.py first to set up the credentials.")
        return
    
    # Display company information
    company_info = generate_company_info()
    if company_info:
        print(company_info)
    
    # Display payment information (masked)
    payment_info = generate_payment_info()
    if payment_info:
        print(payment_info)
    
    print("\nNote: Sensitive information is masked for security.")
    print("In your actual application, you would use the full values as needed.")

if __name__ == "__main__":
    main() 