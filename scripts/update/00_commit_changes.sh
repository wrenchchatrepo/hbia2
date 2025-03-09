#!/bin/bash

# Exit on error
set -e

echo "=== Preparing Repository for Commit ==="

# Make sure all scripts are executable
echo "Making all scripts executable..."
find scripts -name "*.sh" -exec chmod +x {} \;

# Check if there are any remaining temporary files
echo "Checking for temporary files..."
temp_files=$(find . -maxdepth 1 -name "*.sh" -not -name "commit_changes.sh" | grep -v "scripts/")
if [ -n "$temp_files" ]; then
    echo "Warning: Found temporary script files in the root directory:"
    echo "$temp_files"
    read -p "Do you want to move these to the garbage directory? (y/n): " move_temp
    if [[ $move_temp == "y" || $move_temp == "Y" ]]; then
        mkdir -p garbage/temp
        for file in $temp_files; do
            mv "$file" garbage/temp/
            echo "Moved $file to garbage/temp/"
        done
    fi
fi

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

# Show git status
echo ""
echo "Current Git Status:"
git status

# Ask to add files
echo ""
read -p "Do you want to add all changes to Git? (y/n): " add_all
if [[ $add_all == "y" || $add_all == "Y" ]]; then
    git add .
    echo "All changes added to Git."
    
    # Ask for commit message
    echo ""
    read -p "Enter commit message (default: 'Reorganized scripts and directory structure'): " commit_msg
    commit_msg=${commit_msg:-"Reorganized scripts and directory structure"}
    
    # Commit changes
    git commit -m "$commit_msg"
    echo "Changes committed with message: '$commit_msg'"
    
    # Ask to push
    echo ""
    read -p "Do you want to push changes to remote repository? (y/n): " push_changes
    if [[ $push_changes == "y" || $push_changes == "Y" ]]; then
        git push origin main
        echo "Changes pushed to remote repository."
    else
        echo "Changes not pushed. You can push later with: git push origin main"
    fi
else
    echo "Changes not added to Git. You can add them later with: git add ."
fi

echo ""
echo "=== Repository preparation complete ===" 