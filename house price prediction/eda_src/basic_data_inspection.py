from abc import ABC, abstractmethod

import pandas as pd

#Base abstract class for data inspection strategies

class DataInspectionStrategy(ABC):
    abstractmethod
    def inspect(self, df: pd.DataFrame):
        """perform a specific type of data inspection

        Params: 
        df (pd.DataFrame): the dataframe to be inspected

        Returns:
        None: this prints the inspection resutls directly
        """

#This strategy inpects the data types of each column and counts non-null values
class DataTypesInspectionStrategy(DataInspectionStrategy):
    
    def inspect(self, df: pd.DataFrame):
        """
        Inspects and prints the data types and non-null counts of the dataframe columns.

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Prints the data types and non-null counts to the console.
        """
        print("\nData Types and Non-null Counts:")
        print(df.info())

# This strategy provides summary statistics for both numerical and categorical features.
class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        Prints summary statistics for numerical and categorical features.

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Prints summary statistics to the console.
        """
        print("\nSummary Statistics (Numerical Features):")
        print(df.describe())
        print("\nSummary Statistics (Categorical Features):")
        print(df.describe(include=["O"]))

# Context Class that uses a DataInspectionStrategy
# ------------------------------------------------
# This class allows you to switch between different data inspection strategies.
class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        """
        Initializes the DataInspector with a specific inspection strategy.

        Parameters:
        strategy (DataInspectionStrategy): The strategy to be used for data inspection.

        Returns:
        None
        """
        self._strategy = strategy

    def set_strategy(self, strategy, DataInspectionStrategy):

        """
        Sets a new strategy for the DataInspector.

        Parameters:
        strategy (DataInspectionStrategy): The new strategy to be used for data inspection.

        Returns:
        None
        """
        self._strategy = strategy

    def execute_inspection(self, df: pd.DataFrame):
        """Executes the inspection using the current strategy

        Parameters:
        df (pd.DataFrame): The dataframe to be inspected.

        Returns:
        None: Executes the strategy's inspection method.
        """

        self._strategy.inspect(df)

if __name__ == "__main__":
    df = pd.read_csv('/Users/sylvestermhlanga/house prediction system/extracted_data/AmesHousing.csv')

    inspector = DataInspector(DataTypesInspectionStrategy())
    inspector.execute_inspection(df)



