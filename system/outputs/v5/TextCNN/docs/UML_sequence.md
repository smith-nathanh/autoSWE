sequenceDiagram
    participant User
    participant Main
    participant DataLoader
    participant TextCNN
    participant Trainer
    participant Logger
    participant CheckpointManager
    User->>Main: Run training script
    Main->>DataLoader: Load and preprocess data
    DataLoader-->>Main: Return processed data
    Main->>TextCNN: Initialize model
    Main->>Trainer: Initialize with model and data
    loop for each epoch
        Trainer->>TextCNN: Train model
        Trainer->>Logger: Log training loss and accuracy
        Trainer->>CheckpointManager: Save checkpoint if best accuracy
    end
    User->>Main: Run testing script
    Main->>CheckpointManager: Load best model checkpoint
    Main->>Trainer: Evaluate model on test data
    Trainer->>Logger: Log test accuracy