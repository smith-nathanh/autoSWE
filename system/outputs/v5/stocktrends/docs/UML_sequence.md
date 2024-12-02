sequenceDiagram
    participant User
    participant FinancialDataProcessor
    participant IndicatorCalculator
    participant InstrumentAnalyzer
    participant ReportGenerator
    participant TestSuite

    User->>FinancialDataProcessor: load_data(file_path)
    FinancialDataProcessor->>User: return data
    User->>FinancialDataProcessor: preprocess_data(data)
    FinancialDataProcessor->>User: return preprocessed data

    User->>IndicatorCalculator: calculate_renko(preprocessed data, brick_size)
    IndicatorCalculator->>User: return renko data

    User->>IndicatorCalculator: calculate_line_break(preprocessed data, line_count)
    IndicatorCalculator->>User: return line break data

    User->>IndicatorCalculator: calculate_pnf(preprocessed data)
    IndicatorCalculator->>User: return pnf data

    User->>InstrumentAnalyzer: analyze_instrument(preprocessed data, instrument_type)
    InstrumentAnalyzer->>User: return analysis result

    User->>ReportGenerator: generate_report(analysis result)
    ReportGenerator->>User: return report

    User->>TestSuite: run_unit_tests()
    TestSuite->>User: return test results

    User->>TestSuite: run_acceptance_tests()
    TestSuite->>User: return acceptance test results