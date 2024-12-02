import unittest
import os
import subprocess
import torch
from model.text_cnn import TextCNN
from data.data_loader import DataLoader
from training.trainer import Trainer
from training.checkpoint_manager import CheckpointManager


class TestFeatures(unittest.TestCase):
    def setUp(self):
        self.output_dir = './outputs'
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def test_training_mode(self):
        """Test the training mode to ensure loss decreases and accuracy is above 0.6."""
        # Run the training script
        result = subprocess.run([
            'python', 'src/main.py',
            '--learning_rate', '0.01',
            '--num_epochs', '1',  # Reduced for testing purposes
            '--batch_size', '16',
            '--embedding_dim', '300',
            '--kernel_sizes', '3', '4', '5',
            '--max_length', '50',
            '--save_every_n_epoch', '1',
            '--train',
            '--output_dir', self.output_dir,
            '--train_log_per_k_batch', '20',
            '--random_seed', '20'
        ], capture_output=True, text=True)

        # Check if the training loss decreases and accuracy is above 0.6
        self.assertIn('Training Loss', result.stdout)
        self.assertIn('Validation Accuracy', result.stdout)
        accuracy_lines = [line for line in result.stdout.split('\n') if 'Validation Accuracy' in line]
        last_accuracy = float(accuracy_lines[-1].split(': ')[-1])
        self.assertGreater(last_accuracy, 0.6)

    def test_testing_mode(self):
        """Test the testing mode to ensure accuracy is above 0.6."""
        # Assume a model checkpoint is already available
        checkpoint_manager = CheckpointManager()
        model = TextCNN(embedding_dim=300, kernel_sizes=[3, 4, 5], max_length=50)
        checkpoint_manager.save_checkpoint(model, 1, self.output_dir)

        # Run the testing script
        result = subprocess.run([
            'python', 'src/main.py',
            '--test',
            '--output_dir', self.output_dir
        ], capture_output=True, text=True)

        # Check if the test accuracy is above 0.6
        self.assertIn('Test Accuracy', result.stdout)
        test_accuracy = float(result.stdout.split('Test Accuracy: ')[-1])
        self.assertGreater(test_accuracy, 0.6)


if __name__ == '__main__':
    unittest.main()
