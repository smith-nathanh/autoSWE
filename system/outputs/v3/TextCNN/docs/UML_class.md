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
        +save_checkpoint()
    }
    class Logger {
        +log_training_loss()
        +log_accuracy()
    }
    class Config {
        +float learning_rate
        +int batch_size
        +int num_epochs
        +int embedding_dim
        +list kernel_sizes
        +int max_length
        +int save_every_n_epoch
        +bool train
        +bool test
        +string output_dir
        +bool gpu
        +int train_log_per_k_batch
        +int random_seed
    }
    TextCNN --> Trainer
    Trainer --> Logger
    Trainer --> DataLoader
    Config --> Trainer
    Config --> TextCNN
    Config --> DataLoader