# Katib
## Installation
Katib is installed natively with Kubeflow.
## Architecture
Katib consists of an Experiment Controller, Trial Controller, and Suggestion Controller.
## Usage
Define an `Experiment` custom resource with the algorithm and search space.
## Best Practices
- Limit `maxTrialCount` to prevent resource exhaustion.
- Use `RandomSearch` for initial exploration before Bayesian Optimization.
