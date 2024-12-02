import pytest
from src.report_generator import ReportGenerator

def test_generate_report():
    generator = ReportGenerator()
    analysis_result = {'average_close': 104, 'max_close': 108, 'min_close': 100}
    report = generator.generate_report(analysis_result)
    assert "average_close: 104" in report
    assert "max_close: 108" in report
    assert "min_close: 100" in report