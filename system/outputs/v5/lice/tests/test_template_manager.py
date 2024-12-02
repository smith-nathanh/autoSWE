import unittest
from src.template_manager import TemplateManager

class TestTemplateManager(unittest.TestCase):
    def setUp(self):
        self.manager = TemplateManager()

    def test_loadTemplate(self):
        template = self.manager.loadTemplate('mit')
        self.assertIn('MIT License', template)

    def test_listTemplateVariables(self):
        variables = self.manager.listTemplateVariables('mit')
        self.assertIn('year', variables)
        self.assertIn('organization', variables)

if __name__ == '__main__':
    unittest.main()