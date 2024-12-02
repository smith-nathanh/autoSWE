# TextCNN Sentiment Classification

This project implements a TextCNN model for sentiment classification on movie reviews using the PyTorch library. The model is trained and evaluated on the IMDb dataset.

## Project Structure

- `src/`: Contains the source code for the project.
  - `main.py`: Main script to run training and testing.
  - `model/`: Contains the TextCNN model implementation.
  - `data/`: Contains data loading and preprocessing scripts.
  - `training/`: Contains training logic and checkpoint management.
  - `utils/`: Contains utility functions like logging.
- `examples/`: Contains example scripts for usage.
- `tests/`: Contains unit tests for the project.

## Requirements

- Python 3.8+
- PyTorch
- Transformers
- Datasets
- Evaluate

## Usage

To train the model, run:

```bash
python src/main.py \
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

To test a trained model, run:

```bash
python src/main.py \
  --test \
  --gpu \
  --output_dir './outputs'
```

## Testing

Run the tests using:

```bash
pytest tests/
```