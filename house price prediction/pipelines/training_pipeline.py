from steps.data_ingestion_step import data_ingestion_step
from steps.handle_missing_values_step import handle_missing_values_step

from zenml import Model, pipeline, step

@pipeline(
    model=Model(
        name ='house_price_predictor'
    )
)

def ml_pipeline():
    """define end to end machine learning pipeline"""
    #data ingestion step
    raw_data = data_ingestion_step(
        file_path = '/Users/sylvestermhlanga/Documents/GitHub/ML-projects/house price prediction/data/archive.zip'
    )

    #handle missing values step
    filled_data = handle_missing_data_step(raw_data)





    return model

if __name__ == '__main__':
    #running the pipeline
    run = ml_pipeline()
