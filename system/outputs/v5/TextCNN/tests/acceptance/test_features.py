import unittest
import torch
from src.main import main
from src.model.text_cnn import TextCNN
from src.data.data_loader import DataLoader
from src.training.trainer import Trainer
from src.utils.logger import Logger
from src.training.checkpoint_manager import CheckpointManager
import os


class TestFeatures(unittest.TestCase):
    def setUp(self):
        # Set up necessary components for testing
        self.output_dir = './outputs'
        os.makedirs(self.output_dir, exist_ok=True)
        self.data_loader = DataLoader()
        self.logger = Logger()
        self.checkpoint_manager = CheckpointManager(self.output_dir)

        # Load data
        self.train_data, self.val_data, self.test_data = self.data_loader.load_data()

        # Initialize model
        self.model = TextCNN(embedding_dim=300, kernel_sizes=[3, 4, 5], max_length=50)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(self.device)

        # Initialize trainer
        self.trainer = Trainer(model=self.model, train_data=self.train_data, val_data=self.val_data, test_data=self.test_data,
                               learning_rate=0.01, batch_size=16, num_epochs=10, device=self.device,
                               logger=self.logger, checkpoint_manager=self.checkpoint_manager,
                               train_log_per_k_batch=20, save_every_n_epoch=2)

    def test_training_mode(self):
        # Test training mode
        self.trainer.train()

        # Check if the model training logs show decreasing loss and accuracy above 0.6
        train_accuracy = self.trainer.evaluate(DataLoader(self.train_data, batch_size=16))
        val_accuracy = self.trainer.evaluate(DataLoader(self.val_data, batch_size=16))

        self.assertGreaterEqual(train_accuracy, 0.6, "Training accuracy should be at least 0.6")
        self.assertGreaterEqual(val_accuracy, 0.6, "Validation accuracy should be at least 0.6")

    def test_testing_mode(self):
        # Test testing mode
        self.trainer.train()  # Ensure the model is trained
        test_accuracy = self.trainer.evaluate()

        # Check if the test accuracy is above 0.6
        self.assertGreaterEqual(test_accuracy, 0.6, "Test accuracy should be at least 0.6")


if __name__ == '__main__':
    unittest.main()
