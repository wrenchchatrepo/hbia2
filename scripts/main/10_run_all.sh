#!/bin/bash

# 10_run_all.sh
# Master script to run all scripts in sequence

# Exit on error
set -e

echo "=== Vertex AI Agent Builder: Running All Scripts ==="

# Function to run a script and check its exit status
run_script() {
    local script="$1"
    echo ""
    echo "========================================================"
    echo "Running $script..."
    echo "========================================================"
    
    if [ -f "$script" ]; then
        chmod +x "$script"
        "$script"
        local status=$?
        if [ $status -ne 0 ]; then
            echo "ERROR: Script $script failed with exit code $status"
            exit $status
        fi
    else
        echo "ERROR: Script $script not found"
        exit 1
    fi
}

# Get the directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Make all scripts executable
echo "Making all scripts executable..."
find "$PROJECT_ROOT/scripts" -name "*.sh" -exec chmod +x {} \;

# Run each script in sequence
run_script "$PROJECT_ROOT/scripts/main/01_setup_environment.sh"
run_script "$PROJECT_ROOT/scripts/main/02_setup_directory_structure.sh"
run_script "$PROJECT_ROOT/scripts/setup/03_download_documentation.sh"
run_script "$PROJECT_ROOT/scripts/setup/04_create_buckets.sh"
run_script "$PROJECT_ROOT/scripts/setup/05_upload_to_buckets.sh"
run_script "$PROJECT_ROOT/scripts/setup/06_create_datastores.sh"
run_script "$PROJECT_ROOT/scripts/setup/07_create_agents.sh"
run_script "$PROJECT_ROOT/scripts/update/08_update_datastores.sh"

# Ask if user wants to run Git operations
echo ""
read -p "Do you want to run Git operations now? (y/n): " run_git
if [[ $run_git == "y" || $run_git == "Y" ]]; then
    run_script "$PROJECT_ROOT/scripts/main/09_git_operations.sh"
fi

echo ""
echo "=== All scripts completed successfully ==="
echo "Your Vertex AI Agent Builder environment is now set up!" 