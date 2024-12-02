import pandas as pd

class FinancialDataProcessor:
    def load_data(self, file_path: str) -> pd.DataFrame:
        return pd.read_csv(file_path)

    def preprocess_data(self, data: pd.DataFrame) -> pd.DataFrame:
        data.columns = map(str.lower, data.columns)
        return data
