# Terraform Setup

This directory contains Terraform scripts for setting up the infrastructure.

## Structure
- `dev/`: Development environment setup
- `staging/`: Staging environment setup
- `prod/`: Production environment setup
- `main.tf`: Main Terraform script
- `variables.tf`: Configurable variables
- `outputs.tf`: Terraform outputs

## Instructions
1. Update `variables.tf` with your environment details.
2. Run the following commands to provision resources:
   ```sh
   terraform init
   terraform plan
   terraform apply