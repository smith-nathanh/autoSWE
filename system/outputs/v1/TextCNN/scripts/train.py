import argparse
from data.data_loader import DataLoader
from models.text_cnn import TextCNN
from trainers.trainer import Trainer
import torch

def main(args):
    # Set device
    device = torch.device('cuda' if args.gpu and torch.cuda.is_available() else 'cpu')

    # Load and preprocess data
    data_loader = DataLoader(batch_size=args.batch_size, max_length=args.max_length)
    dataset = data_loader.load_data()
    tokenized_datasets = data_loader.preprocess_data(dataset)
    train_loader, val_loader, _ = data_loader.get_data_loaders(tokenized_datasets)

    # Initialize model
    model = TextCNN(embedding_dim=args.embedding_dim, kernel_sizes=args.kernel_sizes, max_length=args.max_length)

    # Initialize trainer
    trainer = Trainer(model, learning_rate=args.learning_rate, batch_size=args.batch_size, num_epochs=args.num_epochs, device=device)

    # Train the model
    trainer.train(train_loader, val_loader)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--learning_rate', type=float, default=1e-3)
    parser.add_argument('--batch_size', type=int, default=32)
    parser.add_argument('--num_epochs', type=int, default=10)
    parser.add_argument('--embedding_dim', type=int, default=500)
    parser.add_argument('--kernel_sizes', nargs='+', type=int, default=[3, 4, 5])
    parser.add_argument('--max_length', type=int, default=50)
    parser.add_argument('--gpu', action='store_true')
    args = parser.parse_args()
    main(args)
