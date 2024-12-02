classDiagram
    class FinancialDataProcessor {
        +load_data(file_path: str) void
        +preprocess_data(data: DataFrame) DataFrame
    }

    class IndicatorCalculator {
        +calculate_renko(data: DataFrame, brick_size: float) DataFrame
        +calculate_line_break(data: DataFrame, line_count: int) DataFrame
        +calculate_pnf(data: DataFrame) DataFrame
    }

    class InstrumentAnalyzer {
        +analyze_instrument(data: DataFrame, instrument_type: str) AnalysisResult
    }

    class ReportGenerator {
        +generate_report(analysis_result: AnalysisResult) void
    }

    class TestValidator {
        +validate_renko(data: DataFrame, expected: DataFrame) bool
        +validate_line_break(data: DataFrame, expected: DataFrame) bool
    }

    FinancialDataProcessor --> IndicatorCalculator
    IndicatorCalculator --> InstrumentAnalyzer
    InstrumentAnalyzer --> ReportGenerator
    ReportGenerator --> TestValidator
    TestValidator --> FinancialDataProcessor