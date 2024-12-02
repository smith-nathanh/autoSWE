from datasets import load_dataset
from transformers import BertTokenizer
from torch.utils.data import DataLoader, random_split


class DataLoader:
    def __init__(self, config):
        self.config = config
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    def load_data(self):
        dataset = load_dataset('imdb')
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        train_size = int(0.9 * len(train_dataset))
        val_size = len(train_dataset) - train_size
        train_dataset, val_dataset = random_split(train_dataset, [train_size, val_size])

        train_data = self.preprocess_data(train_dataset)
        val_data = self.preprocess_data(val_dataset)
        test_data = self.preprocess_data(test_dataset)

        return train_data, val_data, test_data

    def preprocess_data(self, dataset):
        def tokenize_function(examples):
            return self.tokenizer(examples['text'], padding='max_length', truncation=True, max_length=self.config.max_length)

        tokenized_datasets = dataset.map(tokenize_function, batched=True)
        return DataLoader(tokenized_datasets, batch_size=self.config.batch_size, shuffle=True)