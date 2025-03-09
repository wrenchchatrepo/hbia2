# Repository Reorganization Plan

## Overview

This directory contains files related to reorganizing the HBIA2 repository into a more maintainable structure with six top-level product directories.

## Files

- **structure.md**: Detailed description of the new directory structure
- **reorganize.py**: Python script to execute the reorganization

## How to Use

### 1. Prepare for Reorganization

Before running the full reorganization, you can:

- Review the proposed structure in `structure.md`
- Create the directory structure without moving files:
  ```bash
  python3 reorganize.py --simulate
  ```
- Test the reorganization with dry-run mode to see what would happen:
  ```bash
  python3 reorganize.py --dry-run
  ```

### 2. Execute the Reorganization

When ready, run the script without any flags to perform the actual reorganization:

```bash
python3 reorganize.py
```

This will:
1. Create the new directory structure if it doesn't exist
2. Move files from various sources to their appropriate product directories
3. Archive duplicate TXT files when MD versions exist
4. Organize scripts into logical categories

### 3. Update References

After reorganization, you'll need to:

1. Update references in scripts to point to the new file locations
2. Update any documentation that references file paths
3. Clean up empty directories that are no longer needed

## Expected Results

The reorganization will result in:

- Six top-level product directories (bigquery, looker, dbt, gcp, omni, looker-studio)
- Files organized by product and content type (api, docs, github)
- Duplicate .txt files archived when .md versions exist
- Scripts organized into logical categories

## Validation

After running the script, verify:

1. All content is accessible in the new structure
2. No essential files were missed
3. Scripts and other tools still work with the new structure

## Rollback Plan

If issues arise, you can:

1. Use Git to revert changes if the reorganization was committed
2. Manually move files back to their original locations using the log output
3. Run a modified version of the script to reverse the changes

## Next Steps

After successful reorganization:

1. Update the project_checklist.md with the new structure
2. Update any scripts that reference the old paths
3. Update documentation to reflect the new organization 