import unittest
import pandas as pd
from src.financial_data_processor import FinancialDataProcessor
from src.indicator_calculator import IndicatorCalculator
from src.test_validator import TestValidator

class TestFeatures(unittest.TestCase):
    def setUp(self):
        self.data_processor = FinancialDataProcessor()
        self.indicator_calculator = IndicatorCalculator()
        self.validator = TestValidator()

    def test_renko_indicator_acceptance(self):
        # Load and preprocess data
        data = self.data_processor.load_data('project_root/acceptance_samples/HOOLI.csv')
        processed_data = self.data_processor.preprocess_data(data)

        # Calculate Renko indicator
        renko_data = self.indicator_calculator.calculate_renko(processed_data, brick_size=4)

        # Load expected data
        expected_data = self.data_processor.load_data('project_root/acceptance_samples/hooli_renko_4.csv')

        # Validate Renko indicator
        self.assertTrue(self.validator.validate_renko(renko_data, expected_data))

    def test_line_break_indicator_acceptance(self):
        # Load and preprocess data
        data = self.data_processor.load_data('project_root/acceptance_samples/HOOLI.csv')
        processed_data = self.data_processor.preprocess_data(data)

        # Calculate Line Break indicator
        line_break_data = self.indicator_calculator.calculate_line_break(processed_data, line_count=3)

        # Load expected data
        expected_data = self.data_processor.load_data('project_root/acceptance_samples/hooli_linebreak_3.csv')

        # Validate Line Break indicator
        self.assertTrue(self.validator.validate_line_break(line_break_data, expected_data))

if __name__ == '__main__':
    unittest.main()
