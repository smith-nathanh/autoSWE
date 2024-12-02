class LicenseTemplate:
    def load_template(self, template_path):
        with open(template_path, 'r') as file:
            content = file.read()
        return LicenseTemplateContent(content)

class LicenseTemplateContent:
    def __init__(self, content):
        self.content = content

    def apply_variables(self, vars):
        result = self.content
        for key, value in vars.items():
            result = result.replace(f'{{{{ {key} }}}}', value)
        return result

    def list_variables(self):
        # This is a placeholder for actual variable extraction logic
        return ['year', 'organization']