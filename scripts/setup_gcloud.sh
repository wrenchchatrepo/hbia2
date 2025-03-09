#!/bin/bash

# Configuration
PROJECT_ID="HeuristicsAI"
SERVICE_ACCOUNT="gemini-cloud@heuristicsai.iam.gserviceaccount.com"
KEY_FILE="/Users/dionedge/dev/creds/heuristicsai-34d197537b6e.json"

echo "Setting up Google Cloud SDK..."

# 1. Authenticate with service account
echo "Authenticating with service account..."
gcloud auth activate-service-account ${SERVICE_ACCOUNT} --key-file=${KEY_FILE}

# 2. Set project
echo "Setting project to ${PROJECT_ID}..."
gcloud config set project ${PROJECT_ID}

# 3. Test authentication and project setup
echo "Testing setup..."
gcloud auth list
gcloud config list project

# 4. Verify service account permissions
echo "Verifying service account permissions..."
gcloud projects get-iam-policy ${PROJECT_ID} \
    --flatten="bindings[].members" \
    --format='table(bindings.role)' \
    --filter="bindings.members:${SERVICE_ACCOUNT}"

echo "Setup complete! Please verify the output above." 