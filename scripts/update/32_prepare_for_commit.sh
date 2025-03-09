#!/bin/bash

# Exit on error
set -e

echo "=== Preparing Repository for Commit ==="

# Remove temporary files and directories
echo "Removing temporary files and directories..."
rm -rf scripts_backup
rm -rf scripts_new
rm -rf scripts_organized
rm -f rename_scripts.sh
rm -f organize_scripts.sh
rm -f organize_scripts_final.sh
rm -f clean_numbering.sh
rm -f cleanup_duplicates.sh
rm -f final_cleanup.sh
rm -f finalize_scripts.sh
rm -f restore_structure.sh
rm -f run_all.sh

# Remove old shell directory if it exists
if [ -d "shell" ]; then
    echo "Removing old shell directory..."
    rm -rf shell
fi

# Remove old scripts
echo "Removing old script files..."
rm -f Datastore_Update.sh
rm -f Datastore_Update_2.sh
rm -f clone_and_flatten_repos.sh
rm -f download_docs.sh
rm -f flatten_repos.sh
rm -f setup_vertex_agent.sh

# Update .gitignore
echo "Updating .gitignore..."
if ! grep -q "^garbage/" .gitignore; then
    echo "garbage/" >> .gitignore
fi
if ! grep -q "^google-cloud-sdk/" .gitignore; then
    echo "google-cloud-sdk/" >> .gitignore
fi
if ! grep -q "^*.pdf" .gitignore; then
    echo "*.pdf" >> .gitignore
fi

# Make all scripts executable
echo "Making all scripts executable..."
find scripts -name "*.sh" -exec chmod +x {} \;

echo "=== Repository is now ready for commit ==="
echo "You can now run the following commands to commit your changes:"
echo "git add ."
echo "git commit -m \"Reorganized scripts and directory structure\""
echo "git push origin main" 