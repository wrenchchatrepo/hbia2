# Troubleshooting Guide

This document provides solutions to common issues encountered when setting up and using the Vertex AI Agent Builder framework.

## Directory Structure Issues

### Issue: Inconsistent Directory Naming

**Problem:** We encountered issues with inconsistent directory naming, specifically with `looker_studio` vs `lookerstudio`.

**Solution:**
- Always use underscores instead of spaces in directory names
- Standardize on `looker_studio` with an underscore
- If you find both directories exist, use this command to consolidate:
  ```bash
  # Move unique files from lookerstudio to looker_studio
  find ./datastores/lookerstudio -type f | while read file; do
    filename=$(basename "$file")
    if [ ! -f "./datastores/looker_studio/$filename" ]; then
      cp "$file" "./datastores/looker_studio/"
    fi
  done
  
  # Remove the duplicate directory
  rm -rf ./datastores/lookerstudio
  ```

### Issue: Missing Directories

**Problem:** Scripts fail because expected directories don't exist.

**Solution:**
- Always run the directory structure setup script first:
  ```bash
  ./scripts/main/02_setup_directory_structure.sh
  ```
- Verify directory structure before running other scripts:
  ```bash
  find . -type d -not -path "*/\.*" | sort
  ```

## Script Organization Issues

### Issue: Duplicate Scripts in Different Locations

**Problem:** We had duplicate scripts with different versions in multiple locations, causing confusion about which one to use.

**Solution:**
- Organize scripts by function in the `scripts/` directory:
  - `main/`: Core operational scripts
  - `setup/`: Scripts for setting up resources
  - `update/`: Scripts for updating resources
- Use a consistent numbering scheme for scripts to indicate execution order
- Move non-working scripts to a `garbage/` directory (which is git-ignored)
- Use the master script (`scripts/main/10_run_all.sh`) to run all scripts in sequence

### Issue: Script Execution Permissions

**Problem:** Scripts fail to execute due to missing execution permissions.

**Solution:**
- Make all scripts executable before running:
  ```bash
  find scripts -name "*.sh" -exec chmod +x {} \;
  ```
- Always check if a script is executable before running it:
  ```bash
  if [ ! -x "script.sh" ]; then
    chmod +x script.sh
  fi
  ```

## Environment Configuration Issues

### Issue: Missing Environment Variables

**Problem:** Scripts fail because environment variables are not set.

**Solution:**
- Always source the `.env` file at the beginning of your scripts:
  ```bash
  # Source environment variables
  if [ -f .env ]; then
    source .env
  else
    echo "Error: .env file not found"
    exit 1
  fi
  ```
- Verify that all required variables are set:
  ```bash
  required_vars=("PROJECT_ID" "REGION" "BUCKET_BASE")
  for var in "${required_vars[@]}"; do
    if [ -z "${!var}" ]; then
      echo "Error: $var is not set in .env file"
      exit 1
    fi
  done
  ```

## Google Cloud Issues

### Issue: Datastore Creation Failures

**Problem:** Datastore creation fails due to missing buckets or incorrect permissions.

**Solution:**
- Ensure buckets are created before creating datastores:
  ```bash
  ./scripts/setup/04_create_buckets.sh
  ```
- Verify bucket existence before creating datastores:
  ```bash
  gsutil ls | grep "${BUCKET_BASE}"
  ```
- Check IAM permissions for your service account:
  ```bash
  gcloud projects get-iam-policy ${PROJECT_ID} \
    --flatten="bindings[].members" \
    --format="table(bindings.role,bindings.members)" \
    --filter="bindings.members:serviceAccount"
  ```

### Issue: Agent Creation Failures

**Problem:** Agent creation fails due to missing datastores or incorrect configuration.

**Solution:**
- Ensure datastores are created before creating agents:
  ```bash
  ./scripts/setup/06_create_datastores.sh
  ```
- Verify datastore existence before creating agents:
  ```bash
  gcloud ai datastores list --region=${REGION}
  ```
- Check agent configuration in `vertex_config.yaml` for correctness

## Path Resolution Issues

### Issue: Relative Path Problems

**Problem:** Scripts fail because they're run from different directories, causing relative path issues.

**Solution:**
- Use absolute paths in scripts:
  ```bash
  # Get the directory of the script
  SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
  
  # Use absolute paths
  source "${PROJECT_ROOT}/.env"
  ```
- Always change to the project root directory before running scripts:
  ```bash
  cd "$(git rev-parse --show-toplevel)" || exit 1
  ```

## Documentation Issues

### Issue: Missing or Outdated Documentation

**Problem:** Documentation doesn't match the actual directory structure or script organization.

**Solution:**
- Keep README.md updated with the current directory structure
- Document script organization and execution order
- Add comments to scripts explaining their purpose and usage
- Create a TROUBLESHOOTING.md file (like this one) to document common issues and solutions

## Git Issues

### Issue: Committing Sensitive Information

**Problem:** Accidentally committing sensitive information like API keys.

**Solution:**
- Always use `.env` for sensitive information and ensure it's in `.gitignore`
- Use `.env.example` as a template with placeholder values
- Check what will be committed before committing:
  ```bash
  git diff --cached
  ```
- If sensitive information is accidentally committed, use:
  ```bash
  git filter-branch --force --index-filter \
    "git rm --cached --ignore-unmatch .env" \
    --prune-empty --tag-name-filter cat -- --all
  ```

## Conclusion

By following the guidelines in this troubleshooting guide, you can avoid the common issues we encountered when setting up and using the Vertex AI Agent Builder framework. If you encounter additional issues, please document them here to help others. 