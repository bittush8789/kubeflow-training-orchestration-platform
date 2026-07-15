# Troubleshooting Guide
## Failed Pipelines
Check Argo workflow logs.
## Failed Training Jobs
Check worker pod logs for OOM (Out of Memory) errors.
## Katib Failures
Ensure objective metrics are being correctly logged by the training container.
## KServe Issues
If scale-from-zero fails, verify Knative pod startup times and image pull secrets.
