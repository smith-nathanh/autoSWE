import unittest
from unittest.mock import patch, MagicMock
import torch
from models.text_cnn import TextCNN
from data.data_loader import DataLoader
from tokenizer.tokenizer import Tokenizer
from trainer.trainer import Trainer


class TestTextCNN(unittest.TestCase):
    def setUp(self):
        self.embedding_dim = 300
        self.kernel_sizes = [3, 4, 5]
        self.max_length = 50
        self.model = TextCNN(self.embedding_dim, self.kernel_sizes, self.max_length)

    def test_textcnn_structure(self):
        # Check if the model has the correct layers
        self.assertIsInstance(self.model.embedding, torch.nn.EmbeddingBag)
        self.assertEqual(len(self.model.convs), len(self.kernel_sizes))
        self.assertIsInstance(self.model.fc, torch.nn.Linear)

    def test_textcnn_forward(self):
        # Check if the forward pass works
        input_data = torch.randint(0, 100, (32, self.max_length))
        output = self.model(input_data)
        self.assertEqual(output.shape, (32, 2))


class TestDataLoader(unittest.TestCase):
    @patch('data.data_loader.load_dataset')
    def test_load_data(self, mock_load_dataset):
        # Mock the dataset loading
        mock_load_dataset.return_value = {'train': [{'text': 'good movie'}], 'test': [{'text': 'bad movie'}]}
        tokenizer = MagicMock()
        tokenizer.tokenize.return_value = {'input_ids': [1, 2, 3], 'labels': 1}

        data_loader = DataLoader()
        train_data, val_data, test_data = data_loader.load_data(tokenizer)

        # Check if data is split correctly
        self.assertEqual(len(train_data), 1)
        self.assertEqual(len(test_data), 1)


class TestTokenizer(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer()

    def test_tokenize(self):
        # Check if the tokenizer returns the correct format
        text = "This is a test."
        result = self.tokenizer.tokenize(text)
        self.assertIn('input_ids', result)
        self.assertIn('attention_mask', result)


class TestTrainer(unittest.TestCase):
    def setUp(self):
        self.learning_rate = 0.01
        self.batch_size = 16
        self.num_epochs = 2
        self.save_every_n_epoch = 1
        self.output_dir = './outputs'
        self.train_log_per_k_batch = 10
        self.trainer = Trainer(self.learning_rate, self.batch_size, self.num_epochs,
                               self.save_every_n_epoch, self.output_dir, self.train_log_per_k_batch)

    @patch('trainer.trainer.TorchDataLoader')
    @patch('trainer.trainer.optim.Adam')
    def test_train(self, mock_adam, mock_data_loader):
        # Mock the data loader and optimizer
        mock_data_loader.return_value = MagicMock()
        mock_adam.return_value = MagicMock()

        model = MagicMock()
        train_data = MagicMock()
        val_data = MagicMock()
        device = torch.device('cpu')

        # Run train method
        self.trainer.train(model, train_data, val_data, device)

        # Check if optimizer and data loader are called
        mock_adam.assert_called_once()
        mock_data_loader.assert_called()

    @patch('trainer.trainer.TorchDataLoader')
    def test_evaluate(self, mock_data_loader):
        # Mock the data loader
        mock_data_loader.return_value = MagicMock()

        model = MagicMock()
        test_data = MagicMock()
        device = torch.device('cpu')

        # Run evaluate method
        self.trainer.evaluate(model, test_data, device)

        # Check if data loader is called
        mock_data_loader.assert_called()


if __name__ == '__main__':
    unittest.main()
