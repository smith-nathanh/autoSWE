import unittest
import pandas as pd
from src.indicator_calculator import IndicatorCalculator

class TestFeatures(unittest.TestCase):
    def setUp(self):
        self.calculator = IndicatorCalculator()
        self.hooli_data = pd.DataFrame({
            'date': ['2015/1/1', '2015/1/2'],
            'open': [143.15, 144.00],
            'high': [146, 147],
            'low': [141.825, 142.00],
            'close': [143.95, 145.00]
        })

    def test_renko_indicator(self):
        expected_renko_data = pd.DataFrame({
            'index': [0, 1],
            'date': ['2015/1/1', '2015/1/2'],
            'open': [136, 137],
            'high': [140, 141],
            'low': [136, 137],
            'close': [140, 141],
            'uptrend': [True, False]
        })
        renko_chart = self.calculator.calculate_renko(self.hooli_data, brick_size=4, chart_type='PERIOD_CLOSE')
        pd.testing.assert_frame_equal(renko_chart, expected_renko_data, atol=1e-12)

    def test_line_break_indicator(self):
        expected_line_break_data = pd.DataFrame({
            'index': [0, 1],
            'date': ['2015/1/1', '2015/1/2'],
            'open': [143.15, 144.00],
            'high': [146, 147],
            'low': [141.825, 142.00],
            'close': [143.95, 145.00],
            'uptrend': [True, False]
        })
        line_break_chart = self.calculator.calculate_line_break(self.hooli_data, line_number=3)
        pd.testing.assert_frame_equal(line_break_chart, expected_line_break_data, atol=1e-12)

if __name__ == '__main__':
    unittest.main()
