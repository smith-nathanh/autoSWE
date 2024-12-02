import unittest
import pandas as pd
from src.financial_data_processor import FinancialDataProcessor
from src.indicator_calculator import IndicatorCalculator
from src.instrument_analyzer import InstrumentAnalyzer
from src.report_generator import ReportGenerator
from src.test_validator import TestValidator

class TestFinancialDataProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = FinancialDataProcessor()
        self.sample_data = pd.DataFrame({
            'Date': ['2021/01/01', '2021/01/02'],
            'Open': [100, 102],
            'High': [110, 112],
            'Low': [99, 101],
            'Close': [105, 107]
        })

    def test_load_data(self):
        data = self.processor.load_data('data/unit_samples/HOOLI.csv')
        self.assertFalse(data.empty)

    def test_preprocess_data(self):
        processed_data = self.processor.preprocess_data(self.sample_data)
        self.assertTrue(all(col.islower() for col in processed_data.columns))

class TestIndicatorCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = IndicatorCalculator()
        self.sample_data = pd.DataFrame({
            'close': [100, 102, 104, 106, 108, 110]
        })

    def test_calculate_renko(self):
        renko_data = self.calculator.calculate_renko(self.sample_data, brick_size=2)
        self.assertFalse(renko_data.empty)

    def test_calculate_line_break(self):
        line_break_data = self.calculator.calculate_line_break(self.sample_data, line_count=3)
        self.assertFalse(line_break_data.empty)

    def test_calculate_pnf(self):
        pnf_data = self.calculator.calculate_pnf(self.sample_data)
        self.assertFalse(pnf_data.empty)

class TestInstrumentAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = InstrumentAnalyzer()
        self.sample_data = pd.DataFrame({
            'close': [100, 102, 104, 106, 108, 110]
        })

    def test_analyze_instrument_stock(self):
        result = self.analyzer.analyze_instrument(self.sample_data, 'stock')
        self.assertIn('average_close', result)

    def test_analyze_instrument_commodity(self):
        result = self.analyzer.analyze_instrument(self.sample_data, 'commodity')
        self.assertIn('average_close', result)

    def test_analyze_instrument_invalid(self):
        with self.assertRaises(ValueError):
            self.analyzer.analyze_instrument(self.sample_data, 'invalid')

class TestReportGenerator(unittest.TestCase):
    def test_generate_report(self):
        report_generator = ReportGenerator()
        analysis_result = {'average_close': 105.0}
        with self.assertLogs(level='INFO') as log:
            report_generator.generate_report(analysis_result)
            self.assertIn('Analysis Report', log.output[0])
            self.assertIn('average_close: 105.0', log.output[0])

class TestTestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = TestValidator()
        self.sample_data = pd.DataFrame({
            'close': [100, 102, 104, 106, 108, 110]
        })
        self.expected_data = pd.DataFrame({
            'close': [100, 102, 104, 106, 108, 110]
        })

    def test_validate_renko(self):
        self.assertTrue(self.validator.validate_renko(self.sample_data, self.expected_data))

    def test_validate_line_break(self):
        self.assertTrue(self.validator.validate_line_break(self.sample_data, self.expected_data))

if __name__ == '__main__':
    unittest.main()
