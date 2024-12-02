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
        data = self.processor.load_data('unit_samples/HOOLI.csv')
        self.assertFalse(data.empty)

    def test_preprocess_data(self):
        sample_data = pd.DataFrame({
            'Date': ['2021/01/01'],
            'Open': [100],
            'High': [110],
            'Low': [90],
            'Close': [105]
        })
        preprocessed_data = self.processor.preprocess_data(sample_data)
        self.assertIn('date', preprocessed_data.columns)


class TestIndicatorCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = IndicatorCalculator()

    def test_calculate_renko(self):
        sample_data = pd.DataFrame({
            'date': ['2021/01/01'],
            'open': [100],
            'high': [110],
            'low': [90],
            'close': [105]
        })
        renko_chart = self.calculator.calculate_renko(sample_data, brick_size=2, chart_type='PERIOD_CLOSE')
        self.assertIsInstance(renko_chart, pd.DataFrame)

    def test_calculate_line_break(self):
        sample_data = pd.DataFrame({
            'date': ['2021/01/01'],
            'open': [100],
            'high': [110],
            'low': [90],
            'close': [105]
        })
        line_break_chart = self.calculator.calculate_line_break(sample_data, line_number=3)
        self.assertIsInstance(line_break_chart, pd.DataFrame)

    def test_calculate_pnf(self):
        sample_data = pd.DataFrame({
            'date': ['2021/01/01'],
            'open': [100],
            'high': [110],
            'low': [90],
            'close': [105]
        })
        pnf_chart = self.calculator.calculate_pnf(sample_data)
        self.assertIsInstance(pnf_chart, pd.DataFrame)


class TestInstrumentAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = InstrumentAnalyzer()

    def test_analyze_instrument(self):
        sample_data = pd.DataFrame({
            'date': ['2021/01/01'],
            'open': [100],
            'high': [110],
            'low': [90],
            'close': [105]
        })
        results = self.analyzer.analyze_instrument(sample_data, instrument_type='stock')
        self.assertIsInstance(results, dict)


class TestReportGenerator(unittest.TestCase):
    def setUp(self):
        self.report_generator = ReportGenerator()

    def test_generate_report(self):
        report = self.report_generator.generate_report({})
        self.assertIsInstance(report, str)


if __name__ == '__main__':
    unittest.main()
