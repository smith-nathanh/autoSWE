# TextCNN Sentiment Classification

This project implements a TextCNN model for sentiment classification on movie reviews using the PyTorch library. The model is trained and evaluated on the IMDb dataset.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Training
To train the model, run the following command:
```bash
python main.py \
  --learning_rate 0.01 \
  --num_epochs 10 \
  --batch_size 16 \
  --embedding_dim 300\
  --kernel_sizes 3 4 5\
  --max_length 50\
  --save_every_n_epoch 2\
  --train \
  --gpu \
  --output_dir './outputs'\
  --train_log_per_k_batch 20\
  --random_seed 20
```

### Testing
To test a trained checkpoint, run the following command:
```bash
python main.py \
  --test \
  --gpu \
  --output_dir './outputs'
```

## Project Structure
- `main.py`: Entry point for training and testing the TextCNN model.
- `requirements.txt`: Lists all the dependencies required to run the project.
- `models/text_cnn.py`: Defines the TextCNN model architecture.
- `data/data_loader.py`: Handles loading and preprocessing of the IMDb dataset.
- `tokenizer/tokenizer.py`: Manages the loading and usage of the BERT tokenizer.
- `trainer/trainer.py`: Contains the training loop, evaluation, and checkpoint saving logic.
- `examples/example_usage.sh`: Shell script demonstrating how to run training and testing.
- `examples/train_example.py`: Example script for training the model.
- `examples/test_example.py`: Example script for testing the model.

## Dependencies
- transformers
- datasets
- evaluate
- torch

## License
This project is licensed under the MIT License.