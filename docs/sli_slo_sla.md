# SLI, SLO, and SLA Documentation

This document defines the Service Level Indicators (SLIs), Service Level Objectives (SLOs), and Service Level Agreements (SLAs) for our SRE Demo Application.

## Service Level Indicators (SLIs)

SLIs are quantitative measures of service level provided to customers. Our application measures:

### 1. Availability
- **Definition**: Percentage of successful HTTP requests (non-5xx responses)
- **Measurement**: `sum(rate(app_request_count{http_status!~"5.."}[1h])) / sum(rate(app_request_count[1h]))`
- **Collection**: Continuous via Prometheus

### 2. Latency
- **Definition**: Time taken to process and respond to requests
- **Measurement**: 
  - 50th percentile (median): `histogram_quantile(0.5, sum(rate(app_request_latency_seconds_bucket[1h])) by (le))`
  - 95th percentile: `histogram_quantile(0.95, sum(rate(app_request_latency_seconds_bucket[1h])) by (le))`
  - 99th percentile: `histogram_quantile(0.99, sum(rate(app_request_latency_seconds_bucket[1h])) by (le))`

### 3. Error Rate
- **Definition**: Percentage of requests that result in an error (5xx responses)
- **Measurement**: `sum(rate(app_request_count{http_status=~"5.."}[1h])) / sum(rate(app_request_count[1h]))`

### 4. Throughput
- **Definition**: Number of requests processed per second
- **Measurement**: `sum(rate(app_request_count[1m]))`

## Service Level Objectives (SLOs)

SLOs define the target values for our SLIs. Our SLOs are:

### 1. Availability SLO
- **Target**: 99.9% of requests should be successful
- **Measurement Window**: 30-day rolling window
- **Error Budget**: 0.1% (43.8 minutes of downtime per month)

### 2. Latency SLO
- **Target**: 
  - 95% of requests should complete within 200ms
  - 99% of requests should complete within 500ms
- **Measurement Window**: 24-hour rolling window

### 3. Error Rate SLO
- **Target**: Error rate should be less than 1%
- **Measurement Window**: 1-hour rolling window

## Service Level Agreement (SLA)

This is our customer-facing commitment regarding service quality:

### Availability Commitment
- **Commitment**: 99.5% monthly uptime
- **Calculation**: Percentage of minutes the service responds successfully in a month
- **Exclusions**: Scheduled maintenance, force majeure events

### Performance Commitment
- **Commitment**: 95% of requests will complete within 300ms
- **Measurement**: Based on server-side measurements
- **Reporting**: Monthly availability report

### Incident Response Times
- **Severity 1 (Critical)**: Response within 15 minutes, resolution or mitigation within 2 hours
- **Severity 2 (High)**: Response within 30 minutes, resolution or mitigation within 8 hours
- **Severity 3 (Medium)**: Response within 2 hours, resolution or mitigation within 24 hours
- **Severity 4 (Low)**: Response within 24 hours, resolution or mitigation within 72 hours

### Remediation
- **Credit**: 10% of monthly fee for each 0.5% below SLA commitment
- **Maximum Credit**: 30% of monthly fee
- **Claim Process**: Customer must submit claim within 30 days of incident

## Monitoring and Reporting

- **Dashboard**: Real-time SLO dashboard available in Grafana (port 3000)
- **Alerts**: Set up in Prometheus for SLO violations
- **Monthly Reports**: Generated on the 1st of each month

## Error Budget Policy

Our error budget is 0.1% of total requests (for availability). If we consume more than:

- 50% of error budget: Alert SRE team
- 75% of error budget: Freeze new feature deployments
- 100% of error budget: All hands on deck to improve reliability

## Revision History

| Date | Version | Description |
|------|---------|-------------|
| 2025-05-16 | 1.0 | Initial version | 