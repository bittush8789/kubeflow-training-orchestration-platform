# Kubeflow Pipelines
## Installation
Pipelines are installed as part of the standard Kubeflow deployment.
## Architecture
KFP leverages Argo Workflows under the hood to orchestrate DAGs of containers.
## Usage
Build components using `kfp.components.create_component_from_func` and define pipelines using `@kfp.dsl.pipeline`.
## Best Practices
- Keep components small and modular.
- Pass references (URIs) rather than large data objects between steps.
