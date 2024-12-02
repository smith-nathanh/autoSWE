import sys
from license_generator import LicenseGenerator


def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python core.py <license_type> [options]")
        return

    license_type = args[0]
    options = args[1:]

    generator = LicenseGenerator()
    generator.generateLicense(license_type, options)


if __name__ == "__main__":
    main()