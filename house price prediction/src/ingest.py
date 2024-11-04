import os
import zipfile
from abc import ABC, abstractmethod
import pandas as pd


class DataIngestor(ABC):
  @abstractmethod
  def ingest(self, filepath: str) -> pd.DataFrame:
    pass

class ZipIngestor(DataIngestor):
  def ingest(self, filepath: str) -> pd.DataFrame:
    #ensure the file is a .zip
    if not filepath.endswith('.zip'):
      raise ValueError('The file provided is not a zip file')

    #extract files from zip
    with zipfile.ZipFile(filepath, 'r') as zip_ref:
      zip_ref.extractall('extracted_data')
    
    #find extracted csv file(s)
    extracted_files = os.listdir('extracted_data')
    csv_files = [file for file in extracted_files if file.endswith('.csv')]

    if len(csv_files) == 0:
      raise FileNotFoundError('No CSV files found in the zip file')
    if len(csv_files) > 1:
      raise ValueError('Multiple csv files found, please specify which one to read')

    csv_filepath = os.path.join('extracted_data', csv_files[0])
    df = pd.read_csv(csv_filepath)

    return df

class DataIngestorFactory:
  @staticmethod
  def get_data_ingestor(file_extension: str) -> DataIngestor:
    if file_extension == '.zip':
      return ZipIngestor()
    else:
      raise ValueError('No Ingestor available for the ile extension')

"""if __name__ == '__main__':
    filepath = '/Users/sylvestermhlanga/house prediction system/archive.zip'
    file_extension = os.path.splitext(filepath)[1]

    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)

    df = data_ingestor.ingest(filepath)

    print(df.head())"""