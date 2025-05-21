# Learn This Project: SRE-LA-FINAL

## 1. Project Overview
This project demonstrates Site Reliability Engineering (SRE) principles using a simple web application stack. It includes a Flask backend, a static frontend, infrastructure as code (Terraform), CI/CD (GitHub Actions), and monitoring (Prometheus & Grafana).

---

## 2. Application Components

### 2.1 Backend (`app/backend`)
- **Language:** Python (Flask)
- **Key files:**
  - `app.py`: Main API logic and Prometheus metrics endpoint
  - `requirements.txt`: Python dependencies
  - `Dockerfile`: Containerizes the backend
  - `test_app.py`: Unit tests

### 2.2 Frontend (`app/frontend`)
- **Type:** Static HTML/JS (e.g., React or plain HTML)
- **Key files:**
  - `index.html`: Main UI
  - `Dockerfile`: Containerizes the frontend

---

## 3. Infrastructure as Code (`infrastructure`)
- **Tool:** Terraform
- **Key files:**
  - `main.tf`: Root Terraform configuration, wires up all modules
  - `modules/`: Contains submodules for VPC, compute, security, load balancer, and monitoring
- **How it works:**
  - Each module is a reusable chunk of infrastructure (e.g., VPC, EC2, Security Groups)
  - The root module (`main.tf`) passes variables to each submodule
  - Outputs from one module (e.g., VPC ID) are used as inputs to others (e.g., compute, lb)

---

## 4. Monitoring (`monitoring`)
- **Prometheus:**
  - `prometheus.yml`: Scrape config for metrics
  - `alerts.yml`: Alerting rules
- **Grafana:**
  - `grafana/provisioning/`: Dashboards and datasources auto-provisioned
  - `app-dashboard.json`: Example dashboard

---

## 5. Docker & Docker Compose
- **Dockerfiles:**
  - Backend and frontend each have their own Dockerfile
- **docker-compose.yml:**
  - Orchestrates backend, frontend, Prometheus, and Grafana for local development

---

## 6. CI/CD Pipeline (`.github/workflows/ci-cd.yml`)
- **Test job:** Lints and tests backend
- **Build-and-push job:** Builds and pushes Docker images to Docker Hub
- **Deploy job:** Runs Terraform to provision/update infrastructure
- **Best practices:** Uses latest GitHub Actions, secrets for credentials, and job dependencies

---

## 7. SRE Practices
- **SLI/SLO/SLA:** Defined in `docs/sli_slo_sla.md` and implemented via Prometheus metrics and Grafana dashboards
- **Security:** Security audit in `docs/security_audit.md` with actionable recommendations
- **Capacity Planning:** Custom tool in `tools/capacity_planner.py` (see setup guide)

---

## 8. How Everything Fits Together
1. **Developers** write code in `app/backend` and `app/frontend`.
2. **CI/CD** runs tests, builds Docker images, and deploys infrastructure and containers.
3. **Terraform** provisions AWS resources (VPC, EC2, Security Groups, etc).
4. **Docker Compose** is used for local development/testing.
5. **Prometheus** scrapes metrics from the backend and infrastructure.
6. **Grafana** visualizes metrics and SLOs.
7. **Security** and **capacity planning** are integrated into the workflow.

---

## 9. Learning Path: Step by Step
1. **Understand the app:** Read `app/backend/app.py` and `app/frontend/index.html`.
2. **Run locally:** Use `docker-compose up` to start the stack.
3. **Explore monitoring:** Visit Prometheus and Grafana dashboards.
4. **Check CI/CD:** Review `.github/workflows/ci-cd.yml` for automation logic.
5. **Review IaC:** Study `infrastructure/main.tf` and modules.
6. **Deploy to cloud:** Use Terraform to provision AWS resources.
7. **Review SRE docs:** Read `docs/sli_slo_sla.md` and `docs/security_audit.md`.
8. **Try capacity planning:** Run the tool in `tools/capacity_planner.py`.

---

## 10. Where to Go Next
- Deepen your understanding of each SRE/DevOps tool used
- Expand modules to real infrastructure (replace placeholders)
- Implement security recommendations
- Add more tests and monitoring

---

**This project is a full-stack SRE/DevOps demo. Use it as a template, a learning resource, or a starting point for your own production-ready systems!** 