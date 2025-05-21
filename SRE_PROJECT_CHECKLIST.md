# SRE Project Step-by-Step Checklist

This checklist/report guides you through building a full SRE/DevOps project from scratch, similar to SRE-LA-FINAL.

---

## 1. Create a Simple Web Application
- [ ] Choose a backend framework (e.g., Flask, Express, Django)
- [ ] Implement basic API endpoints
- [ ] (Optional) Create a frontend (React, Vue, or static HTML)
- [ ] Add unit tests for backend logic

## 2. Containerize the Application
- [ ] Write a `Dockerfile` for the backend
- [ ] Write a `Dockerfile` for the frontend
- [ ] Build and run containers locally to verify

## 3. Orchestrate with Docker Compose
- [ ] Create a `docker-compose.yml` to run all services (backend, frontend, monitoring)
- [ ] Add Prometheus and Grafana services for monitoring
- [ ] Test the full stack locally with `docker-compose up`

## 4. Infrastructure as Code (IaC) with Terraform
- [ ] Install Terraform
- [ ] Write `main.tf` for root configuration
- [ ] Create modules for VPC, compute, security, load balancer, monitoring
- [ ] Define variables and outputs for each module
- [ ] Use outputs from one module as inputs to others
- [ ] Test with `terraform init`, `plan`, and `apply` (use AWS or localstack)

## 5. Set Up CI/CD Pipeline
- [ ] Create a GitHub Actions workflow (`.github/workflows/ci-cd.yml`)
- [ ] Add jobs for testing, building, pushing Docker images, and deploying with Terraform
- [ ] Store secrets (Docker Hub, AWS credentials) in GitHub Secrets
- [ ] Use job dependencies and latest action versions

## 6. Implement Monitoring & Alerting
- [ ] Add Prometheus metrics to backend (e.g., using `prometheus_client` in Flask)
- [ ] Configure `prometheus.yml` to scrape metrics
- [ ] Set up Grafana dashboards (JSON or via UI)
- [ ] Add alerting rules in Prometheus (`alerts.yml`)

## 7. Define SLI/SLO/SLA
- [ ] Document SLIs (availability, latency, error rate, throughput)
- [ ] Set SLO targets (e.g., 99.9% availability)
- [ ] Define SLA commitments (e.g., 99.5% uptime)
- [ ] Visualize SLOs in Grafana
- [ ] Set up error budget policies

## 8. Security Best Practices
- [ ] Audit security groups and network access
- [ ] Use HTTPS for all endpoints
- [ ] Run containers as non-root
- [ ] Change default credentials (e.g., Grafana)
- [ ] Add dependency scanning to CI/CD
- [ ] Implement security headers in web responses

## 9. Capacity Planning
- [ ] Collect usage metrics with Prometheus
- [ ] Analyze trends and forecast with a custom tool (e.g., Python script)
- [ ] Document findings and adjust infrastructure as needed

## 10. Documentation & Handover
- [ ] Write a `README.md` with project overview and instructions
- [ ] Document setup steps in a `setup_guide.md`
- [ ] Write a security audit report
- [ ] Document SLI/SLO/SLA definitions

---

**Follow this checklist to build a robust, observable, and reliable web service with modern SRE/DevOps practices!** 