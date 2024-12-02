sequenceDiagram
    participant User
    participant FinancialDataProcessor
    participant IndicatorCalculator
    participant InstrumentAnalyzer
    participant ReportGenerator
    participant TestValidator

    User->>FinancialDataProcessor: load_data(file_path)
    FinancialDataProcessor->>FinancialDataProcessor: preprocess_data(data)
    FinancialDataProcessor->>IndicatorCalculator: calculate_renko(data, brick_size)
    IndicatorCalculator->>InstrumentAnalyzer: analyze_instrument(data, instrument_type)
    InstrumentAnalyzer->>ReportGenerator: generate_report(analysis_result)
    ReportGenerator->>TestValidator: validate_renko(data, expected)
    TestValidator->>User: return validation result