# Vertex AI Agent Builder

A comprehensive framework for building, deploying, and managing intelligent agents using Google Cloud's Vertex AI.

## Overview

This repository contains all the necessary components to set up a suite of specialized AI agents using Google Cloud's Vertex AI. The agents are designed to provide expert assistance in various domains including Looker, BigQuery, DBT, GCP architecture, Omni, and Looker Studio.

## Features

- **Multiple Specialized Agents**: Domain-specific assistants for Looker, BigQuery, DBT, GCP, Omni, and Looker Studio
- **Automated Setup**: Scripts to automate the entire setup process
- **Documentation Integration**: Automatically downloads and processes relevant documentation
- **Repository Integration**: Flattens and processes GitHub repositories for knowledge ingestion
- **Slack Integration**: Connect your agents to Slack for team collaboration
- **Centralized Configuration**: Easy-to-manage configuration files

## Prerequisites

- Google Cloud Platform account with billing enabled
- `gcloud` CLI installed and configured
- `gsutil` installed
- `git` installed
- `wget` installed
- Bash shell environment

## Quick Start

1. Clone this repository:
```bash
   git clone https://github.com/wrenchchatrepo/hbia2.git
   cd hbia2
   ```

2. Fill in the required values in the `.env` file:
   ```bash
   cp .env.example .env
   # Edit .env with your specific values
   ```

3. Run the setup script:
```bash
   chmod +x setup_vertex_agent.sh
   ./setup_vertex_agent.sh
   ```

4. Follow the prompts to complete the setup.

## Project Structure

```
.
├── .env                           # Environment variables (create from .env.example)
├── vertex_config.yaml             # Main configuration file
├── setup_vertex_agent.sh          # Main setup script
├── flatten_repos.sh               # Script to process GitHub repositories
├── download_docs.sh               # Script to download documentation
├── repos.md                       # List of repositories to process
├── scripts/
│   ├── setup/
│   │   ├── create_datastores.sh   # Script to create Vertex AI datastores
│   │   └── create_agents.sh       # Script to create Vertex AI agents
│   └── update/
│       └── update_datastores.sh   # Script to update datastores
└── datastores/                    # Directory for downloaded documentation
    ├── looker/
    ├── bigquery/
    ├── dbt/
    ├── gcp/
    ├── omni/
    └── lookerstudio/
```

## Configuration

### Environment Variables (.env)

The `.env` file contains sensitive information and configuration parameters:

- Project information (ID, region)
- API keys
- Storage bucket names
- Slack integration details
- Agent configuration parameters

### Main Configuration (vertex_config.yaml)

The `vertex_config.yaml` file defines the structure of your Vertex AI agents:

- Organization information
- Google Cloud project details
- Storage configuration
- Agent definitions
- Integration settings
- Code interpreter settings

## Setup Process

The setup process consists of several steps:

1. **Environment Setup**: Configuring Google Cloud project and enabling APIs
2. **Infrastructure Creation**: Creating storage buckets and directory structure
3. **Data Collection**: Downloading documentation and processing GitHub repositories
4. **Datastore Creation**: Setting up Vertex AI datastores
5. **Agent Creation**: Creating and configuring Vertex AI agents
6. **Integration**: Setting up Slack integration (optional)

## Maintenance

### Updating Datastores

To update the content in your datastores:

```bash
./scripts/update/update_datastores.sh
```

### Adding New Repositories

1. Edit the `repos.md` file to add new GitHub repositories
2. Run the repository flattening script:
   ```bash
   ./flatten_repos.sh
   ```
3. Update the datastores:
   ```bash
   ./scripts/update/update_datastores.sh
   ```

## Slack Integration

To integrate your agents with Slack:

1. Create a Slack app in the [Slack API Console](https://api.slack.com/apps)
2. Enable webhooks and generate tokens
3. Update the `.env` file with your Slack credentials
4. Configure the channels in `vertex_config.yaml`

## Security Considerations

- Keep your `.env` file secure and never commit it to version control
- Use service accounts with minimal required permissions
- Regularly rotate API keys and tokens
- Monitor usage to detect any unauthorized access

## Troubleshooting

### Common Issues

- **API Quota Exceeded**: Increase your quota limits in Google Cloud Console
- **Permission Denied**: Check IAM permissions for your service account
- **Datastore Update Failures**: Ensure your bucket has the correct files and format

### Logs

Check the following logs for troubleshooting:

- `flatten_repos.log`: Repository processing logs
- Google Cloud Logging: For Vertex AI related issues

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Cloud Vertex AI team for the powerful agent platform
- The open-source community for valuable tools and libraries

