from src.report_generator import ReportGenerator


def test_generate_report(capsys):
    report_generator = ReportGenerator()
    analysis_result = {'average_close': 105.0}
    report_generator.generate_report(analysis_result)
    captured = capsys.readouterr()
    assert "Analysis Report" in captured.out
    assert "average_close: 105.0" in captured.out