import datasets
from transformers import BertTokenizer
from torch.utils.data import DataLoader, random_split

class DataLoader:
    def __init__(self, batch_size=32, max_length=50):
        self.batch_size = batch_size
        self.max_length = max_length
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    def load_data(self):
        dataset = datasets.load_dataset('imdb')
        return dataset

    def preprocess_data(self, dataset):
        def tokenize_function(examples):
            return self.tokenizer(examples['text'], padding='max_length', truncation=True, max_length=self.max_length)

        tokenized_datasets = dataset.map(tokenize_function, batched=True)
        return tokenized_datasets

    def get_data_loaders(self, dataset):
        train_size = int(0.9 * len(dataset['train']))
        val_size = len(dataset['train']) - train_size
        train_dataset, val_dataset = random_split(dataset['train'], [train_size, val_size])

        train_loader = DataLoader(train_dataset, batch_size=self.batch_size, shuffle=True)
        val_loader = DataLoader(val_dataset, batch_size=self.batch_size)
        test_loader = DataLoader(dataset['test'], batch_size=self.batch_size)

        return train_loader, val_loader, test_loader
