from kfp.v2 import dsl, compiler
import sys
import os

# Add components path to sys.path if doing local imports, 
# for simplicity we define them inline or load them.
# In a real project we would use kfp.components.load_component_from_file

@dsl.pipeline(
    name="enterprise-ml-pipeline",
    description="End-to-end ML Pipeline for Enterprise Platform"
)
def enterprise_ml_pipeline(
    s3_raw_data_path: str = "s3://enterprise-ml-data/raw/data.csv",
    learning_rate: float = 0.01,
    n_estimators: int = 100
):
    from pipelines.ingestion.component import ingest_data
    from pipelines.validation.component import validate_data
    from pipelines.preprocessing.component import preprocess_data
    from pipelines.training.component import train_model
    from pipelines.evaluation.component import evaluate_model
    from pipelines.deployment.component import register_model
    
    ingest_task = ingest_data(s3_path=s3_raw_data_path)
    
    validate_task = validate_data(dataset=ingest_task.outputs['dataset'])
    
    preprocess_task = preprocess_data(dataset_in=ingest_task.outputs['dataset']).after(validate_task)
    
    train_task = train_model(
        dataset=preprocess_task.outputs['dataset_out'],
        learning_rate=learning_rate,
        n_estimators=n_estimators
    )
    
    eval_task = evaluate_model(
        dataset=preprocess_task.outputs['dataset_out'],
        model=train_task.outputs['model']
    )
    
    # Example conditional registration based on some metric could go here
    # register_task = register_model(model=train_task.outputs['model'], metrics={})

if __name__ == '__main__':
    compiler.Compiler().compile(
        pipeline_func=enterprise_ml_pipeline,
        package_path='enterprise_ml_pipeline.json'
    )
