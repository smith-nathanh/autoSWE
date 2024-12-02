import os

class TemplateManager:
    def __init__(self):
        self.template_dir = './templates/'

    def loadTemplate(self, license_type):
        template_path = os.path.join(self.template_dir, f'template-{license_type}.txt')
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"Template for {license_type} not found.")

        with open(template_path, 'r') as file:
            return file.read()

    def getTemplateVariables(self, template):
        # Assuming template variables are in the format {var}
        import re
        return re.findall(r'{(.*?)}', template)