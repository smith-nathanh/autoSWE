from datasets import load_dataset
from transformers import BertTokenizer
from torch.utils.data import DataLoader, random_split


class DataLoader:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    def load_data(self):
        # Load IMDb dataset
        dataset = load_dataset('imdb')
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Preprocess data
        train_data, val_data = self.preprocess_data(train_dataset)
        test_data = self.preprocess_data(test_dataset, train=False)

        return train_data, val_data, test_data

    def preprocess_data(self, dataset, train=True):
        # Tokenize and encode sequences
        def tokenize_function(examples):
            return self.tokenizer(examples['text'], padding='max_length', truncation=True, max_length=50)

        dataset = dataset.map(tokenize_function, batched=True)
        dataset.set_format(type='torch', columns=['input_ids', 'label'])

        if train:
            # Split train into train and validation
            train_size = int(0.9 * len(dataset))
            val_size = len(dataset) - train_size
            train_dataset, val_dataset = random_split(dataset, [train_size, val_size])
            return train_dataset, val_dataset
        else:
            return dataset