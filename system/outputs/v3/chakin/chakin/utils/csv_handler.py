import pandas as pd
from ..chakin import Dataset

class CSVHandler:
    def loadCSV(self, filePath):
        return pd.read_csv(filePath)

    def parseCSV(self):
        df = self.loadCSV('./chakin/datasets.csv')
        datasets = []
        for _, row in df.iterrows():
            dataset = Dataset(
                name=row['Name'],
                dimension=row['Dimension'],
                corpus=row['Corpus'],
                vocabularySize=row['VocabularySize'],
                method=row['Method'],
                language=row['Language'],
                paper=row['Paper'],
                author=row['Author'],
                url=row['URL']
            )
            datasets.append(dataset)
        return datasets
