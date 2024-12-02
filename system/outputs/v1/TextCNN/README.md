# TextCNN Sentiment Classification

This repository contains the implementation of a TextCNN model for sentiment classification on the IMDb dataset using PyTorch.

## Project Structure

- `data/`: Contains data loading and preprocessing scripts.
- `models/`: Contains the TextCNN model implementation.
- `trainers/`: Contains the training and evaluation logic.
- `utils/`: Contains utility scripts like logging and checkpoint management.
- `scripts/`: Contains scripts to run training and testing.
- `main.py`: Entry point for training and testing the model.
- `requirements.txt`: Lists the dependencies required for the project.

## Usage

To train the model, run:
```bash
python main.py --train --output_dir './outputs'
```

To test the model, run:
```bash
python main.py --test --output_dir './outputs' --checkpoint_path './outputs/model_epoch_X.pt'
```

Replace `X` with the epoch number of the checkpoint you want to test.

## Requirements

Install the required packages using:
```bash
pip install -r requirements.txt
```

## Description

The TextCNN model is used for classifying movie reviews from the IMDb dataset into positive or negative sentiments. The model is built using PyTorch and leverages the `transformers` and `datasets` libraries for data handling and tokenization.