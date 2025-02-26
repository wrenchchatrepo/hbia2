# Repository Flattener

A bash script that clones multiple GitHub repositories from a markdown file, flattens their directory structure, and consolidates all files into a single directory while handling duplicates and filtering unnecessary files.

## Overview

This tool is particularly useful when you need to:
- Aggregate files from multiple repositories
- Create a consolidated codebase for analysis
- Prepare files for ingestion into AI/ML training
- Build documentation databases
- Create searchable code archives

## Prerequisites

- Bash shell environment
- Git installed and configured
- Sufficient disk space for repository cloning
- Read access to the GitHub repositories
- Write access to the local directory

## Installation

1. Clone or download the script:
```bash
curl -O https://raw.githubusercontent.com/your-repo/flatten_repos.sh
```
2. Make the script executable:
```bash
chmod +x flatten_repos.sh
```

## Usage

1. Create a markdown file (repos.md) containing GitHub repository URLs:
```yaml
# Repository List

## Category 1
- https://github.com/org1/repo1
- https://github.com/org1/repo2

## Category 2
- https://github.com/org2/repo1
```
2. Run the script:
```yaml
./flatten_repos.sh
```

## Directory Structure

.
├── flatten_repos.sh  # Main script
├── repos.md          # Input file with repository URLs
├── flattened_repos/  # Output directory containing all files
├── temp_repos/       # Temp directory, deleted post processing
└── flatten_repos.log # Detailed log file

## File Naming Convention

### Files in the output directory follow this naming pattern:

`repository-name_original-path_filename.ext`

#### For duplicate filenames, a number is appended:
```
repository-name_original-path_filename_1.ext
repository-name_original-path_filename_2.ext
```

## Excluded Files

### File Types
- .pyc, .pyo, .pyd
- .so, .dll, .dylib
- .log, .cache
- .DS_Store
- __pycache__
- .ipynb_checkpoints
### Common Files
- LICENSE
- README.md
- CHANGELOG.md
- CONTRIBUTING.md
- Dockerfile
- requirements.txt
- setup.py
- package.json
- .gitignore
- .env

## Configuration

You can modify the excluded files and extensions by editing these arrays in the script:
```
EXCLUDE_FILES=(
    "license"
    "readme.md"
    # Add more files...
)

EXCLUDE_EXTENSIONS=(
    ".pyc"
    ".pyo"
    # Add more extensions...
)
```

## Logging

### The script generates a detailed log file (flatten_repos.log) containing:
+ Start and end timestamps
+ Successfully cloned repositories
+ Processed and excluded files
+ Error messages
+ Summary statistics

### Example log output:

```log
Repository flattening process started at Wed Feb 25 07:15:15 CST 2025
Processing repository: https://github.com/org1/repo1
Successfully cloned https://github.com/org1/repo1
Copied: /path/to/file.py -> flattened_repos/org1_repo1_src_file.py
...
Process Summary:
Total repositories processed: 10
Total files in output directory: 1500
Process completed at Wed Feb 25 07:20:15 CST 2025
```

## Error Handling

### The script handles common errors:
+ Failed repository clones
+ File access permissions
+ Duplicate filenames
+ Invalid repository URLs

## Performance

+ Uses shallow cloning (--depth 1) to minimize download size
+ Processes files in a single pass
+ Cleans up temporary files automatically
+ Early filtering of excluded files

## Limitations

+ Requires direct GitHub URLs
+ Does not handle private repositories requiring authentication
+ May require significant disk space for large repositories
+ File names are modified to ensure uniqueness





