import unittest
from src.indicator_calculator import IndicatorCalculator
import pandas as pd

class TestIndicatorCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = IndicatorCalculator()

    def test_calculate_renko(self):
        data = pd.DataFrame({'close': [100, 105, 102, 108]})
        result = self.calculator.calculate_renko(data, 5)
        self.assertIsInstance(result, pd.DataFrame)

    def test_calculate_line_break(self):
        data = pd.DataFrame({'close': [100, 105, 102, 108]})
        result = self.calculator.calculate_line_break(data, 3)
        self.assertIsInstance(result, pd.DataFrame)

    def test_calculate_pnf(self):
        data = pd.DataFrame({'close': [100, 105, 102, 108]})
        result = self.calculator.calculate_pnf(data)
        self.assertIsInstance(result, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()
