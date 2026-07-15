# Deployment Guide

## Production Deployment (Cloud)
1. Provision EKS/GKE cluster.
2. Install Kubeflow manifests.
3. Configure OIDC authentication.
4. Deploy pipeline via `.github/workflows/ci-cd.yaml`.

## Local Setup & Execution (Ubuntu)

If you are developing or testing locally on an Ubuntu system, follow these steps to set up the environment and execute the pipeline:

### 1. Install System Dependencies
Update your package list and install Docker and Python:
```bash
sudo apt update
sudo apt install -y python3 python3-pip docker.io curl
```

### 2. Install Kind & Kubectl
Kind (Kubernetes IN Docker) will act as our local Kubernetes cluster.
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

### 3. Clone and Setup the Repository
```bash
git clone <your-repo-url>
cd enterprise-ml-training-platform

# Install Python dependencies
pip3 install -r requirements.txt
```

### 4. Execute the Kubeflow Pipeline
To compile the pipeline and generate the workflow JSON definition:
```bash
python3 kubeflow/pipelines/workflow.py
```
This will produce an `enterprise_ml_pipeline.json` file which can then be uploaded and executed via the Kubeflow Pipelines UI.
