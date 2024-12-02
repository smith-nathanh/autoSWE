sequenceDiagram
    participant User
    participant Config
    participant DataLoader
    participant TextCNN
    participant Trainer
    participant Logger
    User->>Config: Set parameters
    User->>DataLoader: Load and preprocess data
    DataLoader-->>Trainer: Provide data
    User->>TextCNN: Initialize model
    User->>Trainer: Start training
    loop for each epoch
        Trainer->>TextCNN: Forward pass
        TextCNN-->>Trainer: Output
        Trainer->>Logger: Log training loss and accuracy
        alt Save checkpoint
            Trainer->>Trainer: Save model
        end
    end
    User->>Trainer: Evaluate model
    Trainer->>Logger: Log evaluation results
    User->>Trainer: Test model
    Trainer->>Logger: Log test accuracy