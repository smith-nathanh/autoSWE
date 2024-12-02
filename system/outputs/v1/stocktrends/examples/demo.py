from src.financial_data_processor import FinancialDataProcessor
from src.indicator_calculator import IndicatorCalculator
from src.instrument_analyzer import InstrumentAnalyzer
from src.report_generator import ReportGenerator

# Example usage
data_processor = FinancialDataProcessor()
indicator_calculator = IndicatorCalculator()
instrument_analyzer = InstrumentAnalyzer()
report_generator = ReportGenerator()

# Load and preprocess data
data = data_processor.load_data('project_root/unit_samples/HOOLI.csv')
processed_data = data_processor.preprocess_data(data)

# Calculate indicators
renko_data = indicator_calculator.calculate_renko(processed_data, brick_size=2)
line_break_data = indicator_calculator.calculate_line_break(processed_data, line_count=3)

# Analyze instrument
analysis_result = instrument_analyzer.analyze_instrument(processed_data, 'stock')

# Generate report
report_generator.generate_report(analysis_result)
