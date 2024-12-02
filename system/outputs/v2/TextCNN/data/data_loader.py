from datasets import load_dataset
from sklearn.model_selection import train_test_split


class DataLoader:
    def load_data(self, tokenizer):
        # Load IMDb dataset
        dataset = load_dataset('imdb')
        train_data, test_data = dataset['train'], dataset['test']

        # Tokenize data
        train_data = self.preprocess_data(train_data, tokenizer)
        test_data = self.preprocess_data(test_data, tokenizer)

        # Split train data into train and validation
        train_data, val_data = train_test_split(train_data, test_size=0.1, random_state=42)

        return train_data, val_data, test_data

    def preprocess_data(self, data, tokenizer):
        # Tokenize the text
        data = data.map(lambda x: tokenizer.tokenize(x['text']), batched=True)
        return data