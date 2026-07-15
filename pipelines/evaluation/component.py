from kfp.v2.dsl import component, Input, Model, Dataset, Metrics

@component(base_image="python:3.9-slim", packages_to_install=["pandas", "scikit-learn", "joblib"])
def evaluate_model(dataset: Input[Dataset], model: Input[Model], metrics: Output[Metrics]):
    import pandas as pd
    import joblib
    from sklearn.metrics import accuracy_score, f1_score
    
    df = pd.read_csv(dataset.path)
    clf = joblib.load(model.path + '.joblib')
    predictions = clf.predict(df[['feature1']])
    
    accuracy = accuracy_score(df['target'], predictions)
    f1 = f1_score(df['target'], predictions, average='macro')
    
    metrics.log_metric("accuracy", accuracy)
    metrics.log_metric("f1_score", f1)
