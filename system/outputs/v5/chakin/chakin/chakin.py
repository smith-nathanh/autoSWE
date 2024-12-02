import os
from .dataset_manager import DatasetManager
from .progress_bar import ProgressBar

class Chakin:
    def __init__(self, dataset_path='datasets.csv'):
        self.dataset_manager = DatasetManager(dataset_path)

    def search(self, lang):
        vectors = self.dataset_manager.getVectorsByLanguage(lang)
        return vectors

    def download(self, number, save_dir):
        vectors = self.dataset_manager.loadDatasets()
        if number < 0 or number >= len(vectors):
            raise ValueError("Invalid vector number.")
        vector = vectors[number]
        self._download_vector(vector.url, save_dir)

    def _download_vector(self, url, save_dir):
        progress_bar = ProgressBar()
        progress_bar.start()
        # Simulate download with progress
        for i in range(100):
            progress_bar.update(i + 1)
        progress_bar.finish()
        print(f"Downloaded to {os.path.join(save_dir, os.path.basename(url))}")
