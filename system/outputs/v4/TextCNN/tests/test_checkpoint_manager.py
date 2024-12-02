import unittest
import os
import torch
from model.text_cnn import TextCNN
from training.checkpoint_manager import CheckpointManager


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


if __name__ == '__main__':
    unittest.main()
