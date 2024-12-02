# chakin/csv_handler.py

import csv
from .dataset import Dataset

class CSVHandler:
    def load_csv(self, file_path: str):
        datasets = []
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dataset = Dataset(
                    Name=row['Name'],
                    Dimension=int(row['Dimension']),
                    Corpus=row['Corpus'],
                    VocabularySize=row['VocabularySize'],
                    Method=row['Method'],
                    Language=row['Language'],
                    Paper=row['Paper'],
                    Author=row['Author'],
                    URL=row['URL']
                )
                datasets.append(dataset)
        return datasets

    def search_by_language(self, language: str):
        return [dataset for dataset in self.datasets if dataset.Language.lower() == language.lower()]
