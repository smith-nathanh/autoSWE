import unittest
from src.instrument_analyzer import InstrumentAnalyzer
import pandas as pd

class TestInstrumentAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = InstrumentAnalyzer()

    def test_analyze_instrument(self):
        data = pd.DataFrame({'close': [100, 105, 102, 108]})
        result = self.analyzer.analyze_instrument(data, 'stock')
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
