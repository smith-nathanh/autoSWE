import os
import pandas as pd
from .utils.csv_handler import CSVHandler
from .utils.progress_bar import ProgressBar

class Chakin:
    def __init__(self):
        self.csv_handler = CSVHandler()
        self.datasets = self.csv_handler.parseCSV()

    def search(self, lang):
        results = [dataset for dataset in self.datasets if dataset.language.lower() == lang.lower()]
        return results

    def download(self, number, save_dir):
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        dataset = self.datasets[number]
        url = dataset.url
        file_path = os.path.join(save_dir, f"{dataset.name}.vec.gz")
        self._download_file(url, file_path)

    def _download_file(self, url, file_path):
        import requests
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        progress = ProgressBar(total_size)
        with open(file_path, 'wb') as file:
            for data in response.iter_content(1024):
                file.write(data)
                progress.update(len(data))
        progress.finish()
