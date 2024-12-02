import argparse
import torch
from data.data_loader import DataLoader
from model.text_cnn import TextCNN
from training.trainer import Trainer
from training.checkpoint_manager import CheckpointManager
from utils.logger import Logger


def parse_args():
    parser = argparse.ArgumentParser(description='Train or test the TextCNN model.')
    parser.add_argument('--learning_rate', type=float, default=1e-3, help='Learning rate for training')
    parser.add_argument('--batch_size', type=int, default=32, help='Batch size for training')
    parser.add_argument('--num_epochs', type=int, default=10, help='Number of epochs for training')
    parser.add_argument('--embedding_dim', type=int, default=500, help='Dimension of embedding layer')
    parser.add_argument('--kernel_sizes', nargs='+', type=int, default=[3, 4, 5], help='Kernel sizes for convolutional layers')
    parser.add_argument('--max_length', type=int, default=50, help='Maximum length of input sequences')
    parser.add_argument('--save_every_n_epoch', type=int, default=1, help='Save model every n epochs')
    parser.add_argument('--train', action='store_true', help='Flag to train the model')
    parser.add_argument('--test', action='store_true', help='Flag to test the model')
    parser.add_argument('--output_dir', type=str, required=True, help='Directory to save outputs')
    parser.add_argument('--gpu', action='store_true', help='Flag to use GPU')
    parser.add_argument('--train_log_per_k_batch', type=int, default=10, help='Log training loss every k batches')
    parser.add_argument('--random_seed', type=int, default=42, help='Random seed for reproducibility')
    return parser.parse_args()


def main():
    args = parse_args()

    # Set device
    device = torch.device('cuda' if args.gpu and torch.cuda.is_available() else 'cpu')

    # Set random seed
    torch.manual_seed(args.random_seed)

    # Load and preprocess data
    data_loader = DataLoader()
    train_data, val_data, test_data = data_loader.load_data()

    # Initialize model
    model = TextCNN(embedding_dim=args.embedding_dim, kernel_sizes=args.kernel_sizes, max_length=args.max_length)
    model.to(device)

    # Initialize logger
    logger = Logger()

    # Initialize checkpoint manager
    checkpoint_manager = CheckpointManager(args.output_dir)

    # Initialize trainer
    trainer = Trainer(model=model, train_data=train_data, val_data=val_data, test_data=test_data,
                      learning_rate=args.learning_rate, batch_size=args.batch_size, num_epochs=args.num_epochs,
                      device=device, logger=logger, checkpoint_manager=checkpoint_manager,
                      train_log_per_k_batch=args.train_log_per_k_batch, save_every_n_epoch=args.save_every_n_epoch)

    if args.train:
        trainer.train()

    if args.test:
        trainer.evaluate()


if __name__ == '__main__':
    main()
