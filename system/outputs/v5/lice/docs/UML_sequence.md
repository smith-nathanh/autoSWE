sequenceDiagram
    participant User
    participant CLI
    participant LicenseGenerator
    participant TemplateManager
    participant LanguageDetector
    User->>CLI: Run command with arguments
    CLI->>LicenseGenerator: parseArguments(args)
    LicenseGenerator->>TemplateManager: loadTemplate(type)
    TemplateManager-->>LicenseGenerator: template
    LicenseGenerator->>LanguageDetector: detectLanguage(filename)
    LanguageDetector-->>LicenseGenerator: language
    LicenseGenerator->>LicenseGenerator: generateLicense(type, year, org)
    LicenseGenerator->>LicenseGenerator: generateHeader(type, language)
    LicenseGenerator->>LicenseGenerator: saveToFile(content, filename)
    LicenseGenerator-->>CLI: Command execution complete
    CLI-->>User: Output result