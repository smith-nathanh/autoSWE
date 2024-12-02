from datasets import load_dataset
from transformers import BertTokenizer
from torch.utils.data import DataLoader, random_split


class DataLoader:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    def load_data(self):
        dataset = load_dataset('imdb')
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Tokenize and preprocess
        train_dataset = train_dataset.map(self.preprocess_data, batched=True)
        test_dataset = test_dataset.map(self.preprocess_data, batched=True)

        # Split train into train and validation
        train_size = int(0.9 * len(train_dataset))
        val_size = len(train_dataset) - train_size
        train_dataset, val_dataset = random_split(train_dataset, [train_size, val_size])

        return train_dataset, val_dataset, test_dataset

    def preprocess_data(self, examples):
        return self.tokenizer(examples['text'], padding='max_length', truncation=True, max_length=50)
