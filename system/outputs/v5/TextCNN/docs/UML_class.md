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
    }
    class Trainer {
        +float learning_rate
        +int batch_size
        +int num_epochs
        +train()
        +evaluate()
    }
    class Logger {
        +log_training_loss()
        +log_accuracy()
    }
    class CheckpointManager {
        +save_checkpoint()
        +load_checkpoint()
    }
    TextCNN --> DataLoader : uses
    Trainer --> TextCNN : trains
    Trainer --> Logger : logs
    Trainer --> CheckpointManager : manages
    DataLoader --> Trainer : provides data