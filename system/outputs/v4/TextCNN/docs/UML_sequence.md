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
    Main->>TextCNN: Initialize model
    Main->>Trainer: Initialize trainer
    loop for each epoch
        Trainer->>TextCNN: train(data)
        TextCNN-->>Trainer: return loss, accuracy
        Trainer->>Logger: log_training_loss(batch, loss)
        Trainer->>Logger: log_accuracy(epoch, accuracy)
        Trainer->>CheckpointManager: save_checkpoint(model, epoch)
    end
    User->>Main: Run testing script
    Main->>DataLoader: load_data()
    DataLoader-->>Main: return test data
    Main->>TextCNN: load_checkpoint()
    Main->>Trainer: evaluate(model, test data)
    Trainer-->>User: return test accuracy