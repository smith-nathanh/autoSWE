import unittest
from src.financial_data_processor import FinancialDataProcessor
from src.indicator_calculator import IndicatorCalculator
from src.instrument_analyzer import InstrumentAnalyzer
from src.report_generator import ReportGenerator
import pandas as pd

class TestFinancialDataProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = FinancialDataProcessor()

    def test_load_data(self):
        data = self.processor.load_data('project_root/unit_samples/HOOLI.csv')
        self.assertIsInstance(data, pd.DataFrame)

    def test_preprocess_data(self):
        data = pd.DataFrame({'Date': ["2021-01-01"], 'Open': [100]})
        processed_data = self.processor.preprocess_data(data)
        self.assertIn('date', processed_data.columns)

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

class TestInstrumentAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = InstrumentAnalyzer()

    def test_analyze_instrument(self):
        data = pd.DataFrame({'close': [100, 105, 102, 108]})
        result = self.analyzer.analyze_instrument(data, 'stock')
        self.assertIsNone(result)

class TestReportGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = ReportGenerator()

    def test_generate_report(self):
        result = self.generator.generate_report(None)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
