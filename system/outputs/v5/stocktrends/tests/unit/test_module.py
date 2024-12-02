import unittest
import pandas as pd
from src.financial_data_processor import FinancialDataProcessor
from src.indicator_calculator import IndicatorCalculator
from src.instrument_analyzer import InstrumentAnalyzer
from src.report_generator import ReportGenerator

class TestFinancialDataProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = FinancialDataProcessor()

    def test_load_data(self):
        data = self.processor.load_data('data/unit_samples/HOOLI.csv')
        self.assertFalse(data.empty)

    def test_preprocess_data(self):
        data = pd.DataFrame({'Date': ['2021-01-01'], 'Open': [100]})
        preprocessed_data = self.processor.preprocess_data(data)
        self.assertIn('date', preprocessed_data.columns)
        self.assertIn('open', preprocessed_data.columns)

class TestIndicatorCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = IndicatorCalculator()

    def test_calculate_renko(self):
        data = pd.DataFrame({'close': [100, 102, 104, 106, 108]})
        renko_data = self.calculator.calculate_renko(data, brick_size=2)
        self.assertEqual(len(renko_data), 4)

    def test_calculate_line_break(self):
        data = pd.DataFrame({'close': [100, 102, 104, 106, 108]})
        line_break_data = self.calculator.calculate_line_break(data, line_count=3)
        self.assertEqual(len(line_break_data), 5)

    def test_calculate_pnf(self):
        data = pd.DataFrame({'close': [100, 102, 104, 106, 108]})
        pnf_data = self.calculator.calculate_pnf(data)
        self.assertEqual(len(pnf_data), 4)

class TestInstrumentAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = InstrumentAnalyzer()

    def test_analyze_instrument_stock(self):
        data = pd.DataFrame({'close': [100, 102, 104, 106, 108]})
        result = self.analyzer.analyze_instrument(data, 'stock')
        self.assertEqual(result['average_close'], 104)
        self.assertEqual(result['max_close'], 108)
        self.assertEqual(result['min_close'], 100)

    def test_analyze_instrument_commodity(self):
        data = pd.DataFrame({'close': [200, 202, 204, 206, 208]})
        result = self.analyzer.analyze_instrument(data, 'commodity')
        self.assertEqual(result['average_close'], 204)
        self.assertEqual(result['max_close'], 208)
        self.assertEqual(result['min_close'], 200)

    def test_analyze_instrument_invalid(self):
        data = pd.DataFrame({'close': [200, 202, 204, 206, 208]})
        with self.assertRaises(ValueError):
            self.analyzer.analyze_instrument(data, 'invalid')

class TestReportGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = ReportGenerator()

    def test_generate_report(self):
        analysis_result = {'average_close': 104, 'max_close': 108, 'min_close': 100}
        report = self.generator.generate_report(analysis_result)
        self.assertIn('average_close: 104', report)
        self.assertIn('max_close: 108', report)
        self.assertIn('min_close: 100', report)

if __name__ == '__main__':
    unittest.main()
