# SRE Final Project
## Application Reliability with SRE Principles

**Team Members:**
- Iskakov Amir
- Zholtaev Temirlan

**Group:** SE-2331  
**Date:** May 16, 2025

---

# Project Overview

We have created a comprehensive Site Reliability Engineering (SRE) implementation with:

1. Web application with built-in reliability features
2. Infrastructure as Code (Terraform)
3. CI/CD pipeline (GitHub Actions)
4. Monitoring and alerting (Prometheus & Grafana)
5. Security auditing
6. Capacity planning
7. Custom SRE tooling

---

# Task 1: Application Reliability

Our application is a simple web service with:

- **Flask backend** with built-in metrics collection
- **React frontend** with responsive UI
- **Prometheus metrics** for monitoring
- **Simulated failures** to demonstrate SRE principles

## SLIs (Service Level Indicators)

- Response time (95th percentile < 200ms)
- Error rate (< 1%)
- Availability (> 99.9%)

## SLOs (Service Level Objectives)

- 95% of requests complete in < 200ms
- Error rate is < 1% over 30-day window
- Service is available 99.9% of time (43.8 minutes downtime/month)

---

# Task 2: Infrastructure as Code

We used Terraform to design a scalable infrastructure:

- **AWS infrastructure** with autoscaling
- **VPC, subnets, security groups** properly configured
- **Load balancers** for high availability
- **Modular design** for easier management

**Team collaboration:**
- Iskakov Amir: Network, Security modules
- Zholtaev Temirlan: Compute, Monitoring modules

---

# Task 3: Automated Deployment Pipeline

Our CI/CD pipeline using GitHub Actions includes:

1. **Build stage**
   - Code checkout
   - Dependency installation
   - Unit tests
   - Linting

2. **Test stage**
   - Integration tests
   - Code quality checks

3. **Deploy stage**
   - Docker image creation
   - Terraform provisioning
   - Zero-downtime deployment

---

# Task 4: Security Audit

We conducted a security audit and identified these vulnerabilities:

1. **Open security groups** exposing ports unnecessarily
2. **No HTTPS** for frontend traffic
3. **Default container privileges**
4. **No WAF** protection against common attacks

## Mitigations implemented:

- Restricted security groups to necessary ports
- Added HTTPS with proper certificates
- Implemented least-privilege containers
- Added WAF rules for XSS, injection protection

---

# Task 5: Capacity Planning

We created a capacity planning simulation that:

1. Forecasts resource needs based on traffic patterns
2. Uses historical metrics for predictions
3. Displays confidence intervals for better planning
4. Integrates with our monitoring system

Our custom tool demonstrates:
- Linear regression forecasting
- Visualization of growth patterns
- Alerting when capacity thresholds approached

---

# Task 6: SRE Tool Development

We developed a custom SRE tool for capacity planning:

- **Python-based** with command-line interface
- **Integrates with Prometheus** for real-time data
- **Predicts future resource needs** based on historical usage
- **Generates visual reports** for easier understanding
- **Calculates confidence intervals** for better planning

```bash
# Example usage
python tools/capacity_planner.py --prometheus http://localhost:9090 --range 14d
```

---

# Lessons Learned

1. **Importance of monitoring** from the beginning
2. **Infrastructure as Code** makes deployments repeatable
3. **Automation** reduces human error
4. **Security** must be integrated throughout
5. **Capacity planning** prevents outages

## Challenges Faced

- Setting up proper metrics collection
- Ensuring zero-downtime deployments
- Balancing security with usability
- Accurate capacity predictions

---

# Demo & Questions

## Repository

https://github.com/iskakov-amir/SRE-LA-FINAL

## Thank you!

**Iskakov Amir & Zholtaev Temirlan**  
SE-2331 