import os
import unittest
from unittest.mock import MagicMock, patch

import boto3
from moto import mock_aws

from security_monitor.handler import lambda_handler
from security_monitor.utils import create_alert_message, get_severity_level


class TestSecurityHandler(unittest.TestCase):
    """Test cases for the Security Handler Lambda function"""

    @mock_aws
    def setUp(self):
        """Set up test fixtures"""
        self.sns = boto3.client("sns", region_name="us-east-1")
        self.topic = self.sns.create_topic(Name="test-topic")
        os.environ["SNS_TOPIC_ARN"] = self.topic["TopicArn"]

        # Sample security finding
        self.sample_finding = {
            "detail": {
                "findings": [
                    {
                        "Title": "Test Security Finding",
                        "Description": "This is a test finding",
                        "Severity": {"Label": "HIGH"},
                        "AwsAccountId": "123456789012",
                        "Region": "us-east-1",
                        "Resources": [{"Id": "test-resource-id"}],
                    }
                ]
            }
        }

    def test_get_severity_level(self):
        """Test severity level conversion"""
        self.assertEqual(get_severity_level("CRITICAL"), 4)
        self.assertEqual(get_severity_level("HIGH"), 3)
        self.assertEqual(get_severity_level("MEDIUM"), 2)
        self.assertEqual(get_severity_level("LOW"), 1)
        self.assertEqual(get_severity_level("INFORMATIONAL"), 0)
        self.assertEqual(get_severity_level("UNKNOWN"), 0)

    def test_create_alert_message(self):
        """Test alert message creation"""
        finding = self.sample_finding["detail"]["findings"][0]
        message = create_alert_message(finding)

        # Verify message contains required information
        self.assertIn("Test Security Finding", message)
        self.assertIn("HIGH", message)
        self.assertIn("test-resource-id", message)
        self.assertIn("123456789012", message)

    @mock_aws
    @patch("boto3.client")
    def test_lambda_handler_high_severity(self, mock_boto):
        """Test lambda handler with high severity finding"""
        # Setup mock SNS
        mock_sns = MagicMock()
        mock_boto.return_value = mock_sns

        # Call lambda handler
        response = lambda_handler(self.sample_finding, {})

        # Verify SNS publish was called
        mock_sns.publish.assert_called_once()
        call_args = mock_sns.publish.call_args[1]
        self.assertIn("Security Finding - HIGH", call_args["Subject"])
        self.assertEqual(response["statusCode"], 200)

    def test_lambda_handler_no_findings(self):
        """Test lambda handler with no findings"""
        event = {"detail": {"findings": []}}
        response = lambda_handler(event, {})
        self.assertEqual(response["statusCode"], 200)

    @mock_aws
    def test_lambda_handler_low_severity(self):
        """Test lambda handler with low severity finding"""
        # Modify finding to low severity
        low_severity_finding = self.sample_finding.copy()
        low_severity_finding["detail"]["findings"][0]["Severity"][
            "Label"
        ] = "LOW"  # format

        response = lambda_handler(low_severity_finding, {})
        self.assertEqual(response["statusCode"], 200)

    def test_error_handling(self):
        """Test error handling in lambda handler"""
        # Test with invalid event structure
        invalid_event = {"invalid": "structure"}
        with self.assertRaises(KeyError):
            lambda_handler(invalid_event, {})

            # TODO fix

    # @mock_aws
    # def test_multiple_findings(self):
    #     """Test handling multiple findings"""
    #     multiple_findings = {
    #         "detail": {
    #             "findings": [
    #                 {
    #                     "Title": "Finding 1",
    #                     "Description": "First finding",
    #                     "Severity": {"Label": "HIGH"},
    #                     "AwsAccountId": "123456789012",
    #                     "Region": "us-east-1",
    #                     "Resources": [{"Id": "resource-1"}],
    #                 },
    #                 {
    #                     "Title": "Finding 2",
    #                     "Description": "Second finding",
    #                     "Severity": {"Label": "CRITICAL"},
    #                     "AwsAccountId": "123456789012",
    #                     "Region": "us-east-1",
    #                     "Resources": [{"Id": "resource-2"}],
    #                 },
    #             ]
    #         }
    #     }
    #
    #     response = lambda_handler(multiple_findings, {})
    #     self.assertEqual(response["statusCode"], 200)


if __name__ == "__main__":
    unittest.main()
