import unittest
import torch
from torch.utils.data import Dataset
from src.data.data_loader import DataLoader
from src.model.text_cnn import TextCNN
from src.training.trainer import Trainer
from src.utils.logger import Logger
from src.training.checkpoint_manager import CheckpointManager
import os

class MockDataset(Dataset):
    def __init__(self, size=100):
        self.size = size
        self.data = [{'text': 'This is a sample text.', 'label': 1} for _ in range(size)]

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return self.data[idx]

    def map(self, func, batched=False):
        if batched:
            return [func(self.data)]
        return [func(item) for item in self.data]

class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.data_loader = DataLoader()

    def test_load_data(self):
        train_data, val_data, test_data = self.data_loader.load_data()
        self.assertIsNotNone(train_data)
        self.assertIsNotNone(val_data)
        self.assertIsNotNone(test_data)

    def test_preprocess_data(self):
        dataset = MockDataset()
        train_data, val_data = self.data_loader.preprocess_data(dataset)
        self.assertIsNotNone(train_data)
        self.assertIsNotNone(val_data)

class TestTextCNN(unittest.TestCase):
    def setUp(self):
        self.model = TextCNN(embedding_dim=300, kernel_sizes=[3, 4, 5], max_length=50)

    def test_forward(self):
        input_data = torch.randint(0, 1000, (32, 50))  # Batch of 32, sequence length of 50
        output = self.model(input_data)
        self.assertEqual(output.shape, (32, 1))

    def test_invalid_input(self):
        with self.assertRaises(RuntimeError):
            input_data = torch.randint(1000, 2000, (32, 50))  # Invalid input range
            self.model(input_data)

class TestTrainer(unittest.TestCase):
    def setUp(self):
        self.model = TextCNN(embedding_dim=300, kernel_sizes=[3, 4, 5], max_length=50)
        self.logger = Logger()
        self.checkpoint_manager = CheckpointManager(output_dir='./outputs')
        self.trainer = Trainer(model=self.model, train_data=MockDataset(), val_data=MockDataset(), test_data=MockDataset(),
                               learning_rate=0.01, batch_size=16, num_epochs=1, device='cpu',
                               logger=self.logger, checkpoint_manager=self.checkpoint_manager,
                               train_log_per_k_batch=1, save_every_n_epoch=1)

    def test_train(self):
        self.trainer.train()

    def test_evaluate(self):
        accuracy = self.trainer.evaluate()
        self.assertIsInstance(accuracy, float)

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
