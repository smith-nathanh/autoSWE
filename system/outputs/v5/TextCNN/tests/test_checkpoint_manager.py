import unittest
import os
import torch
from src.model.text_cnn import TextCNN
from src.training.checkpoint_manager import CheckpointManager


class TestCheckpointManager(unittest.TestCase):
    def setUp(self):
        self.output_dir = './outputs'
        self.checkpoint_manager = CheckpointManager(self.output_dir)
        self.model = TextCNN(embedding_dim=300, kernel_sizes=[3, 4, 5], max_length=50)

    def test_save_checkpoint(self):
        self.checkpoint_manager.save_checkpoint(self.model, 0, 0.0)
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'model_epoch_0_acc_0.00.pt')))

    def test_load_checkpoint(self):
        checkpoint_path = os.path.join(self.output_dir, 'model_epoch_0_acc_0.00.pt')
        self.checkpoint_manager.save_checkpoint(self.model, 0, 0.0)
        loaded_model = self.checkpoint_manager.load_checkpoint(self.model, checkpoint_path)
        self.assertIsNotNone(loaded_model)


if __name__ == '__main__':
    unittest.main()