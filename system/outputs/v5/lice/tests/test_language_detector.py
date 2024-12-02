import unittest
from src.language_detector import LanguageDetector

class TestLanguageDetector(unittest.TestCase):
    def setUp(self):
        self.detector = LanguageDetector()

    def test_detectLanguage(self):
        self.assertEqual(self.detector.detectLanguage('main.py'), 'Python')
        self.assertEqual(self.detector.detectLanguage('index.html'), 'HTML')
        self.assertEqual(self.detector.detectLanguage('unknown.xyz'), 'Unknown')

if __name__ == '__main__':
    unittest.main()