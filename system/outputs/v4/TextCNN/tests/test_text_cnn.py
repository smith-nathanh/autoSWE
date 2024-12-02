import unittest
import torch
from model.text_cnn import TextCNN


class TestTextCNN(unittest.TestCase):
    def setUp(self):
        self.model = TextCNN(embedding_dim=300, kernel_sizes=[3, 4, 5], max_length=50)

    def test_forward(self):
        input_data = torch.randint(0, 1000, (32, 50))  # Batch of 32, sequence length of 50
        output = self.model(input_data)
        self.assertEqual(output.shape, (32, 2))  # Assuming binary classification


if __name__ == '__main__':
    unittest.main()
