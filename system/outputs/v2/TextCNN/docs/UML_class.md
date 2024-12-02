classDiagram
    class TextCNN {
        +int embedding_dim
        +list kernel_sizes
        +int max_length
        +forward(input)
    }
    class DataLoader {
        +load_data()
        +preprocess_data()
        +split_data()
    }
    class Trainer {
        +float learning_rate
        +int batch_size
        +int num_epochs
        +train(model, data)
        +evaluate(model, data)
        +save_checkpoint()
        +log_metrics()
    }
    class Tokenizer {
        +load_tokenizer()
        +tokenize(text)
    }
    TextCNN --> Trainer : uses
    Trainer --> DataLoader : interacts
    Trainer --> Tokenizer : interacts
    DataLoader --> Tokenizer : uses