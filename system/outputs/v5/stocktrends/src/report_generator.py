class ReportGenerator:
    def generate_report(self, analysis_result):
        """Generate a report from the analysis result."""
        report = "Analysis Report\n"
        report += "================\n"
        for key, value in analysis_result.items():
            report += f"{key}: {value}\n"
        return report