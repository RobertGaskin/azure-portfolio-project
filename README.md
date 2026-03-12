#This project demonstrates deploying Azure infrastructure using Bicep Infrastructure as Code. The goal of the project is to automate Azure resource deployment using reusable templates and parameterized configurations.

The environment was deployed and tested using Azure CLI and GitHub version control to simulate a real cloud engineering workflow.

⸻

Architecture Overview

The deployment provisions a basic Azure environment that includes:

• Azure Virtual Network
• Subnet configuration
• Network Security Groups
• Azure Virtual Machine deployment
• Parameterized infrastructure configuration
• Infrastructure deployment through Bicep templates

This project demonstrates how cloud infrastructure can be automated and deployed consistently across environments.

⸻

Technologies Used

• Microsoft Azure
• Azure CLI
• Bicep Infrastructure as Code
• GitHub
• Virtual Machines
• Networking configuration

⸻

Virtual Machine Deployment

A Windows Virtual Machine was deployed as part of the infrastructure build to simulate a real workload running in Azure.

The VM was created using Bicep templates and deployed through Azure CLI.

VM configuration included

• Secure admin credentials through parameters
• Virtual network connectivity
• Subnet integration
• Network security rules
• Public IP configuration

This demonstrates automated infrastructure provisioning and cloud environment setup.

⸻

Deployment Method

Infrastructure was deployed using the Azure CLI with the following command structure:
az deployment group create \
--resource-group rg-azure-portfolio \
--template-file main.bicep \
--parameters main.parameters.json
This deployment method enables repeatable infrastructure provisioning using Infrastructure as Code practices.
⸻

Planned improvements include

• Azure Key Vault integration
• CI CD pipeline deployment through GitHub Actions
• Azure Monitor and logging integration
• Additional networking security controls
• Automated scaling configurations


