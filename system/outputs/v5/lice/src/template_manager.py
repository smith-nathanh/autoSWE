import os

class TemplateManager:
    TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), '../templates')

    def loadTemplate(self, type):
        template_path = os.path.join(self.TEMPLATE_DIR, f'template-{type}.txt')
        with open(template_path, 'r') as file:
            return file.read()

    def listTemplateVariables(self, type):
        template = self.loadTemplate(type)
        return [word.strip('{}') for word in template.split() if word.startswith('{{') and word.endswith('}}')]