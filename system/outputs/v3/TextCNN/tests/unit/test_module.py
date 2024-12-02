import unittest
from unittest.mock import patch, MagicMock
import torch
from config.config import Config
from data.data_loader import DataLoader
from models.text_cnn import TextCNN
from train.trainer import Trainer
from train.logger import Logger

class TestConfig(unittest.TestCase):
    def test_config_initialization(self):
        config = Config(0.01, 16, 10, 300, [3, 4, 5], 50, 2, True, False, './outputs', True, 20, 42)
        self.assertEqual(config.learning_rate, 0.01)
        self.assertEqual(config.batch_size, 16)
        self.assertEqual(config.num_epochs, 10)
        self.assertEqual(config.embedding_dim, 300)
        self.assertEqual(config.kernel_sizes, [3, 4, 5])
        self.assertEqual(config.max_length, 50)
        self.assertEqual(config.save_every_n_epoch, 2)
        self.assertTrue(config.train)
        self.assertFalse(config.test)
        self.assertEqual(config.output_dir, './outputs')
        self.assertTrue(config.gpu)
        self.assertEqual(config.train_log_per_k_batch, 20)
        self.assertEqual(config.random_seed, 42)

class TestDataLoader(unittest.TestCase):
    @patch('data.data_loader.BertTokenizer.from_pretrained')
    @patch('data.data_loader.load_dataset')
    def test_load_data(self, mock_load_dataset, mock_tokenizer):
        mock_tokenizer.return_value = MagicMock()
        mock_load_dataset.return_value = {'train': [
            {'text': 'Great movie!', 'label': 1},
            {'text': 'Bad movie!', 'label': 0}
        ], 'test': [
            {'text': 'Okay movie.', 'label': 1}
        ]}

        config = Config(0.01, 16, 10, 300, [3, 4, 5], 50, 2, True, False, './outputs', True, 20, 42)
        data_loader = DataLoader(config)
        train_data, val_data, test_data = data_loader.load_data()

        self.assertEqual(len(train_data.dataset), 1)  # 90% of 2 is 1.8, rounded to 1
        self.assertEqual(len(val_data.dataset), 1)  # 10% of 2 is 0.2, rounded to 1
        self.assertEqual(len(test_data.dataset), 1)

class TestTextCNN(unittest.TestCase):
    def test_text_cnn_forward(self):
        config = Config(0.01, 16, 10, 300, [3, 4, 5], 50, 2, True, False, './outputs', True, 20, 42)
        model = TextCNN(config)
        input_data = torch.randint(0, 30522, (16, 50))  # batch_size x max_length
        output = model(input_data)
        self.assertEqual(output.shape, (16, 2))  # batch_size x num_classes

class TestLogger(unittest.TestCase):
    @patch('builtins.print')
    def test_log_training_loss(self, mock_print):
        logger = Logger()
        logger.log_training_loss(0, 0, 0.5)
        mock_print.assert_called_with('Epoch [1], Batch [1], Loss: 0.5000')

    @patch('builtins.print')
    def test_log_accuracy(self, mock_print):
        logger = Logger()
        logger.log_accuracy(0, 0.75)
        mock_print.assert_called_with('Epoch [1], Validation Accuracy: 0.7500')

    @patch('builtins.print')
    def test_log_test_accuracy(self, mock_print):
        logger = Logger()
        logger.log_test_accuracy(0.8)
        mock_print.assert_called_with('Test Accuracy: 0.8000')

class TestTrainer(unittest.TestCase):
    @patch('train.trainer.Logger')
    @patch('train.trainer.optim.Adam')
    @patch('train.trainer.nn.CrossEntropyLoss')
    def test_trainer_train(self, mock_loss, mock_optim, mock_logger):
        config = Config(0.01, 16, 1, 300, [3, 4, 5], 50, 1, True, False, './outputs', False, 1, 42)
        model = MagicMock()
        train_data = [
            {'input_ids': torch.randint(0, 30522, (16, 50)), 'label': torch.randint(0, 2, (16,))}
        ]
        val_data = train_data
        test_data = train_data

        trainer = Trainer(config, model, train_data, val_data, test_data)
        trainer.train()

        self.assertTrue(mock_logger.return_value.log_training_loss.called)
        self.assertTrue(mock_logger.return_value.log_accuracy.called)

    @patch('train.trainer.Logger')
    def test_trainer_evaluate(self, mock_logger):
        config = Config(0.01, 16, 1, 300, [3, 4, 5], 50, 1, False, True, './outputs', False, 1, 42)
        model = MagicMock()
        test_data = [
            {'input_ids': torch.randint(0, 30522, (16, 50)), 'label': torch.randint(0, 2, (16,))}
        ]

        trainer = Trainer(config, model, test_data, test_data, test_data)
        accuracy = trainer.evaluate()

        self.assertTrue(mock_logger.return_value.log_accuracy.called)
        self.assertIsInstance(accuracy, float)

if __name__ == '__main__':
    unittest.main()
