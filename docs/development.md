# Development Guide

## Setup Development Environment

### 1. Prerequisites
- Python 3.8+
- Node.js 14+
- Terraform 1.0+
- AWS CLI v2

### 2. Local Development
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements-dev.txt
```

## Testing

### 1. Unit Tests
```bash
# Run Python tests
pytest tests/python/

# Run Terraform tests
cd tests/terraform
go test -v
```

### 2. Integration Tests
```bash
# Deploy test environment
./scripts/deploy.sh test

# Run integration tests
pytest tests/integration/
```

## Code Quality

### 1. Linting
```bash
# Python
flake8 lambda/
black lambda/

# Terraform
terraform fmt
tflint
```

### 2. Security Scanning
```bash
# Python dependencies
safety check

# Infrastructure
checkov -d terraform/
tfsec terraform/
