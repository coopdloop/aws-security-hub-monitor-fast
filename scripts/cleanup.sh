#!/bin/bash
set -e

echo "Cleaning up AWS Security Monitor resources..."

# Disable Security Hub
aws securityhub disable-security-hub

# Stop AWS Config recorder
CONFIG_RECORDER=$(aws configservice describe-configuration-recorders --query 'ConfigurationRecorders[0].name' --output text)
aws configservice stop-configuration-recorder --configuration-recorder-name $CONFIG_RECORDER

# Destroy Terraform resources
cd terraform
terraform destroy -auto-approve

echo "Cleanup completed successfully!"
