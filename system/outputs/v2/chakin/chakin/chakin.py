import os
import pandas as pd
from .utils.csv_handler import CSVHandler
from .utils.progress_bar import ProgressBar

class Chakin:
    def __init__(self):
        self.csv_handler = CSVHandler()
        self.datasets = self.csv_handler.loadCSV('./chakin/datasets.csv')

    def search(self, lang: str):
        results = [dataset for dataset in self.datasets if dataset.language.lower() == lang.lower()]
        return results

    def download(self, number: int, save_dir: str):
        if number < 0 or number >= len(self.datasets):
            raise ValueError("Invalid dataset number.")
        dataset = self.datasets[number]
        url = dataset.url
        file_name = os.path.join(save_dir, os.path.basename(url))
        self._download_file(url, file_name)

    def _download_file(self, url: str, file_name: str):
        # Simulate download with progress bar
        progress = ProgressBar()
        progress.start()
        # Here you would add the actual download logic
        progress.finish()