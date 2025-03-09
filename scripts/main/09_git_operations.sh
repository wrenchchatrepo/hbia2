#!/bin/bash

# 08_git_operations.sh
# Handles Git operations for the project

# Exit on error
set -e

echo "=== Git Operations ==="

# Function to check Git status
check_git_status() {
    echo "Checking Git status..."
    git status
}

# Function to add all changes
add_all_changes() {
    echo "Adding all changes to Git..."
    git add .
    echo "Changes added."
}

# Function to commit changes
commit_changes() {
    local message="$1"
    if [ -z "$message" ]; then
        read -p "Enter commit message: " message
    fi
    
    echo "Committing changes with message: '$message'..."
    git commit -m "$message"
    echo "Changes committed."
}

# Function to push changes
push_changes() {
    echo "Pushing changes to remote repository..."
    git push -u origin main
    echo "Changes pushed."
}

# Main menu
show_menu() {
    echo ""
    echo "Git Operations Menu:"
    echo "1. Check status"
    echo "2. Add all changes"
    echo "3. Commit changes"
    echo "4. Push changes"
    echo "5. Complete workflow (add, commit, push)"
    echo "6. Exit"
    echo ""
    read -p "Enter your choice (1-6): " choice
    
    case $choice in
        1) check_git_status; show_menu ;;
        2) add_all_changes; show_menu ;;
        3) commit_changes; show_menu ;;
        4) push_changes; show_menu ;;
        5) 
            add_all_changes
            commit_changes
            push_changes
            show_menu
            ;;
        6) echo "Exiting Git operations."; exit 0 ;;
        *) echo "Invalid choice. Please try again."; show_menu ;;
    esac
}

# Start the menu
show_menu

echo "=== Git operations completed ===" 