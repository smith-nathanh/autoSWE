import pandas as pd
from ..chakin import Dataset

class CSVHandler:
    def loadCSV(self, filePath: str):
        df = pd.read_csv(filePath)
        datasets = [Dataset(**row) for index, row in df.iterrows()]
        return datasets