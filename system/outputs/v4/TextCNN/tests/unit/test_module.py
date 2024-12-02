
import unittest
from unittest.mock import patch, MagicMock
import torch
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from main import main
from model.text_cnn import TextCNN
from data.data_loader import DataLoader
from training.trainer import Trainer
from training.checkpoint_manager import CheckpointManager


class TestMain(unittest.TestCase):
    @patch('argparse.ArgumentParser.parse_args')
    def test_train(self, mock_args):
        mock_args.return_value = argparse.Namespace(
            learning_rate=0.01,
            batch_size=16,
            num_epochs=1,
            embedding_dim=300,
            kernel_sizes=[3, 4, 5],
            max_length=50,
            save_every_n_epoch=1,
            train=True,
            test=False,
            output_dir='./outputs',
            gpu=False,
            train_log_per_k_batch=20,
            random_seed=20
        )
        with patch('main.Trainer.train') as mock_train:
            main()
            mock_train.assert_called_once()

    @patch('argparse.ArgumentParser.parse_args')
    def test_test(self, mock_args):
        mock_args.return_value = argparse.Namespace(
            train=False,
            test=True,
            output_dir='./outputs',
            gpu=False
        )
        with patch('main.Trainer.evaluate', return_value=0.7) as mock_evaluate:
            with patch('main.CheckpointManager.load_checkpoint') as mock_load:
                main()
                mock_load.assert_called_once()
                mock_evaluate.assert_called_once()


class TestTextCNN(unittest.TestCase):
    def setUp(self):
        self.model = TextCNN(embedding_dim=300, kernel_sizes=[3, 4, 5], max_length=50)

    def test_forward(self):
        input_data = torch.randint(0, 1000, (32, 50))  # Batch of 32, sequence length of 50
        output = self.model(input_data)
        self.assertEqual(output.shape, (32, 2))  # Assuming binary classification

    def test_invalid_input(self):
        with self.assertRaises(RuntimeError):
            input_data = torch.randint(0, 1000, (32, 60))  # Invalid sequence length
            self.model(input_data)


class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.data_loader = DataLoader()

    def test_load_data(self):
        train_data, val_data, test_data = self.data_loader.load_data()
        self.assertIsNotNone(train_data)
        self.assertIsNotNone(val_data)
        self.assertIsNotNone(test_data)

    def test_preprocess_data(self):
        examples = {'text': ['This is a test sentence.']}
        processed = self.data_loader.preprocess_data(examples)
        self.assertIn('input_ids', processed)


class TestTrainer(unittest.TestCase):
    def setUp(self):
        self.data_loader = DataLoader()
        self.train_data, self.val_data, _ = self.data_loader.load_data()
        self.model = TextCNN(embedding_dim=300, kernel_sizes=[3, 4, 5], max_length=50)
        self.trainer = Trainer(learning_rate=0.01, batch_size=16, num_epochs=1, save_every_n_epoch=1,
                               train_log_per_k_batch=20, output_dir='./outputs', gpu=False)

    def test_train(self):
        with patch('training.trainer.DataLoader', return_value=MagicMock()) as mock_loader:
            self.trainer.train(self.model, self.train_data, self.val_data)
            mock_loader.assert_called()

    def test_evaluate(self):
        accuracy = self.trainer.evaluate(self.model, self.val_data)
        self.assertIsInstance(accuracy, float)


class TestCheckpointManager(unittest.TestCase):
    def setUp(self):
        self.model = TextCNN(embedding_dim=300, kernel_sizes=[3, 4, 5], max_length=50)
        self.checkpoint_manager = CheckpointManager()
        self.output_dir = './outputs'
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def test_save_and_load_checkpoint(self):
        self.checkpoint_manager.save_checkpoint(self.model, 1, self.output_dir)
        loaded_model = self.checkpoint_manager.load_checkpoint(os.path.join(self.output_dir, 'model_epoch_1.pth'))
        self.assertIsNotNone(loaded_model)

    def test_load_checkpoint_invalid_path(self):
        with self.assertRaises(FileNotFoundError):
            self.checkpoint_manager.load_checkpoint('invalid_path.pth')


if __name__ == '__main__':
    unittest.main()
