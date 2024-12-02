sequenceDiagram
    participant User
    participant CLI as CommandLineInterface
    participant Lice
    participant LicenseTemplate
    participant HeaderTemplate
    participant Environment
    
    User->>CLI: Run command with arguments
    CLI->>Lice: parseArguments(args)
    Lice->>Environment: getDefaultOrg()
    Environment-->>Lice: org
    Lice->>LicenseTemplate: loadTemplate(type)
    LicenseTemplate-->>Lice: template
    Lice->>HeaderTemplate: loadHeaderTemplate(language)
    HeaderTemplate-->>Lice: headerTemplate
    Lice->>LicenseTemplate: applyVariables(vars)
    LicenseTemplate-->>Lice: filledTemplate
    Lice->>HeaderTemplate: applyHeaderVariables(vars)
    HeaderTemplate-->>Lice: filledHeaderTemplate
    Lice->>CLI: executeCommand()
    CLI-->>User: License file created