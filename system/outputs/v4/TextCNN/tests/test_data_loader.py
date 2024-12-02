import unittest
from data.data_loader import DataLoader


class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.data_loader = DataLoader()

    def test_load_data(self):
        train_data, val_data, test_data = self.data_loader.load_data()
        self.assertIsNotNone(train_data)
        self.assertIsNotNone(val_data)
        self.assertIsNotNone(test_data)


if __name__ == '__main__':
    unittest.main()
