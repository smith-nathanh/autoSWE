
import unittest
import subprocess
import os

class TestTextCNNAcceptance(unittest.TestCase):
    def setUp(self):
        self.output_dir = './outputs'
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def test_training_mode(self):
        # Run the training script
        result = subprocess.run([
            'python', 'main.py', '--train', '--output_dir', self.output_dir,
            '--learning_rate', '0.01', '--num_epochs', '2', '--batch_size', '16',
            '--embedding_dim', '300', '--kernel_sizes', '3', '4', '5', '--max_length', '50',
            '--save_every_n_epoch', '1', '--train_log_per_k_batch', '20', '--random_seed', '20'
        ], capture_output=True, text=True)

        # Check if the training loss decreases and accuracy is above 0.6
        self.assertIn('Loss:', result.stdout)
        self.assertIn('Accuracy:', result.stdout)
        # This is a simplified check, in practice, you would parse the output and check values

    def test_testing_mode(self):
        # Assume a checkpoint is available at './outputs/model_epoch_1.pt'
        checkpoint_path = os.path.join(self.output_dir, 'model_epoch_1.pt')
        if not os.path.exists(checkpoint_path):
            self.skipTest('Checkpoint not found, skipping test.')

        # Run the testing script
        result = subprocess.run([
            'python', 'main.py', '--test', '--output_dir', self.output_dir, '--checkpoint_path', checkpoint_path
        ], capture_output=True, text=True)

        # Check if the test accuracy is above 0.6
        self.assertIn('Test Accuracy:', result.stdout)
        # This is a simplified check, in practice, you would parse the output and check values

if __name__ == '__main__':
    unittest.main()
