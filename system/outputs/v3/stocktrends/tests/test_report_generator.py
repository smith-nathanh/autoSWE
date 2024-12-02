import pytest
from src.report_generator import ReportGenerator

@pytest.fixture
def report_generator():
    return ReportGenerator()


def test_generate_report(report_generator):
    report = report_generator.generate_report({})
    assert isinstance(report, str)