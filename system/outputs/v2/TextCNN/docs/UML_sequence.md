sequenceDiagram
    participant User
    participant Main
    participant DataLoader
    participant Tokenizer
    participant TextCNN
    participant Trainer
    User->>Main: Run training script
    Main->>DataLoader: load_data()
    DataLoader->>Tokenizer: load_tokenizer()
    DataLoader->>Tokenizer: tokenize(text)
    DataLoader->>Main: return processed data
    Main->>TextCNN: Initialize model
    Main->>Trainer: Initialize trainer
    Trainer->>TextCNN: train(model, data)
    Trainer->>TextCNN: evaluate(model, data)
    Trainer->>Main: return evaluation metrics
    User->>Main: Run testing script
    Main->>Trainer: load_checkpoint()
    Trainer->>TextCNN: test(model, data)
    Trainer->>Main: return test accuracy