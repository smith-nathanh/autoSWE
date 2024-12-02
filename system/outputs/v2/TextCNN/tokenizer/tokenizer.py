from transformers import BertTokenizer


class Tokenizer:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    def load_tokenizer(self):
        return self.tokenizer

    def tokenize(self, text):
        return self.tokenizer(text, padding='max_length', truncation=True, return_tensors='pt')