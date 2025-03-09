# HBIA2 Architecture

This document describes the architecture of the HBIA2 repository.

## Overview

The HBIA2 repository is designed to scrape, process, and upload documentation for various Google Cloud products. The architecture is organized around the following components:

1. **Scrapers**: Scripts for scraping content from documentation websites and GitHub repositories.
2. **Processors**: Scripts for processing scraped content into a format suitable for upload.
3. **Uploaders**: Scripts for uploading processed content to Google Cloud Storage buckets and datastores.

## Data Flow

The data flows through the system as follows:

1. **Scraping**: Content is scraped from documentation websites and GitHub repositories.
2. **Processing**: Scraped content is processed into a format suitable for upload.
3. **Uploading**: Processed content is uploaded to Google Cloud Storage buckets and datastores.

```
[Documentation Websites] --> [Scrapers] --> [Scraped Content]
[GitHub Repositories]    --> [Scrapers] --> [Scraped Content]
                                            [Scraped Content] --> [Processors] --> [Processed Content]
                                                                                   [Processed Content] --> [Uploaders] --> [GCS Buckets]
                                                                                   [Processed Content] --> [Uploaders] --> [Datastores]
```

## Directory Structure

The repository is organized into the following directories:

- `scripts/`: Contains all scripts for scraping, processing, and uploading content.
  - `scrapers/`: Scripts for scraping content.
  - `processors/`: Scripts for processing content.
  - `utils/`: Utility scripts.
  - `upload/`: Scripts for uploading content.
- `data/`: Contains all data (scraped and processed).
  - `<product>/`: Data for a specific product (e.g., BigQuery, Looker).
    - `api/`: API documentation.
    - `docs/`: General documentation.
    - `github/`: GitHub repository content.
- `config/`: Contains configuration files.
  - `bucket_mappings.json`: Mapping of products to GCS buckets.
  - `datastore_mappings.json`: Mapping of products to datastores.
- `docs/`: Contains project documentation.

## Products

The repository supports the following products:

1. **BigQuery**: Google's fully managed, serverless data warehouse.
2. **Looker**: Business intelligence and data analytics platform.
3. **Looker Studio**: Data visualization and reporting platform.
4. **GCP**: Google Cloud Platform services.
5. **dbt**: Data build tool for analytics engineering.
6. **Omni**: Looker's multi-cloud analytics solution.
7. **Storage**: Google Cloud Storage.

## Content Types

For each product, the repository supports the following content types:

1. **API**: API documentation and reference.
2. **Docs**: General product documentation.
3. **GitHub**: Content from GitHub repositories.

## Source Types

For each content type, the repository supports the following source types:

1. **Scraped**: Raw content scraped from documentation websites or GitHub repositories.
2. **Processed**: Processed content ready for upload to GCS buckets and datastores.

## Configuration

The repository uses the following configuration files:

- `config/bucket_mappings.json`: Maps products to GCS buckets.
- `config/datastore_mappings.json`: Maps products to datastores.

## Dependencies

The repository has the following dependencies:

- Python 3.9+
- requests
- BeautifulSoup4
- Google Cloud SDK 