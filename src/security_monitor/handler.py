import json
import boto3
import os
from .utils import create_alert_message, get_severity_level


def lambda_handler(event, context):
    """
    Process Security Hub findings and generate alerts
    """
    try:
        findings = event["detail"]["findings"]
        sns = boto3.client("sns")

        for finding in findings:
            severity = finding.get("Severity", {}).get(
                "Label", "INFORMATIONAL"
            )  # flake8: noqa

            if get_severity_level(severity) >= get_severity_level("HIGH"):
                message = create_alert_message(finding)

                # Publish to SNS
                finding_title = {finding.get("Title", "No Title")}

                sns.publish(
                    TopicArn=os.environ["SNS_TOPIC_ARN"],
                    Subject=f"Security Finding - {severity}: {finding_title}",
                    Message=message,
                )

        return {
            "statusCode": 200,
            "body": json.dumps("Successfully processed findings"),
        }

    except Exception as e:
        print(f"Error processing findings: {str(e)}")
        raise
