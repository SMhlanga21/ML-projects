import pandas as pd
from src.ingest import DataIngestorFactory
from zenml import step

@step 
def data_ingestion_step(filepath: str) -> pd.DataFrame:
    """Ingest data from a zip file using the appropriate DataIngestor"""

    #determine file extension
    file_extension = '.zip'

    #get the appropriate DataIngestor
    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)

    df = data_ingester(filepath)

    return df

    