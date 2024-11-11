# AWS Security Monitor Architecture

## Overview
This document describes the architecture of the AWS Security Monitor project.

## Components
1. AWS Security Hub
   - Central security findings aggregator
   - Enables security standards
   - Generates security scores

2. AWS Config
   - Records resource configurations
   - Evaluates compliance
   - Tracks changes

3. Lambda Function
   - Processes security findings
   - Generates alerts
   - Implements automated responses

## Flow Diagram
[Include your mermaid diagram here]

## Security Considerations
- All data encrypted at rest
- Least privilege access
- Audit logging enabled
