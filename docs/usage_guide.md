# HBIA2 Usage Guide

This document provides instructions for using the HBIA2 repository.

## Overview

The HBIA2 repository provides scripts for scraping, processing, and uploading documentation for various Google Cloud products. The repository supports the following products:

1. **BigQuery**: Google's fully managed, serverless data warehouse.
2. **Looker**: Business intelligence and data analytics platform.
3. **Looker Studio**: Data visualization and reporting platform.
4. **GCP**: Google Cloud Platform services.
5. **dbt**: Data build tool for analytics engineering.
6. **Omni**: Looker's multi-cloud analytics solution.
7. **Storage**: Google Cloud Storage.

## Scraping Content

To scrape content, use the scripts in the `scripts/scrapers/` directory. The repository provides scripts for scraping API documentation, general documentation, and GitHub repositories.

### Scraping API Documentation

To scrape API documentation for a product, use the corresponding script in the `scripts/scrapers/api/` directory. For example, to scrape BigQuery API documentation:

```bash
cd scripts/scrapers/api
python3 scrape_bigquery_api.py
```

The scraped content will be saved to the `data/<product>/api/scraped/` directory.

### Scraping General Documentation

To scrape general documentation for a product, use the corresponding script in the `scripts/scrapers/docs/` directory. For example, to scrape BigQuery documentation:

```bash
cd scripts/scrapers/docs
python3 scrape_bigquery_docs.py
```

The scraped content will be saved to the `data/<product>/docs/scraped/` directory.

### Scraping GitHub Repositories

To scrape a GitHub repository for a product, use the corresponding script in the `scripts/scrapers/github/` directory. For example, to scrape the dbt GitHub repository:

```bash
cd scripts/scrapers/github
python3 scrape_dbt_github.py
```

The scraped content will be saved to the `data/<product>/github/scraped/` directory.

## Processing Content

To process content, use the scripts in the `scripts/processors/` directory. The repository provides scripts for processing API documentation, general documentation, and GitHub repositories.

### Processing API Documentation

To process API documentation for a product, use the corresponding script in the `scripts/processors/api/` directory. For example, to process BigQuery API documentation:

```bash
cd scripts/processors/api
python3 process_bigquery_api.py
```

The processed content will be saved to the `data/<product>/api/processed/` directory.

### Processing General Documentation

To process general documentation for a product, use the corresponding script in the `scripts/processors/docs/` directory. For example, to process BigQuery documentation:

```bash
cd scripts/processors/docs
python3 process_bigquery_docs.py
```

The processed content will be saved to the `data/<product>/docs/processed/` directory.

### Processing GitHub Repositories

To process a GitHub repository for a product, use the corresponding script in the `scripts/processors/github/` directory. For example, to process the dbt GitHub repository:

```bash
cd scripts/processors/github
python3 process_dbt_github.py
```

The processed content will be saved to the `data/<product>/github/processed/` directory.

## Uploading Content

To upload content, use the scripts in the `scripts/upload/` directory. The repository provides scripts for uploading content to Google Cloud Storage buckets and datastores.

### Uploading to Google Cloud Storage Buckets

To upload content to a Google Cloud Storage bucket, use the `scripts/upload/upload_to_bucket.py` script. For example, to upload processed BigQuery API documentation:

```bash
cd scripts/upload
python3 upload_to_bucket.py --product bigquery --content-type api --source-type processed
```

The content will be uploaded to the corresponding Google Cloud Storage bucket as specified in the `config/bucket_mappings.json` file.

### Uploading to Datastores

To upload content to a datastore, use the `scripts/upload/upload_to_datastore.py` script. For example, to upload processed BigQuery API documentation:

```bash
cd scripts/upload
python3 upload_to_datastore.py --product bigquery --content-type api --source-type processed
```

The content will be uploaded to the corresponding datastore as specified in the `config/datastore_mappings.json` file.

## Utility Scripts

The repository provides utility scripts in the `scripts/utils/` directory. These scripts perform various tasks such as combining API documentation and extracting model properties.

### Combining API Documentation

To combine API documentation from multiple products, use the `scripts/utils/combine_api_docs.py` script:

```bash
cd scripts/utils
python3 combine_api_docs.py
```

The combined API documentation will be saved to the `data/combined/api/` directory.

### Extracting Model Properties

To extract model properties from Looker API documentation, use the `scripts/utils/extract_looker_models.py` script:

```bash
cd scripts/utils
python3 extract_looker_models.py
```

The extracted model properties will be saved to the `data/looker/api/processed/` directory.

## Examples

Here are some examples of common tasks:

### Scrape and Process BigQuery API Documentation

```bash
# Scrape BigQuery API documentation
cd scripts/scrapers/api
python3 scrape_bigquery_api.py

# Process BigQuery API documentation
cd ../../processors/api
python3 process_bigquery_api.py

# Upload processed BigQuery API documentation to GS bucket
cd ../../upload
python3 upload_to_bucket.py --product bigquery --content-type api --source-type processed

# Upload processed BigQuery API documentation to datastore
python3 upload_to_datastore.py --product bigquery --content-type api --source-type processed
```

### Scrape and Process Looker Documentation

```bash
# Scrape Looker documentation
cd scripts/scrapers/docs
python3 scrape_looker_docs.py

# Process Looker documentation
cd ../../processors/docs
python3 process_looker_docs.py

# Upload processed Looker documentation to GS bucket
cd ../../upload
python3 upload_to_bucket.py --product looker --content-type docs --source-type processed

# Upload processed Looker documentation to datastore
python3 upload_to_datastore.py --product looker --content-type docs --source-type processed
```

### Scrape and Process dbt GitHub Repository

```bash
# Scrape dbt GitHub repository
cd scripts/scrapers/github
python3 scrape_dbt_github.py

# Process dbt GitHub repository
cd ../../processors/github
python3 process_dbt_github.py

# Upload processed dbt GitHub repository to GS bucket
cd ../../upload
python3 upload_to_bucket.py --product dbt --content-type github --source-type processed

# Upload processed dbt GitHub repository to datastore
python3 upload_to_datastore.py --product dbt --content-type github --source-type processed
``` 