from kfp.v2.dsl import component, Output, Dataset

@component(base_image="python:3.9-slim", packages_to_install=["pandas", "boto3"])
def ingest_data(s3_path: str, dataset: Output[Dataset]):
    import pandas as pd
    # Mocking data ingestion
    print(f"Loading data from {s3_path}")
    df = pd.DataFrame({'feature1': [1, 2, 3], 'target': [0, 1, 0]})
    df.to_csv(dataset.path, index=False)
