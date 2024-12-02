import unittest
import pandas as pd
from src.financial_data_processor import FinancialDataProcessor
from src.indicator_calculator import IndicatorCalculator
from src.test_validator import TestValidator

class TestFeatures(unittest.TestCase):
    def setUp(self):
        self.processor = FinancialDataProcessor()
        self.calculator = IndicatorCalculator()
        self.validator = TestValidator()

        # Load and preprocess data
        self.data = self.processor.load_data('data/acceptance_samples/HOOLI.csv')
        self.preprocessed_data = self.processor.preprocess_data(self.data)

    def test_renko_indicator(self):
        # Calculate Renko data
        renko_data = self.calculator.calculate_renko(self.preprocessed_data, brick_size=4)
        # Load expected data
        expected_data = self.processor.load_data('data/acceptance_samples/hooli_renko_4.csv')
        expected_data = self.processor.preprocess_data(expected_data)
        # Validate
        self.assertTrue(self.validator.validate_renko(renko_data, expected_data))

    def test_line_break_indicator(self):
        # Calculate Line Break data
        line_break_data = self.calculator.calculate_line_break(self.preprocessed_data, line_count=3)
        # Load expected data
        expected_data = self.processor.load_data('data/acceptance_samples/hooli_linebreak_3.csv')
        expected_data = self.processor.preprocess_data(expected_data)
        # Validate
        self.assertTrue(self.validator.validate_line_break(line_break_data, expected_data))

if __name__ == '__main__':
    unittest.main()
