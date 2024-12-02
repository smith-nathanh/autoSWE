from template_manager import TemplateManager
from language_detector import LanguageDetector

class LicenseGenerator:
    def __init__(self):
        self.template_manager = TemplateManager()
        self.language_detector = LanguageDetector()

    def generateLicense(self, type, year, org):
        template = self.template_manager.loadTemplate(type)
        license_text = template.replace("{{year}}", str(year)).replace("{{organization}}", org)
        return license_text

    def generateHeader(self, type, language):
        header_template = self.template_manager.loadTemplate(f"{type}-header")
        header_text = header_template.replace("{{language}}", language)
        return header_text

    def saveToFile(self, content, filename):
        with open(filename, 'w') as file:
            file.write(content)