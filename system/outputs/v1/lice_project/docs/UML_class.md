classDiagram
    class Lice {
        +generateLicense(type: String, year: int, org: String, language: String, file: String)
        +customTemplate(path: String)
        +listTemplateVariables(licenseType: String)
    }
    class LicenseTemplate {
        +loadTemplate(type: String)
        +applyVariables(vars: Map<String, String>)
    }
    class HeaderTemplate {
        +loadHeaderTemplate(language: String)
        +applyHeaderVariables(vars: Map<String, String>)
    }
    class CommandLineInterface {
        +parseArguments(args: List<String>)
        +executeCommand()
    }
    class Environment {
        +getDefaultOrg() : String
        +getDefaultYear() : int
    }
    Lice --> LicenseTemplate
    Lice --> HeaderTemplate
    Lice --> CommandLineInterface
    Lice --> Environment
    CommandLineInterface --> Lice
    LicenseTemplate --> Lice
    HeaderTemplate --> Lice
    Environment --> Lice