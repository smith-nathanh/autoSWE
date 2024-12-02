import unittest
import torch
from model.text_cnn import TextCNN
from training.trainer import Trainer
from data.data_loader import DataLoader


class TestTrainer(unittest.TestCase):
    def setUp(self):
        self.data_loader = DataLoader()
        self.train_data, self.val_data, _ = self.data_loader.load_data()
        self.model = TextCNN(embedding_dim=300, kernel_sizes=[3, 4, 5], max_length=50)
        self.trainer = Trainer(learning_rate=0.01, batch_size=16, num_epochs=1, save_every_n_epoch=1,
                               train_log_per_k_batch=20, output_dir='./outputs', gpu=False)

    def test_train(self):
        self.trainer.train(self.model, self.train_data, self.val_data)

    def test_evaluate(self):
        accuracy = self.trainer.evaluate(self.model, self.val_data)
        self.assertIsInstance(accuracy, float)


if __name__ == '__main__':
    unittest.main()
