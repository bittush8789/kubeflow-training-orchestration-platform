# Low-Level Design (LLD)
## Enterprise ML Training Platform

### 1. Pipeline Design (Kubeflow Pipelines)
Each pipeline component is encapsulated in a Docker container and orchestrated via KFP SDK (`kfp.v2`).

#### Component Breakdown
1. **Data Ingestion (`pipelines/ingestion`)**
   - Base image: `python:3.9-slim`
   - Action: Downloads CSV/Parquet files from `s3://enterprise-ml-data`.
2. **Data Validation (`pipelines/validation`)**
   - Action: Uses `Great Expectations` or `pandas` for schema checks and null value detection.
3. **Preprocessing & Feature Engineering (`pipelines/preprocessing`)**
   - Action: Handles missing values, scaling, one-hot encoding, and feature selection.
4. **Model Training (`pipelines/training`)**
   - Action: Triggers distributed training or local Katib experiment.
5. **Model Evaluation (`pipelines/evaluation`)**
   - Action: Computes F1, ROC AUC, Precision, Recall.
6. **Registration (`pipelines/deployment`)**
   - Action: If metrics exceed a threshold, registers the model to MLflow and initiates a KServe rollout.

### 2. Katib Design (Hyperparameter Tuning)
- **Algorithm**: `RandomSearch` / `BayesianOptimization`
- **Objective Metric**: `Validation-Accuracy` or `Validation-Loss`.
- **Search Space**:
  - `learning_rate`: `[0.001, 0.1]`
  - `batch_size`: `[16, 32, 64]`
  - `n_estimators`: `[50, 100, 200]`

### 3. Training Workflow (Distributed Operators)
- Uses Kubeflow's `TFJob`, `PyTorchJob`, or `XGBoostJob`.
- **Architecture**:
  - 1 Master / Chief Pod
  - N Worker Pods
- **Storage**: Attached persistent volume for checkpoints, or direct streaming to S3.

### 4. Serving Workflow (KServe)
- **InferenceService Definition**:
  - Custom Predictor or standard SKLearn/PyTorch Server.
  - StorageUri points to `s3://enterprise-model-registry/models/<version>`.
- **Traffic Routing**: Istio handles routing. Canary deployments start with 10% traffic to the new model revision.

### 5. Monitoring Design
- **Prometheus**: Uses `ServiceMonitor` to scrape metrics from the model endpoints `/metrics`.
- **Grafana**:
  - Dashboard 1: Pipeline Success/Failure rates.
  - Dashboard 2: KServe inference latency, requests per second (RPS), error rates.
- **Loki**: DaemonSet Promtail captures stdout/stderr of training pods for central debugging.
