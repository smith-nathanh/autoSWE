import unittest
import torch
from src.model.text_cnn import TextCNN
from src.training.trainer import Trainer
from src.utils.logger import Logger
from src.training.checkpoint_manager import CheckpointManager


class TestTrainer(unittest.TestCase):
    def setUp(self):
        self.model = TextCNN(embedding_dim=300, kernel_sizes=[3, 4, 5], max_length=50)
        self.logger = Logger()
        self.checkpoint_manager = CheckpointManager(output_dir='./outputs')
        self.trainer = Trainer(model=self.model, train_data=[], val_data=[], test_data=[],
                               learning_rate=0.01, batch_size=16, num_epochs=1, device='cpu',
                               logger=self.logger, checkpoint_manager=self.checkpoint_manager,
                               train_log_per_k_batch=1, save_every_n_epoch=1)

    def test_train(self):
        # This is a placeholder test; in practice, you would use a mock dataset
        self.trainer.train()

    def test_evaluate(self):
        # This is a placeholder test; in practice, you would use a mock dataset
        accuracy = self.trainer.evaluate()
        self.assertIsInstance(accuracy, float)


if __name__ == '__main__':
    unittest.main()