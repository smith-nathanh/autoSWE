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
        +train(model, data)
        +evaluate(model, data)
    }
    class Logger {
        +log_training_loss(batch, loss)
        +log_accuracy(epoch, accuracy)
    }
    class CheckpointManager {
        +save_checkpoint(model, epoch)
        +load_checkpoint(path)
    }
    TextCNN --> DataLoader : uses
    Trainer --> TextCNN : trains
    Trainer --> Logger : logs
    Trainer --> CheckpointManager : manages
    DataLoader --> Trainer : provides data