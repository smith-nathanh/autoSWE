sequenceDiagram
    participant User
    participant FinancialDataProcessor
    participant IndicatorCalculator
    participant InstrumentAnalyzer
    participant ReportGenerator
    participant TestValidator

    User->>FinancialDataProcessor: load_data(file_path)
    FinancialDataProcessor->>FinancialDataProcessor: preprocess_data(data)
    FinancialDataProcessor->>IndicatorCalculator: calculate_renko(data, brick_size, chart_type)
    IndicatorCalculator->>InstrumentAnalyzer: analyze_instrument(data, instrument_type)
    InstrumentAnalyzer->>ReportGenerator: generate_report(analysis_results)
    User->>TestValidator: run_acceptance_tests()
    TestValidator->>IndicatorCalculator: validate_renko_calculation()
    TestValidator->>FinancialDataProcessor: validate_data_processing()