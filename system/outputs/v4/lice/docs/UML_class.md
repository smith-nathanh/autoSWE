classDiagram
    class LicenseGenerator {
        +generateLicense(type: String, year: int, org: String): String
        +generateHeader(type: String, language: String): String
        +saveToFile(content: String, filename: String): void
    }
    class TemplateManager {
        +loadTemplate(type: String): String
        +listTemplateVariables(type: String): List<String>
    }
    class LanguageDetector {
        +detectLanguage(filename: String): String
    }
    class CLI {
        +parseArguments(args: List<String>): Map<String, String>
        +executeCommand(args: Map<String, String>): void
    }
    LicenseGenerator --> TemplateManager : uses
    LicenseGenerator --> LanguageDetector : uses
    CLI --> LicenseGenerator : interacts