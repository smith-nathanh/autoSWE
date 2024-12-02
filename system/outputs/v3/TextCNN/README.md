# TextCNN Sentiment Classification

This repository contains the implementation of a TextCNN model for sentiment classification on movie reviews using the PyTorch library. The model is trained and evaluated on the IMDb dataset.

## Project Structure

- `main.py`: The entry point for training and testing the model.
- `requirements.txt`: Lists the dependencies required for the project.
- `models/`: Contains the implementation of the TextCNN model.
- `data/`: Contains the data loading and preprocessing scripts.
- `train/`: Contains the training and logging scripts.
- `config/`: Contains the configuration settings for the project.
- `examples/`: Contains example scripts for training and testing the model.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd project-root
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

## Dependencies
- transformers
- datasets
- evaluate
- torch

## License
This project is licensed under the MIT License.