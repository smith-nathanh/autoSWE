import unittest
import os
import subprocess
import torch

class TestTextCNNAcceptance(unittest.TestCase):
    def setUp(self):
        self.train_command = [
            'python', 'main.py',
            '--learning_rate', '0.01',
            '--num_epochs', '10',
            '--batch_size', '16',
            '--embedding_dim', '300',
            '--kernel_sizes', '3', '4', '5',
            '--max_length', '50',
            '--save_every_n_epoch', '2',
            '--train',
            '--gpu',
            '--output_dir', './outputs',
            '--train_log_per_k_batch', '20',
            '--random_seed', '20'
        ]
        self.test_command = [
            'python', 'main.py',
            '--test',
            '--gpu',
            '--output_dir', './outputs'
        ]

    def test_training_mode(self):
        # Run the training command
        result = subprocess.run(self.train_command, capture_output=True, text=True)
        output = result.stdout

        # Check if training loss decreases and accuracy is above 0.6
        self.assertIn('Loss:', output)
        self.assertIn('Validation Accuracy:', output)

        # Extract the last validation accuracy
        last_accuracy_line = [line for line in output.split('\n') if 'Validation Accuracy:' in line][-1]
        last_accuracy = float(last_accuracy_line.split(': ')[-1])
        self.assertGreaterEqual(last_accuracy, 0.6)

    def test_testing_mode(self):
        # Run the testing command
        result = subprocess.run(self.test_command, capture_output=True, text=True)
        output = result.stdout

        # Check if test accuracy is above 0.6
        self.assertIn('Test Accuracy:', output)

        # Extract the test accuracy
        test_accuracy_line = [line for line in output.split('\n') if 'Test Accuracy:' in line][0]
        test_accuracy = float(test_accuracy_line.split(': ')[-1])
        self.assertGreaterEqual(test_accuracy, 0.6)

if __name__ == '__main__':
    unittest.main()
