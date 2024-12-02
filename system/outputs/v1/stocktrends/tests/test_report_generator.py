import unittest
from src.report_generator import ReportGenerator

class TestReportGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = ReportGenerator()

    def test_generate_report(self):
        result = self.generator.generate_report(None)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
