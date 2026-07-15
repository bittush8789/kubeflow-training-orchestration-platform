# Enterprise ML Training Platform

[![Python](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-latest-blue.svg)](https://kubernetes.io/)
[![Kubeflow](https://img.shields.io/badge/Kubeflow-latest-blue.svg)](https://www.kubeflow.org/)
[![MLflow](https://img.shields.io/badge/MLflow-latest-blue.svg)](https://mlflow.org/)
[![KServe](https://img.shields.io/badge/KServe-latest-blue.svg)](https://kserve.github.io/website/)
[![CI/CD](https://github.com/your-org/enterprise-ml-training-platform/actions/workflows/ci-cd.yaml/badge.svg)](https://github.com/your-org/enterprise-ml-training-platform/actions)

This repository contains the full source code and infrastructure definitions for an Enterprise ML Training Platform built with Kubeflow, KServe, and MLflow.

## Structure
- `pipelines/`: Reusable Kubeflow Pipeline components.
- `kubeflow/`: Definitions for KFP Workflows, Katib Experiments, Training Jobs, and KServe Inference Services.
- `mlflow/`: MLflow tracking deployment configuration.
- `kubernetes/`: Kubernetes namespaces, RBAC, and network policies.
- `docs/`: Comprehensive enterprise architecture and operations documentation.
- `.github/workflows/`: CI/CD pipelines.

## Documentation

Below is the directory of all architectural and operational documentation available in the `docs/` folder:

### Architecture
- [High-Level Design (HLD)](docs/architecture/HLD.md)
- [Low-Level Design (LLD)](docs/architecture/LLD.md)

### Kubeflow
- [Kubeflow Pipelines](docs/kubeflow/Kubeflow-Pipelines.md)
- [Katib (Hyperparameter Tuning)](docs/kubeflow/Katib.md)
- [Training Operators](docs/kubeflow/Training-Operators.md)
- [KServe (Model Serving)](docs/kubeflow/KServe.md)

### Infrastructure
- [Kubernetes Architecture](docs/infrastructure/Kubernetes.md)
- [Storage Strategy](docs/infrastructure/Storage.md)
- [Networking & Policies](docs/infrastructure/Networking.md)
- [Security Architecture](docs/infrastructure/Security.md)

### Monitoring
- [Prometheus Metrics](docs/monitoring/Prometheus.md)
- [Grafana Dashboards](docs/monitoring/Grafana.md)
- [Loki Logging](docs/monitoring/Loki.md)
- [Jaeger Tracing](docs/monitoring/Jaeger.md)

### Operations
- [Deployment Guide](docs/operations/Deployment-Guide.md)
- [Runbook](docs/operations/Runbook.md)
- [Troubleshooting Guide](docs/operations/Troubleshooting.md)

### API
- [OpenAPI Specification](docs/api/OpenAPI.md)

## Getting Started
Please refer to the [Deployment Guide](docs/operations/Deployment-Guide.md) for full installation instructions.

### Ubuntu Setup & Execution

To set up and execute the ML Platform locally on an Ubuntu machine:

1. **Install System Dependencies**
   ```bash
   sudo apt update
   sudo apt install -y python3-pip docker.io curl
   ```

2. **Install Kind & Kubectl**
   ```bash
   # Install Kind
   [ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.22.0/kind-linux-amd64
   chmod +x ./kind
   sudo mv ./kind /usr/local/bin/kind
   
   # Install Kubectl
   sudo snap install kubectl --classic
   
   # Start a local Kubernetes cluster
   kind create cluster --name enterprise-ml
   ```

3. **Install Python Requirements & Execute Pipeline**
   ```bash
   pip3 install -r requirements.txt
   
   # Compile the Kubeflow pipeline
   python3 kubeflow/pipelines/workflow.py
   ```
