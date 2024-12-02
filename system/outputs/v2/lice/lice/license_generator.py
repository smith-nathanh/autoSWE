from template_manager import TemplateManager
from file_manager import FileManager
from config_manager import ConfigManager


class LicenseGenerator:
    def __init__(self):
        self.template_manager = TemplateManager()
        self.file_manager = FileManager()
        self.config_manager = ConfigManager()

    def generateLicense(self, license_type, options):
        year = self.config_manager.getDefaultYear()
        org = self.config_manager.getDefaultOrg()
        language = None
        file_name = None

        for i, option in enumerate(options):
            if option in ('-y', '--year'):
                year = options[i + 1]
            elif option in ('-o', '--org'):
                org = options[i + 1]
            elif option in ('-l', '--language'):
                language = options[i + 1]
            elif option in ('-f', '--file'):
                file_name = options[i + 1]

        template = self.template_manager.loadTemplate(license_type)
        content = template.format(year=year, org=org)

        if language:
            content = self.file_manager.formatHeader(content, language)

        if file_name:
            self.file_manager.createFile(file_name, content)
        else:
            print(content)

    def listTemplateVariables(self, license_type):
        template = self.template_manager.loadTemplate(license_type)
        variables = self.template_manager.getTemplateVariables(template)
        print("Template variables:", variables)