# SRE Project Setup Guide

This guide will help you set up the SRE Demo Project on your local machine or in a cloud environment.

## Prerequisites

- Docker and Docker Compose
- Python 3.9+
- Terraform (if deploying to AWS)
- AWS account (if deploying to cloud)

## Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/SRE-LA-FINAL.git
cd SRE-LA-FINAL
```

### 2. Run with Docker Compose

The easiest way to get the entire stack running is to use Docker Compose:

```bash
docker-compose up
```

This will start:
- Backend API (Flask) on port 5000
- Frontend on port 80
- Prometheus on port 9090
- Grafana on port 3000

### 3. Access the Services

- **Web Application**: http://localhost
- **Backend API**: http://localhost:5000
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000 (default login: admin/admin)

## Manual Setup (without Docker)

### 1. Backend Setup

```bash
cd app/backend
pip install -r requirements.txt
python app.py
```

The backend will start on port 5000 and Prometheus metrics will be available on port 8000.

### 2. Frontend Setup

```bash
cd app/frontend
# Just open index.html in a browser
```

### 3. Monitoring Setup

For local Prometheus:

```bash
cd monitoring
docker run -d -p 9090:9090 -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
```

For local Grafana:

```bash
docker run -d -p 3000:3000 grafana/grafana
```

## Cloud Deployment

### 1. Configure AWS Credentials

```bash
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
export AWS_DEFAULT_REGION="us-west-2"
```

### 2. Deploy with Terraform

```bash
cd infrastructure
terraform init
terraform plan
terraform apply
```

## Using the Capacity Planning Tool

Our custom capacity planning tool can be used to predict future resource needs:

```bash
# Install dependencies
pip install requests numpy scipy matplotlib

# Run the tool
python tools/capacity_planner.py --prometheus http://localhost:9090 --range 7d
```

## SLIs and SLOs

This application has the following SLIs and SLOs:

| SLI | SLO |
|-----|-----|
| Response Time | 95th percentile < 200ms |
| Error Rate | < 1% |
| Availability | 99.9% |

## Security Considerations

- The default setup uses HTTP, not HTTPS
- Default Docker security is used, which may not be ideal for production
- The application includes simulated failures for demonstration purposes

## Troubleshooting

If you encounter issues:

1. Check that all ports are available
2. Ensure Docker has sufficient resources
3. Check logs with `docker-compose logs`
4. For Prometheus errors, verify the configuration in `monitoring/prometheus.yml`

## Support

If you need assistance, please open an issue on GitHub. 