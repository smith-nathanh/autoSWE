import unittest
from src.template_manager import TemplateManager

class TestTemplateManager(unittest.TestCase):
    def setUp(self):
        self.manager = TemplateManager()

    def test_load_template(self):
        template = self.manager.loadTemplate('mit')
        self.assertIn('{{year}}', template)

    def test_list_template_variables(self):
        variables = self.manager.listTemplateVariables('mit')
        self.assertIn('year', variables)
        self.assertIn('organization', variables)

if __name__ == '__main__':
    unittest.main()