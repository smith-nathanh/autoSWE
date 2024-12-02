import pandas as pd
from src.financial_data_processor import FinancialDataProcessor
from src.indicator_calculator import IndicatorCalculator
from src.instrument_analyzer import InstrumentAnalyzer
from src.report_generator import ReportGenerator

# Load and preprocess data
processor = FinancialDataProcessor()
data = processor.load_data('acceptance_samples/HOOLI.csv')
preprocessed_data = processor.preprocess_data(data)

# Calculate indicators
calculator = IndicatorCalculator()
renko_chart = calculator.calculate_renko(preprocessed_data, brick_size=2, chart_type='PERIOD_CLOSE')
line_break_chart = calculator.calculate_line_break(preprocessed_data, line_number=3)
pnf_chart = calculator.calculate_pnf(preprocessed_data)

# Analyze instrument
analyzer = InstrumentAnalyzer()
analysis_results = analyzer.analyze_instrument(preprocessed_data, instrument_type='stock')

# Generate report
report_generator = ReportGenerator()
report = report_generator.generate_report(analysis_results)

print("Renko Chart:", renko_chart)
print("Line Break Chart:", line_break_chart)
print("PnF Chart:", pnf_chart)
print("Analysis Report:", report)