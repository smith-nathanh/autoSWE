import pandas as pd
from .word_vector import WordVector

class DatasetManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def loadDatasets(self):
        df = pd.read_csv(self.file_path)
        return [WordVector(**row) for index, row in df.iterrows()]

    def getVectorsByLanguage(self, language):
        datasets = self.loadDatasets()
        return [vector for vector in datasets if vector.language == language]
