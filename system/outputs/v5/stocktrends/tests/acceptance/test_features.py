import unittest
import pandas as pd
from src.financial_data_processor import FinancialDataProcessor
from src.indicator_calculator import IndicatorCalculator

class TestFeatures(unittest.TestCase):
    def setUp(self):
        self.processor = FinancialDataProcessor()
        self.calculator = IndicatorCalculator()
        
        # Load and preprocess data
        self.data = self.processor.load_data('data/acceptance_samples/HOOLI.csv')
        self.preprocessed_data = self.processor.preprocess_data(self.data)

    def test_renko_indicator(self):
        # Calculate Renko chart
        renko_data = self.calculator.calculate_renko(self.preprocessed_data, brick_size=4)
        expected_data = pd.read_csv('data/acceptance_samples/hooli_renko_4.csv')
        
        # Compare the closing prices
        self.assertEqual(len(renko_data), len(expected_data))
        for i in range(len(renko_data)):
            self.assertAlmostEqual(renko_data['renko_close'].iloc[i], expected_data['close'].iloc[i], places=12)

    def test_line_break_indicator(self):
        # Calculate Line Break chart
        line_break_data = self.calculator.calculate_line_break(self.preprocessed_data, line_count=3)
        expected_data = pd.read_csv('data/acceptance_samples/hooli_linebreak_3.csv')
        
        # Compare the closing prices
        self.assertEqual(len(line_break_data), len(expected_data))
        for i in range(len(line_break_data)):
            self.assertAlmostEqual(line_break_data['line_break_close'].iloc[i], expected_data['close'].iloc[i], places=12)

if __name__ == '__main__':
    unittest.main()
