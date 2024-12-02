import argparse
import torch
from data.data_loader import DataLoader
from model.text_cnn import TextCNN
from training.trainer import Trainer
from training.checkpoint_manager import CheckpointManager
from utils.logger import Logger


def parse_args():
    parser = argparse.ArgumentParser(description='Train or test a TextCNN model.')
    parser.add_argument('--learning_rate', type=float, default=1e-3, help='Learning rate for training')
    parser.add_argument('--batch_size', type=int, default=32, help='Batch size for training')
    parser.add_argument('--num_epochs', type=int, default=10, help='Number of epochs for training')
    parser.add_argument('--embedding_dim', type=int, default=500, help='Dimension of embedding')
    parser.add_argument('--kernel_sizes', nargs='+', type=int, default=[3, 4, 5], help='Kernel sizes')
    parser.add_argument('--max_length', type=int, default=50, help='Maximum length of sequence')
    parser.add_argument('--save_every_n_epoch', type=int, default=1, help='Save model every n epochs')
    parser.add_argument('--train', action='store_true', help='Train the model')
    parser.add_argument('--test', action='store_true', help='Test the model')
    parser.add_argument('--output_dir', type=str, required=True, help='Output directory')
    parser.add_argument('--gpu', action='store_true', help='Use GPU')
    parser.add_argument('--train_log_per_k_batch', type=int, default=10, help='Log training loss every k batches')
    parser.add_argument('--random_seed', type=int, default=42, help='Random seed')
    return parser.parse_args()


def main():
    args = parse_args()

    # Set random seed for reproducibility
    torch.manual_seed(args.random_seed)
    if args.gpu and torch.cuda.is_available():
        torch.cuda.manual_seed(args.random_seed)

    # Load data
    data_loader = DataLoader()
    train_data, val_data, test_data = data_loader.load_data()

    # Initialize model
    model = TextCNN(embedding_dim=args.embedding_dim, kernel_sizes=args.kernel_sizes, max_length=args.max_length)

    # Initialize trainer
    trainer = Trainer(learning_rate=args.learning_rate, batch_size=args.batch_size, num_epochs=args.num_epochs,
                      save_every_n_epoch=args.save_every_n_epoch, train_log_per_k_batch=args.train_log_per_k_batch,
                      output_dir=args.output_dir, gpu=args.gpu)

    # Train or test
    if args.train:
        trainer.train(model, train_data, val_data)
    elif args.test:
        checkpoint_manager = CheckpointManager()
        model = checkpoint_manager.load_checkpoint(args.output_dir)
        accuracy = trainer.evaluate(model, test_data)
        print(f'Test Accuracy: {accuracy}')


if __name__ == '__main__':
    main()
