from kfp.v2.dsl import component, Input, Model

@component(base_image="python:3.9-slim", packages_to_install=["requests"])
def register_model(model: Input[Model], metrics: dict) -> str:
    print(f"Registering model to MLflow with metrics {metrics}")
    # Logic to register with MLFlow would go here
    return "Model registered successfully"
