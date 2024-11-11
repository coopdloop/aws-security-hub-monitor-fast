#!/bin/bash
set -e

# Configuration
REGION=${AWS_REGION:-"us-east-1"}
ENVIRONMENT=${ENVIRONMENT:-"production"}

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo "Deploying AWS Security Monitor to ${ENVIRONMENT}..."

# Check AWS credentials
if ! aws sts get-caller-identity > /dev/null 2>&1; then
    echo -e "${RED}Error: AWS credentials not configured${NC}"
    exit 1
fi

# Deploy Terraform
cd terraform
terraform init
terraform validate
terraform plan -var="environment=${ENVIRONMENT}" -out=tfplan
terraform apply tfplan

echo -e "${GREEN}Deployment completed successfully!${NC}"
