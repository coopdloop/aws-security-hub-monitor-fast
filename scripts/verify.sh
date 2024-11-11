#!/bin/bash
set -e

# Configuration
REGION=${AWS_REGION:-"us-east-1"}

echo "Verifying AWS Security Monitor deployment..."

# Check Security Hub
echo "Checking Security Hub..."
aws securityhub get-enabled-standards

# Check AWS Config
echo "Checking AWS Config..."
aws configservice describe-configuration-recorder-status

# Check findings
echo "Checking Security Hub findings..."
aws securityhub get-findings --filter '{"RecordState":[{"Value":"ACTIVE","Comparison":"EQUALS"}]}'
