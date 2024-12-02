import pandas as pd
from src.financial_data_processor import FinancialDataProcessor
from src.indicator_calculator import IndicatorCalculator
from src.instrument_analyzer import InstrumentAnalyzer
from src.report_generator import ReportGenerator

# Load and preprocess data
processor = FinancialDataProcessor()
data = processor.load_data('data/acceptance_samples/HOOLI.csv')
preprocessed_data = processor.preprocess_data(data)

# Calculate indicators
calculator = IndicatorCalculator()
renko_data = calculator.calculate_renko(preprocessed_data, brick_size=2)
line_break_data = calculator.calculate_line_break(preprocessed_data, line_count=3)

# Analyze instrument
analyzer = InstrumentAnalyzer()
analysis_result = analyzer.analyze_instrument(preprocessed_data, instrument_type='stock')

# Generate report
report_generator = ReportGenerator()
report_generator.generate_report(analysis_result)