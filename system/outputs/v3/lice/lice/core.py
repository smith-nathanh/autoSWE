import sys
from .license_template import LicenseTemplate
from .license_header import LicenseHeader
from .language_detector import LanguageDetector
from .git_config import GitConfig

class Lice:
    def __init__(self):
        self.git_config = GitConfig()
        self.language_detector = LanguageDetector()

    def generate_license(self, license_type, year=None, org=None, language=None, file=None):
        user_info = self.git_config.get_user_info()
        org = org or user_info.get('organization')
        year = year or user_info.get('year')

        template = LicenseTemplate().load_template(f'templates/template-{license_type}.txt')
        license_text = template.apply_variables({'year': year, 'organization': org})

        if language:
            header = LicenseHeader().format_header(language)
            license_text = f'{header}\n{license_text}'

        if file:
            with open(file, 'w') as f:
                f.write(license_text)
        else:
            print(license_text)

    def custom_template(self, template_path):
        return LicenseTemplate().load_template(template_path)

    def list_template_vars(self, license_type):
        template = LicenseTemplate().load_template(f'templates/template-{license_type}.txt')
        return template.list_variables()

if __name__ == "__main__":
    lice = Lice()
    # Example command-line parsing (simplified)
    command = sys.argv[1]
    if command == 'generate':
        lice.generate_license(sys.argv[2], year=sys.argv[3], org=sys.argv[4], language=sys.argv[5], file=sys.argv[6])