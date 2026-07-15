from kfp.v2.dsl import component, Input, Dataset

@component(base_image="python:3.9-slim", packages_to_install=["pandas"])
def validate_data(dataset: Input[Dataset]) -> bool:
    import pandas as pd
    df = pd.read_csv(dataset.path)
    print("Validating data...")
    if df.isnull().values.any():
        raise ValueError("Data contains null values")
    return True
