classDiagram
    class Lice {
        +generate_license(license_type, year, org, language, file)
        +custom_template(template_path)
        +list_template_vars(license_type)
    }
    class LicenseTemplate {
        +load_template(template_path)
        +apply_variables(vars)
    }
    class LicenseHeader {
        +format_header(language)
    }
    class LanguageDetector {
        +detect_language(file_extension)
    }
    class GitConfig {
        +get_user_info()
    }
    Lice --> LicenseTemplate : uses
    Lice --> LicenseHeader : uses
    Lice --> LanguageDetector : uses
    Lice --> GitConfig : uses