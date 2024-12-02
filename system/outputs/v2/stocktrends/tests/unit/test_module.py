import unittest
import pandas as pd
from src.financial_data_processor import FinancialDataProcessor
from src.indicator_calculator import IndicatorCalculator
from src.instrument_analyzer import InstrumentAnalyzer

class TestFinancialDataProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = FinancialDataProcessor()
        self.sample_data = pd.read_csv('data/unit_samples/HOOLI.csv')

    def test_load_data(self):
        data = self.processor.load_data('data/unit_samples/HOOLI.csv')
        self.assertIsInstance(data, pd.DataFrame)

    def test_preprocess_data(self):
        preprocessed_data = self.processor.preprocess_data(self.sample_data)
        self.assertTrue(all(preprocessed_data.columns == ['date', 'open', 'high', 'low', 'close']))

class TestIndicatorCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = IndicatorCalculator()
        self.sample_data = pd.read_csv('data/unit_samples/HOOLI.csv')

    def test_calculate_renko(self):
        renko_data = self.calculator.calculate_renko(self.sample_data, brick_size=2, chart_type='PERIOD_CLOSE')
        self.assertIsInstance(renko_data, pd.DataFrame)

    def test_calculate_line_break(self):
        line_break_data = self.calculator.calculate_line_break(self.sample_data, line_number=3)
        self.assertIsInstance(line_break_data, pd.DataFrame)

    def test_calculate_pnf(self):
        pnf_data = self.calculator.calculate_pnf(self.sample_data)
        self.assertIsInstance(pnf_data, pd.DataFrame)

class TestInstrumentAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = InstrumentAnalyzer()
        self.sample_data = pd.read_csv('data/unit_samples/HOOLI.csv')

    def test_analyze_instrument(self):
        analysis_results = self.analyzer.analyze_instrument(self.sample_data, instrument_type='stock')
        self.assertIn('analysis', analysis_results)

if __name__ == '__main__':
    unittest.main()
