classDiagram
    class LicenseGenerator {
        +generateLicense(type: String, year: int, org: String, language: String, file: String)
        +listTemplateVariables(licenseType: String)
    }
    class TemplateManager {
        +loadTemplate(templatePath: String)
        +getTemplateVariables(template: String)
    }
    class FileManager {
        +createFile(fileName: String, content: String)
        +detectLanguage(fileExtension: String)
    }
    class ConfigManager {
        +getDefaultOrg()
        +getDefaultYear()
    }
    LicenseGenerator --> TemplateManager : uses
    LicenseGenerator --> FileManager : uses
    LicenseGenerator --> ConfigManager : uses
    TemplateManager --> FileManager : uses