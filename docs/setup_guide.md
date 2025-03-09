# HBIA2 Setup Guide

This document provides instructions for setting up the HBIA2 repository.

## Prerequisites

Before setting up the HBIA2 repository, ensure that you have the following prerequisites:

1. **Python 3.9+**: The repository requires Python 3.9 or later.
2. **Google Cloud SDK**: The repository requires the Google Cloud SDK for uploading content to Google Cloud Storage buckets and datastores.
3. **Git**: The repository requires Git for version control.

## Installation

To install the HBIA2 repository, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hbia2.git
   cd hbia2
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The repository requires the following configuration:

1. **Bucket Mappings**: Configure the mapping of products to Google Cloud Storage buckets in `config/bucket_mappings.json`.
2. **Datastore Mappings**: Configure the mapping of products to datastores in `config/datastore_mappings.json`.

### Bucket Mappings

The `config/bucket_mappings.json` file maps products to Google Cloud Storage buckets. The file should have the following format:

```json
{
  "bigquery": "gs://bigquery-docs",
  "looker": "gs://looker-docs",
  "looker-studio": "gs://looker-studio-docs",
  "gcp": "gs://gcp-docs",
  "dbt": "gs://dbt-docs",
  "omni": "gs://omni-docs"
}
```

### Datastore Mappings

The `config/datastore_mappings.json` file maps products to datastores. The file should have the following format:

```json
{
  "bigquery": "bigquery-datastore",
  "looker": "looker-datastore",
  "looker-studio": "looker-studio-datastore",
  "gcp": "gcp-datastore",
  "dbt": "dbt-datastore",
  "omni": "omni-datastore"
}
```

## Directory Structure

The repository has the following directory structure:

```
/hbia2/
├── scripts/                           # All scripts organized by function
│   ├── scrapers/                      # Scripts for scraping content
│   ├── processors/                    # Scripts for processing content
│   ├── utils/                         # Utility scripts
│   └── upload/                        # Scripts for uploading to GS buckets and datastores
├── data/                              # All data (scraped and processed)
│   ├── bigquery/                      # BigQuery product data
│   ├── looker/                        # Looker product data
│   ├── looker-studio/                 # Looker Studio product data
│   ├── gcp/                           # GCP product data
│   ├── dbt/                           # dbt product data
│   ├── omni/                          # Omni product data
│   └── combined/                      # Combined data across products
├── config/                            # Configuration files
│   ├── bucket_mappings.json           # Mapping of products to GS buckets
│   └── datastore_mappings.json        # Mapping of products to datastores
├── docs/                              # Project documentation
└── README.md                          # Repository documentation
```

## Next Steps

After setting up the repository, you can proceed to the [Usage Guide](usage_guide.md) for instructions on how to use the repository. 