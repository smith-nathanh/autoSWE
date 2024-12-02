sequenceDiagram
    participant User
    participant CLI
    participant LicenseGenerator
    participant TemplateManager
    participant FileManager
    participant ConfigManager
    User->>CLI: Run command to generate license
    CLI->>LicenseGenerator: Parse command and call generateLicense
    LicenseGenerator->>ConfigManager: Get default org and year
    ConfigManager-->>LicenseGenerator: Return default org and year
    LicenseGenerator->>TemplateManager: Load license template
    TemplateManager-->>LicenseGenerator: Return template
    LicenseGenerator->>FileManager: Detect language from file extension
    FileManager-->>LicenseGenerator: Return language
    LicenseGenerator->>FileManager: Create license file with content
    FileManager-->>User: License file created