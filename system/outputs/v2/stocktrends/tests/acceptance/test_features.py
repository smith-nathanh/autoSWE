import unittest
import pandas as pd
from src.indicator_calculator import IndicatorCalculator

class TestFinancialIndicators(unittest.TestCase):
    def setUp(self):
        # Load sample data for testing
        self.sample_data = pd.read_csv('data/acceptance_samples/HOOLI.csv')
        self.expected_renko_data = pd.read_csv('data/acceptance_samples/hooli_renko_4.csv')
        self.expected_line_break_data = pd.read_csv('data/acceptance_samples/hooli_linebreak_3.csv')
        self.calculator = IndicatorCalculator()

    def test_renko_calculation(self):
        # Calculate Renko chart data
        renko_data = self.calculator.calculate_renko(self.sample_data, brick_size=4, chart_type='PERIOD_CLOSE')
        # Compare the calculated Renko data with expected data
        pd.testing.assert_frame_equal(renko_data, self.expected_renko_data, atol=1e-12)

    def test_line_break_calculation(self):
        # Calculate Line Break chart data
        line_break_data = self.calculator.calculate_line_break(self.sample_data, line_number=3)
        # Compare the calculated Line Break data with expected data
        pd.testing.assert_frame_equal(line_break_data, self.expected_line_break_data, atol=1e-12)

if __name__ == '__main__':
    unittest.main()
