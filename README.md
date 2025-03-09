# HBIA2 Repository

This repository contains scripts and data for scraping, processing, and uploading documentation for various Google Cloud products.

## Repository Structure

```
/hbia2/
├── scripts/                           # All scraping and processing scripts
│   ├── scrapers/                      # Scripts for scraping content
│   │   ├── api/                       # API scraping scripts
│   │   ├── docs/                      # Documentation scraping scripts
│   │   └── github/                    # GitHub repo scraping scripts
│   ├── processors/                    # Scripts for processing content
│   │   ├── api/                       # API processing scripts
│   │   ├── docs/                      # Documentation processing scripts
│   │   └── github/                    # GitHub repo processing scripts
│   ├── utils/                         # Utility scripts
│   └── upload/                        # Scripts for uploading to GS buckets
├── data/                              # All data (scraped and processed)
│   ├── bigquery/                      # BigQuery product data
│   │   ├── api/                       # API documentation
│   │   │   ├── scraped/               # Raw scraped content
│   │   │   └── processed/             # Processed content
│   │   ├── docs/                      # General documentation
│   │   └── github/                    # GitHub repository content
│   ├── looker/                        # Looker product data
│   ├── looker-studio/                 # Looker Studio product data
│   ├── gcp/                           # GCP product data
│   ├── dbt/                           # dbt product data
│   ├── omni/                          # Omni product data
│   └── combined/                      # Combined data across products
├── config/                            # Configuration files
│   ├── bucket_mappings.json           # Mapping of products to GS buckets
│   └── datastore_mappings.json        # Mapping of products to data stores
```

## Products

The repository is organized around the following products:

1. **BigQuery**: Google's fully managed, serverless data warehouse
2. **Looker**: Business intelligence and data analytics platform
3. **Looker Studio**: Data visualization and reporting platform
4. **GCP**: Google Cloud Platform services
5. **dbt**: Data build tool for analytics engineering
6. **Omni**: Looker's multi-cloud analytics solution

## Content Types

For each product, we organize content into the following types:

1. **API**: API documentation and reference
2. **Docs**: General product documentation
3. **GitHub**: Content from GitHub repositories

## Source Types

For each content type, we have two source types:

1. **Scraped**: Raw content scraped from documentation websites or GitHub repositories
2. **Processed**: Processed content ready for upload to GS buckets and data stores

## Scripts

### Scrapers

Scripts for scraping content from documentation websites and GitHub repositories.

- `scripts/scrapers/api/scrape_bigquery_api.py`: Scrape BigQuery API documentation
- `scripts/scrapers/api/scrape_looker_api.py`: Scrape Looker API documentation
- `scripts/scrapers/api/scrape_storage_api.py`: Scrape Google Cloud Storage API documentation

### Processors

Scripts for processing scraped content.

- `scripts/processors/api/process_bigquery_api.py`: Process BigQuery API documentation
- `scripts/processors/api/process_looker_api.py`: Process Looker API documentation
- `scripts/processors/api/process_storage_api.py`: Process Google Cloud Storage API documentation

### Utils

Utility scripts for various tasks.

- `scripts/utils/combine_api_docs.py`: Combine API documentation from multiple products
- `scripts/utils/extract_looker_models.py`: Extract model properties from Looker API documentation

### Upload

Scripts for uploading content to GS buckets and data stores.

- `scripts/upload/upload_to_bucket.py`: Upload content to GS buckets
- `scripts/upload/upload_to_datastore.py`: Upload content to data stores

## Configuration

Configuration files for the repository.

- `config/bucket_mappings.json`: Mapping of products to GS buckets
- `config/datastore_mappings.json`: Mapping of products to data stores

## Usage

### Scraping Content

To scrape API documentation for a product:

```bash
cd scripts/scrapers/api
python3 scrape_<product>_api.py
```

### Processing Content

To process API documentation for a product:

```bash
cd scripts/processors/api
python3 process_<product>_api.py
```

### Uploading Content

To upload content to a GS bucket:

```bash
cd scripts/upload
python3 upload_to_bucket.py --product <product> --content-type <content_type> --source-type <source_type>
```

To upload content to a data store:

```bash
cd scripts/upload
python3 upload_to_datastore.py --product <product> --content-type <content_type> --source-type <source_type>
```

## Examples

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

# Upload processed BigQuery API documentation to data store
python3 upload_to_datastore.py --product bigquery --content-type api --source-type processed
```

