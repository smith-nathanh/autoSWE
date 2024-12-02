import pytest
from .financial_data_processor import FinancialDataProcessor
from .indicator_calculator import IndicatorCalculator
from .instrument_analyzer import InstrumentAnalyzer
from .report_generator import ReportGenerator

class TestSuite:
    def run_unit_tests(self):
        """Run unit tests."""
        pytest.main(['tests/test_financial_data_processor.py',
                     'tests/test_indicator_calculator.py',
                     'tests/test_instrument_analyzer.py',
                     'tests/test_report_generator.py'])

    def run_acceptance_tests(self):
        """Run acceptance tests."""
        pytest.main(['tests/test_acceptance.py'])