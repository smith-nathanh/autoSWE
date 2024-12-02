import unittest
from src.financial_data_processor import FinancialDataProcessor
import pandas as pd

class TestFinancialDataProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = FinancialDataProcessor()

    def test_load_data(self):
        data = self.processor.load_data('project_root/unit_samples/HOOLI.csv')
        self.assertIsInstance(data, pd.DataFrame)

    def test_preprocess_data(self):
        data = pd.DataFrame({'Date': ["2021-01-01"], 'Open': [100]})
        processed_data = self.processor.preprocess_data(data)
        self.assertIn('date', processed_data.columns)

if __name__ == '__main__':
    unittest.main()
