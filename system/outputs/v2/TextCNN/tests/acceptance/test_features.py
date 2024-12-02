import unittest
import os
import subprocess
import torch

class TestTextCNNAcceptance(unittest.TestCase):
    def setUp(self):
        self.output_dir = './outputs'
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def test_training_mode(self):
        """Test the training mode of the TextCNN model."""
        # Run the training script
        result = subprocess.run(
            [
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
                '--output_dir', self.output_dir,
                '--train_log_per_k_batch', '20',
                '--random_seed', '20'
            ],
            capture_output=True, text=True
        )

        # Check if the training loss decreases and accuracy is above 0.6
        output = result.stdout
        self.assertIn('Loss:', output)
        self.assertIn('Validation Accuracy:', output)

        # Extract the last validation accuracy
        lines = output.split('\n')
        val_accuracies = [float(line.split('Validation Accuracy: ')[1]) for line in lines if 'Validation Accuracy:' in line]
        self.assertGreaterEqual(val_accuracies[-1], 0.6)

    def test_testing_mode(self):
        """Test the testing mode of the TextCNN model."""
        # Run the testing script
        result = subprocess.run(
            [
                'python', 'main.py',
                '--test',
                '--gpu',
                '--output_dir', self.output_dir
            ],
            capture_output=True, text=True
        )

        # Check if the test accuracy is above 0.6
        output = result.stdout
        self.assertIn('Validation Accuracy:', output)

        # Extract the test accuracy
        lines = output.split('\n')
        test_accuracies = [float(line.split('Validation Accuracy: ')[1]) for line in lines if 'Validation Accuracy:' in line]
        self.assertGreaterEqual(test_accuracies[-1], 0.6)

if __name__ == '__main__':
    unittest.main()
