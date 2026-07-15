from kfp.v2.dsl import component, Input, Output, Dataset

@component(base_image="python:3.9-slim", packages_to_install=["pandas", "scikit-learn"])
def preprocess_data(dataset_in: Input[Dataset], dataset_out: Output[Dataset]):
    import pandas as pd
    from sklearn.preprocessing import StandardScaler
    
    df = pd.read_csv(dataset_in.path)
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df[['feature1']])
    df['feature1'] = scaled_features
    df.to_csv(dataset_out.path, index=False)
