# Scripts Directory

This directory contains all the working scripts for the Vertex AI Agent Builder project, organized by function.

## Directory Structure

- **main/** - Core operational scripts
  - `01_setup_environment.sh` - Sets up the environment variables and Google Cloud configuration
  - `02_setup_directory_structure.sh` - Creates the necessary directory structure for the project
  - `09_git_operations.sh` - Handles Git operations like committing and pushing changes
  - `10_run_all.sh` - Master script that runs all the necessary scripts in sequence

- **setup/** - Scripts for setting up datastores, agents, and other resources
  - `03_download_documentation.sh` - Downloads documentation from various sources
  - `04_create_buckets.sh` - Creates Google Cloud Storage buckets
  - `05_upload_to_buckets.sh` - Uploads files to Google Cloud Storage buckets
  - `06_create_datastores.sh` - Creates Vertex AI datastores
  - `07_create_agents.sh` - Creates Vertex AI agents
  - `29_create_agents.sh` - Alternative version of agent creation script
  - `30_create_datastores.sh` - Alternative version of datastore creation script

- **update/** - Scripts for updating datastores and other resources
  - `08_update_datastores.sh` - Updates Vertex AI datastores with new content
  - `31_update_datastores.sh` - Alternative version of datastore update script

## Usage

1. Start with the environment setup script:
   ```
   ./main/01_setup_environment.sh
   ```

2. Create the directory structure:
   ```
   ./main/02_setup_directory_structure.sh
   ```

3. Run the setup scripts in sequence:
   ```
   ./setup/03_download_documentation.sh
   ./setup/04_create_buckets.sh
   ./setup/05_upload_to_buckets.sh
   ./setup/06_create_datastores.sh
   ./setup/07_create_agents.sh
   ```

4. Update datastores as needed:
   ```
   ./update/08_update_datastores.sh
   ```

5. Alternatively, use the master script to run all steps in sequence:
   ```
   ./main/10_run_all.sh
   ```

## Notes

- All scripts are designed to be idempotent - they can be run multiple times without causing issues.
- Scripts will check for prerequisites and dependencies before executing.
- For simulation purposes, some scripts may not perform actual operations but will display the expected output.
- Alternative versions of scripts are provided for different use cases or implementation approaches.
