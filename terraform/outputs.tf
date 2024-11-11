output "security_hub_enabled" {
  description = "Indicates if Security Hub is enabled"
  value       = aws_securityhub_account.main.id
}

output "config_recorder_id" {
  description = "The ID of the AWS Config recorder"
  value       = aws_config_configuration_recorder.config.id
}

output "config_logs_bucket" {
  description = "The name of the S3 bucket storing AWS Config logs"
  value       = aws_s3_bucket.config_logs.id
}

output "config_role_arn" {
  description = "The ARN of the IAM role used by AWS Config"
  value       = aws_iam_role.config_role.arn
}
