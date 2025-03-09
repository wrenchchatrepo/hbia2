# Google Cloud APIs Required for Vertex AI Agent Builder

The following APIs need to be enabled in your Google Cloud project to successfully set up and run the Vertex AI Agent Builder:

## Core APIs

- [x] AI Platform API (`aiplatform.googleapis.com`)
- [x] Cloud Storage API (`storage.googleapis.com`)
- [x] Artifact Registry API (`artifactregistry.googleapis.com`)
- [x] Cloud Resource Manager API (`cloudresourcemanager.googleapis.com`)
- [x] Identity and Access Management (IAM) API (`iam.googleapis.com`)
- [x] Cloud Logging API (`logging.googleapis.com`)
- [x] Cloud Monitoring API (`monitoring.googleapis.com`)

## Additional APIs (Enable as needed)

- [ ] BigQuery API (`bigquery.googleapis.com`) - Required for BigQuery integration
- [ ] Dialogflow API (`dialogflow.googleapis.com`) - Required for conversational interfaces
- [ ] Cloud Run API (`run.googleapis.com`) - Required for deploying serverless applications
- [ ] Secret Manager API (`secretmanager.googleapis.com`) - Recommended for securely storing credentials
- [ ] ~~Cloud Build API (`cloudbuild.googleapis.com`) - Required for CI/CD pipelines~~

## How to Enable APIs

You can enable these APIs using the Google Cloud Console or the gcloud CLI:

### Using gcloud CLI

```bash
# Source environment variables
source .env

# Enable required APIs
gcloud services enable aiplatform.googleapis.com \
    storage.googleapis.com \
    artifactregistry.googleapis.com \
    cloudresourcemanager.googleapis.com \
    iam.googleapis.com \
    logging.googleapis.com \
    monitoring.googleapis.com \
    bigquery.googleapis.com \
    dialogflow.googleapis.com \
    run.googleapis.com \
    secretmanager.googleapis.com \
    cloudbuild.googleapis.com \
    --project=$PROJECT_ID
```

### Using Google Cloud Console

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Select your project
3. Navigate to "APIs & Services" > "Library"
4. Search for each API and click "Enable"

## Verification

To verify that the required APIs are enabled:

```bash
gcloud services list --project=$PROJECT_ID | grep -E 'aiplatform|storage|artifactregistry|cloudresourcemanager|iam|logging|monitoring'
