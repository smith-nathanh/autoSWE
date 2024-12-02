import unittest
from src.language_detector import LanguageDetector

class TestLanguageDetector(unittest.TestCase):
    def setUp(self):
        self.detector = LanguageDetector()

    def test_detect_language(self):
        language = self.detector.detectLanguage('example.py')
        self.assertEqual(language, 'Python')

        language = self.detector.detectLanguage('example.js')
        self.assertEqual(language, 'JavaScript')

        language = self.detector.detectLanguage('unknown.ext')
        self.assertEqual(language, 'Unknown')

if __name__ == '__main__':
    unittest.main()