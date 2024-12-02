classDiagram
    class FinancialDataProcessor {
        +load_data(file_path: str)
        +preprocess_data(data: DataFrame)
    }

    class IndicatorCalculator {
        +calculate_renko(data: DataFrame, brick_size: float, chart_type: str)
        +calculate_line_break(data: DataFrame, line_number: int)
        +calculate_pnf(data: DataFrame)
    }

    class InstrumentAnalyzer {
        +analyze_instrument(data: DataFrame, instrument_type: str)
    }

    class ReportGenerator {
        +generate_report(analysis_results: dict)
    }

    class TestValidator {
        +run_unit_tests()
        +run_acceptance_tests()
    }

    FinancialDataProcessor --> IndicatorCalculator
    IndicatorCalculator --> InstrumentAnalyzer
    InstrumentAnalyzer --> ReportGenerator
    TestValidator --> IndicatorCalculator
    TestValidator --> FinancialDataProcessor