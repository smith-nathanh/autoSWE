sequenceDiagram
    participant User
    participant CLI
    participant Lice
    participant LicenseTemplate
    participant LicenseHeader
    participant LanguageDetector
    participant GitConfig
    User->>CLI: Run command with options
    CLI->>Lice: Parse command
    Lice->>GitConfig: Retrieve user info
    GitConfig-->>Lice: Return user info
    Lice->>LanguageDetector: Detect language
    LanguageDetector-->>Lice: Return language
    Lice->>LicenseTemplate: Load template
    LicenseTemplate-->>Lice: Return template
    Lice->>LicenseHeader: Format header
    LicenseHeader-->>Lice: Return formatted header
    Lice->>CLI: Output license file
    CLI-->>User: License file created