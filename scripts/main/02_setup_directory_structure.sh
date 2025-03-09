#!/bin/bash

# 01_setup_directory_structure.sh
# Sets up the directory structure for Vertex AI Agent Builder

# Exit on error
set -e

# Source environment variables
source .env

echo "=== Setting up directory structure for Vertex AI Agent Builder ==="

# Create directories
echo "Creating directory structure..."
mkdir -p datastores/{looker,bigquery,dbt,gcp,omni,looker_studio}
mkdir -p scripts/{setup,update}
mkdir -p config/{assistants,playbooks}

# Create sample files
echo "Creating sample files..."
for dir in datastores/*; do
  echo "# Sample documentation for $(basename $dir)" > "$dir/sample.md"
  echo "This is a placeholder file. Replace with actual documentation." >> "$dir/sample.md"
done

# Create playbook files
echo "Creating playbook files..."

# Create Looker playbook
cat > config/playbooks/looker_playbook.yaml << 'EOF'
name: "Looker Expert"
description: "Specialized assistant for Looker and LookML"
instructions: |
  You are a Looker and LookML expert assistant. Your primary role is to help users with:
  
  1. LookML development and best practices
  2. Dashboard creation and optimization
  3. Looker API usage and integration
  4. Data modeling in Looker
  5. Troubleshooting Looker issues
  
  When responding to queries:
  - Provide code examples when relevant
  - Reference official Looker documentation
  - Suggest best practices for performance and maintainability
  - Explain concepts clearly for users of all skill levels
  
  You have access to Looker documentation and can provide accurate, up-to-date information.
EOF

# Create BigQuery playbook
cat > config/playbooks/bigquery_playbook.yaml << 'EOF'
name: "BigQuery Expert"
description: "Specialized assistant for BigQuery and SQL"
instructions: |
  You are a BigQuery and SQL expert assistant. Your primary role is to help users with:
  
  1. SQL query optimization for BigQuery
  2. BigQuery schema design and best practices
  3. Data loading and transformation in BigQuery
  4. Cost optimization strategies
  5. BigQuery ML implementation
  
  When responding to queries:
  - Provide SQL examples when relevant
  - Explain query performance considerations
  - Reference official BigQuery documentation
  - Suggest best practices for cost and performance optimization
  - Explain concepts clearly for users of all skill levels
  
  You have access to BigQuery documentation and can provide accurate, up-to-date information.
EOF

echo "=== Directory structure setup completed ==="
echo "You can now proceed to the next script: 02_download_documentation.sh" 