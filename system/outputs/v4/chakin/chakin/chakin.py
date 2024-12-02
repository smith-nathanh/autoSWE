import pandas as pd
import progressbar
import os
import requests

class Chakin:
    def __init__(self):
        self.datasets = self._load_datasets()

    def _load_datasets(self):
        file_path = os.path.join(os.path.dirname(__file__), 'datasets.csv')
        df = pd.read_csv(file_path)
        return df

    def search(self, lang):
        results = self.datasets[self.datasets['Language'].str.contains(lang, case=False)]
        return results.to_dict('records')

    def download(self, number, save_dir):
        dataset = self.datasets.iloc[number]
        url = dataset['URL']
        file_name = os.path.join(save_dir, os.path.basename(url))

        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024

        with open(file_name, 'wb') as file, progressbar.ProgressBar(max_value=total_size) as bar:
            for data in response.iter_content(block_size):
                file.write(data)
                bar.update(len(data))

        print(f"Downloaded {file_name}")
