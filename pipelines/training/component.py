from kfp.v2.dsl import component, Input, Output, Dataset, Model

@component(base_image="python:3.9-slim", packages_to_install=["pandas", "scikit-learn", "joblib"])
def train_model(dataset: Input[Dataset], model: Output[Model], learning_rate: float, n_estimators: int):
    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier
    import joblib
    
    df = pd.read_csv(dataset.path)
    clf = RandomForestClassifier(n_estimators=n_estimators)
    clf.fit(df[['feature1']], df['target'])
    joblib.dump(clf, model.path + '.joblib')
