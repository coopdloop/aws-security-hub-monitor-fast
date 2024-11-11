# flake8: noqa
from datetime import datetime


def get_severity_level(severity):
    """Convert severity label to numeric value"""
    severity_map = {
        "CRITICAL": 4,
        "HIGH": 3,
        "MEDIUM": 2,
        "LOW": 1,
        "INFORMATIONAL": 0,
    }  #
    return severity_map.get(severity.upper(), 0)


def create_alert_message(finding):
    """Create formatted alert message from finding"""
    return f"""
Security Finding Details:
------------------------
Title: {finding.get('Title', 'N/A')}
Severity: {finding.get('Severity', {}).get('Label', 'N/A')}
Description: {finding.get('Description', 'N/A')}
Account: {finding.get('AwsAccountId', 'N/A')}
Region: {finding.get('Region', 'N/A')}
Resource: {finding.get('Resources', [{'Id': 'N/A'}])[0]['Id']}
Remediation: {finding.get('Remediation', {}).get('Recommendation', {}).get('Text', 'N/A')}
"""


def format_timestamp(timestamp):
    """Format timestamp for display"""
    try:
        return datetime.fromisoformat(
            timestamp.replace("Z", "+00:00")
        ).strftime(  # flake
            "%Y-%m-%d %H:%M:%S UTC"
        )
    except:  # noqa: E722
        return timestamp
