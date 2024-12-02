# chakin/chakin.py

import os
import requests
from .csv_handler import CSVHandler
from .progress_bar import ProgressBar

class Chakin:
    def __init__(self, csv_path='datasets.csv'):
        self.csv_handler = CSVHandler()
        self.datasets = self.csv_handler.load_csv(csv_path)

    def search(self, lang: str):
        results = self.csv_handler.search_by_language(lang)
        return [dataset.Name for dataset in results]

    def download(self, number: int, save_dir: str):
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        dataset = self.datasets[number]
        url = dataset.URL
        file_name = os.path.join(save_dir, url.split('/')[-1])

        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        progress_bar = ProgressBar(total_size)

        with open(file_name, 'wb') as f:
            for data in response.iter_content(1024):
                f.write(data)
                progress_bar.update(len(data))

        progress_bar.finish()
