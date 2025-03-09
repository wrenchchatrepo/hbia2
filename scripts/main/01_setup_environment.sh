#!/bin/bash

# 00_setup_environment.sh
# First script to set up the environment for Vertex AI Agent Builder

# Exit on error
set -e

echo "=== Setting up environment for Vertex AI Agent Builder ==="

# Check if .env file exists
if [ ! -f .env ]; then
  echo "Creating .env file from template..."
  cp .env.example .env
  echo "Please edit the .env file with your specific values before continuing."
  exit 1
else
  echo ".env file already exists."
  source .env
fi

# Check required environment variables
echo "Checking required environment variables..."
[ -z "$PROJECT_ID" ] && { echo "ERROR: PROJECT_ID is not set in .env file"; exit 1; }
[ -z "$REGION" ] && { echo "ERROR: REGION is not set in .env file"; exit 1; }
[ -z "$BUCKET_BASE" ] && { echo "ERROR: BUCKET_BASE is not set in .env file"; exit 1; }

# Check if Google Cloud SDK is installed
if [ ! -d "google-cloud-sdk" ]; then
  echo "Google Cloud SDK not found. Downloading..."
  curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-latest-darwin-x86_64.tar.gz
  tar -xzf google-cloud-sdk-latest-darwin-x86_64.tar.gz
  ./google-cloud-sdk/install.sh --quiet
  rm google-cloud-sdk-latest-darwin-x86_64.tar.gz
else
  echo "Google Cloud SDK already installed."
fi

# Add Google Cloud SDK to PATH
export PATH=$PATH:$(pwd)/google-cloud-sdk/bin

# Check authentication
echo "Checking Google Cloud authentication..."
if ! gcloud auth list 2>/dev/null | grep -q "ACTIVE"; then
  echo "Not authenticated with Google Cloud. Please run:"
  echo "gcloud auth login"
  exit 1
else
  echo "Already authenticated with Google Cloud."
fi

# Set project
echo "Setting Google Cloud project to $PROJECT_ID..."
gcloud config set project $PROJECT_ID

# Enable required APIs
echo "Enabling required APIs..."
gcloud services enable aiplatform.googleapis.com \
    storage.googleapis.com \
    artifactregistry.googleapis.com \
    cloudresourcemanager.googleapis.com \
    iam.googleapis.com \
    logging.googleapis.com \
    monitoring.googleapis.com

echo "=== Environment setup completed ==="
echo "You can now proceed to the next script: 01_setup_directory_structure.sh" 