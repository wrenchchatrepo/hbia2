# Repository Reorganization Plan

## New Top-Level Structure

```
/hbia2/
├── bigquery/                       # BigQuery product directory
│   ├── api/                        # API documentation
│   │   ├── scraped/                # Scraped API content
│   │   └── processed/              # Processed API content
│   ├── docs/                       # General documentation
│   │   ├── scraped/                # Scraped docs content
│   │   └── processed/              # Processed docs content
│   └── github/                     # GitHub repository content
│       ├── scraped/                # Scraped GitHub content
│       └── processed/              # Processed GitHub content
│
├── looker/                         # Looker product directory
│   ├── api/                        # Same structure as above
│   ├── docs/
│   └── github/
│
├── dbt/                            # DBT product directory
│   ├── api/
│   ├── docs/
│   └── github/
│
├── gcp/                            # GCP product directory
│   ├── api/
│   ├── docs/
│   └── github/
│
├── omni/                           # Omni product directory
│   ├── api/
│   ├── docs/
│   └── github/
│
├── looker-studio/                  # Looker Studio product directory
│   ├── api/
│   ├── docs/
│   └── github/
│
├── archive/                        # Archive directory
│   ├── bigquery/                   # Archive for BigQuery
│   ├── looker/                     # Archive for Looker
│   ├── dbt/                        # Archive for DBT
│   ├── gcp/                        # Archive for GCP
│   ├── omni/                       # Archive for Omni
│   └── looker-studio/              # Archive for Looker Studio
│
├── scripts/                        # All scripts
│   ├── main/                       # Main operational scripts
│   ├── processors/                 # Content processing scripts
│   ├── scrapers/                   # Content scraping scripts
│   ├── setup/                      # Setup scripts
│   ├── update/                     # Update scripts
│   └── utils/                      # Utility scripts
│
├── config/                         # Configuration files
├── docs/                           # Project documentation
└── utils/                          # Utilities that aren't scripts
```

## Migration Approach

1. Create the new directory structure
2. For each product (bigquery, looker, dbt, gcp, omni, looker-studio):
   - Move all files from `scraped_content` that match the product into the appropriate product directory
   - Move all files from `scraped_docs` that match the product into the appropriate product directory
   - Move all files from `temp_docs` that match the product into the appropriate product directory
   - Move all files from other locations that match the product into the appropriate product directory
   - If both MD and TXT versions of the same file exist, move the MD file to the main directory and the TXT file to the archive

3. Organize scripts into logical categories in the scripts directory

4. Update references in scripts to point to the new file locations

5. Update documentation to reflect the new structure

## Special Cases

- The `cloud.google.com` directory content will be distributed into the appropriate product directories
- Content in `data/[product]` will be moved to the top-level product directories
- Scripts in `scripts/data` will be consolidated

## Old Directories to Remove After Migration

- `/scraped_content`
- `/scraped_docs`
- `/temp_docs`
- `/cloud.google.com`
- `/data/[product]` (after contents are moved) 