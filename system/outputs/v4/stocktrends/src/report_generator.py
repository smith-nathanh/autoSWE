class ReportGenerator:
    def generate_report(self, analysis_result):
        """
        Generate a report from the analysis result.
        """
        print("Analysis Report")
        for key, value in analysis_result.items():
            print(f"{key}: {value}")