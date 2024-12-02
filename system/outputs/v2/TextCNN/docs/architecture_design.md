project-root/
│   README.md
│   main.py
│   requirements.txt
│
├───models/
│       text_cnn.py
│
├───data/
│       data_loader.py
│
├───tokenizer/
│       tokenizer.py
│
├───trainer/
│       trainer.py
│
└───examples/
        example_usage.sh
        train_example.py
        test_example.py

README.md: Contains an overview of the project, setup instructions, and usage examples.
main.py: The entry point for training and testing the TextCNN model.
requirements.txt: Lists all the dependencies required to run the project.

models/text_cnn.py: Defines the TextCNN model architecture.
data/data_loader.py: Handles loading and preprocessing of the IMDb dataset.
tokenizer/tokenizer.py: Manages the loading and usage of the BERT tokenizer.
trainer/trainer.py: Contains the training loop, evaluation, and checkpoint saving logic.

examples/example_usage.sh: Shell script demonstrating how to run training and testing.
examples/train_example.py: Example script for training the model.
examples/test_example.py: Example script for testing the model.