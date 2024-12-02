sequenceDiagram
    participant User
    participant FinancialDataProcessor
    participant IndicatorCalculator
    participant InstrumentAnalyzer
    participant ReportGenerator
    participant TestValidator

    User->>FinancialDataProcessor: load_data(file_path)
    FinancialDataProcessor->>User: return preprocessed data

    User->>IndicatorCalculator: calculate_renko(data, brick_size, chart_type)
    IndicatorCalculator->>User: return renko chart

    User->>IndicatorCalculator: calculate_line_break(data, line_number)
    IndicatorCalculator->>User: return line break chart

    User->>IndicatorCalculator: calculate_pnf(data)
    IndicatorCalculator->>User: return pnf chart

    User->>InstrumentAnalyzer: analyze_instrument(data, instrument_type)
    InstrumentAnalyzer->>User: return analysis results

    User->>ReportGenerator: generate_report(analysis_results)
    ReportGenerator->>User: return report

    User->>TestValidator: run_unit_tests()
    TestValidator->>User: return test results

    User->>TestValidator: run_acceptance_tests()
    TestValidator->>User: return acceptance test results