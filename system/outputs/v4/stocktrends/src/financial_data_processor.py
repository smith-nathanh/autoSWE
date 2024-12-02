import pandas as pd

class FinancialDataProcessor:
    def load_data(self, file_path: str) -> pd.DataFrame:
        """
        Load data from a CSV file.
        """
        return pd.read_csv(file_path)

    def preprocess_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocess the data by normalizing column names.
        """
        data.columns = [col.lower() for col in data.columns]
        return data