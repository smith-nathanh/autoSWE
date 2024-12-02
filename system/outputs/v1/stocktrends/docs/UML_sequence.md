sequenceDiagram
    participant User
    participant FinancialDataProcessor
    participant IndicatorCalculator
    participant InstrumentAnalyzer
    participant ReportGenerator
    participant TestValidator
    participant DataSet

    User->>FinancialDataProcessor: load_data(file_path)
    FinancialDataProcessor->>FinancialDataProcessor: preprocess_data(data)
    FinancialDataProcessor->>IndicatorCalculator: calculate_renko(data, brick_size)
    IndicatorCalculator->>InstrumentAnalyzer: analyze_instrument(data, instrument_type)
    InstrumentAnalyzer->>ReportGenerator: generate_report(analysis_result)
    User->>TestValidator: validate_renko(data, expected)
    TestValidator->>DataSet: load_acceptance_samples()
    TestValidator->>IndicatorCalculator: validate_renko(data, expected)
    User->>TestValidator: validate_line_break(data, expected)
    TestValidator->>DataSet: load_unit_samples()
    TestValidator->>IndicatorCalculator: validate_line_break(data, expected)