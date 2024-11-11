# AWS Security Hub Monitor 🛡️

![Security Monitor Banner](https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg)

## Overview

The AWS Security Hub Monitor is a comprehensive security monitoring solution that integrates AWS Security Hub, AWS Config, and CloudTrail to provide real-time security monitoring, compliance assessment, and automated incident response for your AWS infrastructure.

### Key Features 🌟

- **Automated Security Monitoring**: Real-time detection of security issues and compliance violations
- **Compliance Tracking**: Built-in support for AWS Security Best Practices
- **Audit Logging**: Comprehensive CloudTrail integration
- **Automated Alerting**: Real-time notifications for critical security findings
- **Infrastructure as Code**: Complete Terraform configurations

## Project Structure 📁

```
aws-security-hub-monitor/
├── src/
│   └── security_monitor/
│       ├── __init__.py          # Package initialization
│       ├── handler.py           # Lambda handler implementation
│       └── utils.py             # Utility functions
├── terraform/
│   ├── main.tf                  # Main Terraform configuration
│   ├── variables.tf             # Variable definitions
│   ├── outputs.tf               # Output definitions
│   └── terraform.tfvars         # Variable values
├── tests/
│   └── python/
│       ├── __init__.py          # Test package initialization
│       ├── conftest.py          # Pytest configuration
│       └── test_handler.py      # Handler tests
├── scripts/
│   ├── deploy.sh               # Deployment script
│   ├── verify.sh               # Verification script
│   └── cleanup.sh              # Cleanup script
├── docs/
│   ├── architecture.md         # Architecture documentation
│   ├── security.md            # Security considerations
│   └── maintenance.md         # Maintenance guide
├── .github/
│   └── workflows/
│       ├── terraform.yml       # Terraform CI/CD
│       └── python-tests.yml    # Python testing
├── setup.py                    # Python package setup
├── requirements-dev.txt        # Development dependencies
├── .gitignore
├── README.md
└── LICENSE
```

## Prerequisites 📋

- AWS Account with administrative access
- Python 3.8+
- [Terraform](https://www.terraform.io/) (>= 1.0.0)
- [AWS CLI](https://aws.amazon.com/cli/) configured

## Quick Start 🚀

1. **Clone the Repository**
```bash
git clone https://github.com/coopdloop/aws-security-hub-monitor-fast
cd aws-security-hub-monitor-fast
```

2. **Set Up Python Environment**
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install package in development mode
pip install -e ".[dev]"
```

3. **Initialize Terraform**
```bash
cd terraform
terraform init
```

4. **Deploy Infrastructure**
```bash
# Configure variables
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your values

# Deploy
terraform plan
terraform apply
```

## Development Setup 🔧

1. **Install Development Dependencies**
```bash
pip install -r requirements-dev.txt
```

2. **Run Tests**
```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ -v --cov=src/security_monitor
```

## Testing 🧪

### Unit Tests
```bash
# Run specific test file
python -m pytest tests/python/test_handler.py -v

# Run all tests with coverage
python -m pytest tests/ -v --cov=src/security_monitor
```

### Test Configuration
Tests are configured in `tests/python/conftest.py` to:
- Add source directory to Python path
- Set up test fixtures
- Configure mock AWS services

## Infrastructure Management 🏗️

### Deploy Resources
```bash
cd terraform
terraform init
terraform plan
terraform apply
```

### Verify Deployment
```bash
./scripts/verify.sh
```

### Cleanup
```bash
./scripts/cleanup.sh
```

## Security Features 🔒

1. **AWS Security Hub**
   - Automated security assessments
   - Compliance monitoring
   - Security findings aggregation

2. **AWS Config**
   - Resource configuration monitoring
   - Compliance rules
   - Change tracking

3. **CloudTrail**
   - API activity logging
   - Security analysis
   - Audit trail

# AWS Security Hub Monitor 🛡️

[Previous sections remain the same until Development Setup]

## Code Quality and Security Tools 🔍

### Installation
```bash
# Install all development dependencies
pip install -r requirements-dev.txt
```

### Development Dependencies
```plaintext
# Testing
pytest==7.4.4
pytest-cov==4.1.0
pytest-mock==3.12.0
moto==4.2.13
coverage==7.4.1

# Linting and Formatting
flake8==7.0.0
black==24.1.1
isort==5.13.2
pylint==3.0.3
bandit==1.7.7

# Type Checking
mypy==1.8.0
types-boto3==1.0.2
types-requests==2.31.0.20240125

# Security Testing
safety==2.3.5
checkov==3.1.44

# Documentation
mkdocs==1.5.3
mkdocs-material==9.5.3
mkdocstrings==0.24.0

# Development Tools
pre-commit==3.6.0
commitizen==3.13.0

# AWS SDK
boto3==1.34.29
botocore==1.34.29

# Utilities
python-dotenv==1.0.0
requests==2.31.0
pyyaml==6.0.1
```

### Code Quality Tools

#### 1. Black (Code Formatting)
```bash
# Format all Python files
black src/ tests/

# Check formatting without making changes
black --check src/ tests/

# Format with specific line length
black --line-length 88 src/ tests/
```

#### 2. Flake8 (Linting)
```bash
# Run linting checks
flake8 src/ tests/

# With specific configuration
flake8 --max-line-length=88 --extend-ignore=E203 src/ tests/
```

#### 3. isort (Import Sorting)
```bash
# Sort imports
isort src/ tests/

# Check import sorting
isort --check-only src/ tests/

# Show diff without making changes
isort --diff src/ tests/
```

### Security Testing Tools

#### 1. Bandit (Security Linting)
```bash
# Run basic security checks
bandit -r src/

# Generate HTML report
bandit -r src/ -f html -o security-report.html

# Check specific security tests
bandit -r src/ -tests B201,B301

# Ignore specific tests
bandit -r src/ -s B101,B308
```

#### 2. Safety (Dependency Scanning)
```bash
# Check dependencies for known security issues
safety check

# Check requirements file
safety check -r requirements.txt

# Generate JSON report
safety check --json > safety-report.json
```

#### 3. Checkov (Infrastructure Security)
```bash
# Scan Terraform files
checkov -d terraform/

# Scan specific file
checkov -f terraform/main.tf

# Generate report
checkov -d terraform/ --output-file checkov-report.json

# Skip specific checks
checkov -d terraform/ --skip-check CKV_AWS_1,CKV_AWS_2
```

### Type Checking

#### MyPy
```bash
# Run type checking
mypy src/

# More strict checking
mypy --strict src/

# Generate HTML report
mypy src/ --html-report typing-report
```

### Pre-commit Setup

1. Install pre-commit hooks:
```bash
# Install pre-commit
pre-commit install

# Update hooks
pre-commit autoupdate
```

2. Create `.pre-commit-config.yaml`:
```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files

-   repo: https://github.com/psf/black
    rev: 24.1.1
    hooks:
    -   id: black

-   repo: https://github.com/PyCQA/isort
    rev: 5.13.2
    hooks:
    -   id: isort

-   repo: https://github.com/PyCQA/flake8
    rev: 7.0.0
    hooks:
    -   id: flake8

-   repo: https://github.com/PyCQA/bandit
    rev: 1.7.7
    hooks:
    -   id: bandit
        args: ["-ll"]

-   repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
    -   id: mypy
        additional_dependencies: [types-all]
```

### Continuous Integration

Our GitHub Actions workflows include all these checks:

```yaml
name: Code Quality

on: [push, pull_request]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements-dev.txt

    - name: Run Black
      run: black --check src/ tests/

    - name: Run Flake8
      run: flake8 src/ tests/

    - name: Run isort
      run: isort --check-only src/ tests/

    - name: Run Bandit
      run: bandit -r src/

    - name: Run Safety
      run: safety check

    - name: Run MyPy
      run: mypy src/

    - name: Run Checkov
      uses: bridgecrewio/checkov-action@master
      with:
        directory: terraform/
```

### Documentation Generation

```bash
# Install MkDocs
pip install mkdocs mkdocs-material mkdocstrings

# Create new documentation
mkdocs new .

# Serve documentation locally
mkdocs serve

# Build documentation
mkdocs build
```

## Monitoring & Alerts 📊

### Default Notifications
- Critical security findings
- High-severity issues
- Compliance violations
- Configuration changes

### Alert Channels
- SNS notifications
- CloudWatch alarms
- Security Hub dashboard

## Troubleshooting 🔧

### Common Issues

1. **Import Errors**
```bash
# Verify PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:${PWD}/src"

# Check package installation
pip list | grep aws-security-monitor
```

2. **AWS Configuration**
```bash
# Verify AWS credentials
aws sts get-caller-identity

# Check Security Hub status
aws securityhub get-enabled-standards
```

## Contributing 🤝

1. Fork the repository
2. Create your feature branch
```bash
git checkout -b feature/amazing-feature
```
3. Commit your changes
```bash
git commit -m 'Add amazing feature'
```
4. Push to the branch
```bash
git push origin feature/amazing-feature
```
5. Open a Pull Request

## Development Guidelines 📝

1. **Code Style**
   - Follow PEP 8 guidelines
   - Use Black for formatting
   - Run linters before committing

2. **Testing**
   - Write unit tests for new features
   - Maintain test coverage
   - Use mocking for AWS services

3. **Documentation**
   - Update README for new features
   - Document function parameters
   - Keep architecture docs current

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support 💬

For issues and feature requests:
- Create a GitHub issue
- Provide detailed description
- Include error messages
- Share AWS region info

## Authors ✨

Your Name - [@coopdloop](https://github.com/coopdloop)

## Acknowledgments 👏

- AWS Security Best Practices
- AWS Security Hub Documentation
- Terraform AWS Provider Documentation

## Versioning 🏷️

We use [SemVer](http://semver.org/) for versioning. For available versions, see the [tags on this repository](https://github.com/yourusername/aws-security-hub-monitor/tags).
