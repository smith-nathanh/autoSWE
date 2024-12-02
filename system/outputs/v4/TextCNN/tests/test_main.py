import unittest
from unittest.mock import patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from main import main


class TestMain(unittest.TestCase):
    @patch('argparse.ArgumentParser.parse_args')
    def test_train(self, mock_args):
        mock_args.return_value = argparse.Namespace(
            learning_rate=0.01,
            batch_size=16,
            num_epochs=1,
            embedding_dim=300,
            kernel_sizes=[3, 4, 5],
            max_length=50,
            save_every_n_epoch=1,
            train=True,
            test=False,
            output_dir='./outputs',
            gpu=False,
            train_log_per_k_batch=20,
            random_seed=20
        )
        main()

    @patch('argparse.ArgumentParser.parse_args')
    def test_test(self, mock_args):
        mock_args.return_value = argparse.Namespace(
            train=False,
            test=True,
            output_dir='./outputs',
            gpu=False
        )
        main()


if __name__ == '__main__':
    unittest.main()
