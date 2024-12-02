import unittest
from src.test_validator import TestValidator
import pandas as pd

class TestTestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = TestValidator()

    def test_validate_renko(self):
        data = pd.DataFrame({'close': [100, 105, 102, 108]})
        expected = pd.DataFrame({'close': [100, 105, 102, 108]})
        result = self.validator.validate_renko(data, expected)
        self.assertTrue(result)

    def test_validate_line_break(self):
        data = pd.DataFrame({'close': [100, 105, 102, 108]})
        expected = pd.DataFrame({'close': [100, 105, 102, 108]})
        result = self.validator.validate_line_break(data, expected)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
