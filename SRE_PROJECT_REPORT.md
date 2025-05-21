# SRE Project Report: SRE-LA-FINAL

## 1. Introduction
- **Project goal:** Build a reliable, observable, and automated web service using SRE/DevOps best practices.
- **Team:** Iskakov Amir, Zholtaev Temirlan

---

## 2. Step-by-Step Project Journey

### 2.1 Initial Planning
- Chose Flask for backend, static HTML for frontend, Docker for containerization, Terraform for IaC, GitHub Actions for CI/CD, Prometheus & Grafana for monitoring.

---

### 2.2 Application Development

#### Backend
- **Stack:** Python 3.9, Flask
- **Key file:** `app/backend/app.py`
- **Problems faced:**
  - Flask version compatibility with Werkzeug (fixed by pinning Werkzeug version in `requirements.txt`).
- **Testing:** Wrote `test_app.py` and ran with pytest.

#### Frontend
- **Stack:** Static HTML/JS
- **Key file:** `app/frontend/index.html`
- **Problems faced:**
  - None significant, as frontend is static.

---

### 2.3 Containerization

#### Dockerfiles
- Wrote separate `Dockerfile` for backend and frontend.
- **Backend Dockerfile:** Used official Python image, installed dependencies, exposed port 5000.
- **Frontend Dockerfile:** Used nginx or simple static server.
- **Problems faced:**
  - Ensured correct working directory and port exposure.

#### Docker Compose
- Created `docker-compose.yml` to orchestrate backend, frontend, Prometheus, and Grafana.
- **Problems faced:**
  - Service dependencies and port conflicts.

---

### 2.4 Infrastructure as Code (Terraform)

#### Structure
- Wrote `infrastructure/main.tf` and created modules for VPC, compute, security, lb, monitoring.
- **Problems faced:**
  - **Module not found:**
    - Initially used `source = "modules/compute"` (Terraform expected `./modules/compute`).
    - Fixed by adding `./` prefix.
  - **Empty module directories:**
    - Git does not track empty directories, so modules were missing in CI/CD.
    - Fixed by adding minimal `main.tf`, `variables.tf`, and `outputs.tf` to each module.
  - **Unsupported argument:**
    - Passed variables to modules that were not defined in `variables.tf`.
    - Fixed by adding all required variables to each module's `variables.tf`.
  - **Unsupported attribute:**
    - Tried to use `module.compute.instance_ids` without defining it in `outputs.tf`.
    - Fixed by adding a dummy output.

#### Example Fix:
```hcl
# infrastructure/modules/compute/outputs.tf
output "instance_ids" {
  value = []
}
```

---

### 2.5 CI/CD Pipeline

#### GitHub Actions
- Created `.github/workflows/ci-cd.yml` with jobs for test, build-and-push, and deploy.
- **Problems faced:**
  - **Deprecated set-output warnings:**
    - Fixed by upgrading all actions to latest versions.
  - **Docker login issues:**
    - GPG error when saving credentials locally; fixed by adjusting Docker config and using `--password-stdin`.
    - 401 Unauthorized in CI; fixed by generating a new Docker Hub access token and updating GitHub secrets.
  - **Terraform errors in CI:**
    - Missing module directories (see above).
    - Fixed by ensuring all modules have at least one file and are committed.

---

### 2.6 Monitoring & Alerting

#### Prometheus
- Wrote `monitoring/prometheus.yml` to scrape backend metrics.
- Added `prometheus_client` to Flask app.
- **Problems faced:**
  - Ensured metrics endpoint is exposed and reachable.

#### Grafana
- Provisioned dashboards and datasources via JSON/YAML in `monitoring/grafana/provisioning/`.
- **Problems faced:**
  - Default credentials; noted in security audit.

---

### 2.7 SRE Practices

#### SLI/SLO/SLA
- Defined in `docs/sli_slo_sla.md`.
- Visualized in Grafana.

#### Security Audit
- Wrote `docs/security_audit.md`.
- **Findings:**
  - HTTP only, permissive security groups, default credentials, etc.
- **Actions:**
  - Documented remediation plan.

#### Capacity Planning
- Wrote and used `tools/capacity_planner.py` to analyze Prometheus data.

---

## 3. Screenshots

*(Add screenshots of: running app, Grafana dashboard, Prometheus UI, CI/CD pipeline, Terraform apply output, etc. Place them in a `/screenshots` folder and reference here.)*

Example:
```
![Grafana Dashboard](screenshots/grafana_dashboard.png)
```

---

## 4. Lessons Learned

- Always define all variables and outputs in Terraform modules.
- Git does not track empty directories—add a `.gitkeep` or real files.
- Use the latest versions of GitHub Actions to avoid deprecation warnings.
- Secure your Docker and AWS credentials; rotate tokens as needed.
- Document every step and problem for future reference.

---

## 5. References

- [LEARN_THIS_PROJECT.md](LEARN_THIS_PROJECT.md)
- [docs/setup_guide.md](docs/setup_guide.md)
- [docs/security_audit.md](docs/security_audit.md)
- [docs/sli_slo_sla.md](docs/sli_slo_sla.md)

---

**This report documents the real journey, problems, and solutions of building the SRE-LA-FINAL project.** 