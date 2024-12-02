import argparse
from license_generator import LicenseGenerator
from template_manager import TemplateManager

class CLI:
    def parseArguments(self, args):
        parser = argparse.ArgumentParser(description='Generate license files for your project.')
        parser.add_argument('license', type=str, help='The type of license to generate.')
        parser.add_argument('-o', '--org', type=str, help='The organization under which the license is registered.')
        parser.add_argument('-p', '--proj', type=str, help='The project name for which the license is generated.')
        parser.add_argument('-t', '--template', type=str, help='The path to a custom license template file.')
        parser.add_argument('-y', '--year', type=int, help='The copyright year to be listed in the license.')
        parser.add_argument('-l', '--language', type=str, help='The language for which the license header should be formatted.')
        parser.add_argument('-f', '--file', type=str, help='The output file name where the license should be saved.')
        parser.add_argument('--vars', action='store_true', help='List all template variables for the specified license.')
        return vars(parser.parse_args(args))

    def executeCommand(self, args):
        generator = LicenseGenerator()
        if args['vars']:
            template_manager = TemplateManager()
            variables = template_manager.listTemplateVariables(args['license'])
            print("Template variables:", variables)
        else:
            license_text = generator.generateLicense(args['license'], args.get('year', 2023), args.get('org', 'Unknown'))
            if args.get('language'):
                header = generator.generateHeader(args['license'], args['language'])
                license_text = header + "\n" + license_text
            if args.get('file'):
                generator.saveToFile(license_text, args['file'])
            else:
                print(license_text)