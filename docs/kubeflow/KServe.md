# KServe
## Architecture
KServe builds on Knative and Istio to provide serverless inference with scale-to-zero capabilities.
## Usage
Create `InferenceService` manifests specifying the model format and storage URI.
## Best Practices
- Use canary rollouts for safe production updates.
- Monitor latency closely during scale-from-zero events.
