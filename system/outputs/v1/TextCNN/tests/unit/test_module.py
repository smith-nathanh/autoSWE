import unittest
from unittest.mock import patch, MagicMock
import torch
from data.data_loader import DataLoader
from models.text_cnn import TextCNN
from trainers.trainer import Trainer
from utils.checkpoint_manager import CheckpointManager

class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.data_loader = DataLoader(batch_size=16, max_length=50)

    @patch('datasets.load_dataset')
    def test_load_data(self, mock_load_dataset):
        mock_load_dataset.return_value = {'train': [], 'test': []}
        dataset = self.data_loader.load_data()
        self.assertIn('train', dataset)
        self.assertIn('test', dataset)

    @patch('transformers.BertTokenizer.from_pretrained')
    def test_preprocess_data(self, mock_tokenizer):
        mock_tokenizer.return_value = MagicMock()
        dataset = {'train': [{'text': 'sample text'}]}
        tokenized_datasets = self.data_loader.preprocess_data(dataset)
        self.assertIn('train', tokenized_datasets)

class TestTextCNN(unittest.TestCase):
    def setUp(self):
        self.model = TextCNN(embedding_dim=300, kernel_sizes=[3, 4, 5], max_length=50)

    def test_forward(self):
        input_data = torch.randint(0, 1000, (32, 50))
        output = self.model(input_data)
        self.assertEqual(output.shape, (32, 2))

class TestTrainer(unittest.TestCase):
    def setUp(self):
        self.model = MagicMock()
        self.trainer = Trainer(self.model, learning_rate=0.01, batch_size=16, num_epochs=2, device='cpu')

    @patch('torch.optim.Adam')
    @patch('torch.nn.CrossEntropyLoss')
    def test_train(self, mock_loss, mock_optimizer):
        mock_loss.return_value = MagicMock()
        mock_optimizer.return_value = MagicMock()
        train_loader = [
            {'input_ids': torch.randint(0, 1000, (16, 50)), 'label': torch.randint(0, 2, (16,))}
        ]
        val_loader = [
            {'input_ids': torch.randint(0, 1000, (16, 50)), 'label': torch.randint(0, 2, (16,))}
        ]
        self.trainer.train(train_loader, val_loader)
        self.assertTrue(self.model.to.called)

    @patch('torch.no_grad')
    def test_evaluate(self, mock_no_grad):
        data_loader = [
            {'input_ids': torch.randint(0, 1000, (16, 50)), 'label': torch.randint(0, 2, (16,))}
        ]
        accuracy = self.trainer.evaluate(data_loader)
        self.assertIsInstance(accuracy, float)

class TestCheckpointManager(unittest.TestCase):
    def setUp(self):
        self.checkpoint_manager = CheckpointManager(output_dir='./outputs')
        self.model = MagicMock()

    @patch('torch.save')
    def test_save_checkpoint(self, mock_save):
        self.checkpoint_manager.save_checkpoint(self.model, 1)
        mock_save.assert_called_once()

    @patch('torch.load')
    def test_load_checkpoint(self, mock_load):
        mock_load.return_value = MagicMock()
        self.checkpoint_manager.load_checkpoint(self.model, './outputs/model_epoch_1.pt')
        self.model.load_state_dict.assert_called_once()

if __name__ == '__main__':
    unittest.main()
