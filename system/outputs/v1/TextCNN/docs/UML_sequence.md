sequenceDiagram
    participant User
    participant Main
    participant DataLoader
    participant TextCNN
    participant Trainer
    participant Logger
    participant CheckpointManager
    User->>Main: Run training script
    Main->>DataLoader: load_data()
    DataLoader-->>Main: return data
    Main->>TextCNN: initialize model
    Main->>Trainer: initialize with model
    Main->>Trainer: train()
    loop for each epoch
        Trainer->>TextCNN: forward pass
        Trainer->>Logger: log_training_loss()
        Trainer->>CheckpointManager: save_checkpoint()
    end
    User->>Main: Run testing script
    Main->>DataLoader: load_data()
    DataLoader-->>Main: return test data
    Main->>Trainer: evaluate()
    Trainer->>Logger: log_accuracy()