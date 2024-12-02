import argparse
from data.data_loader import DataLoader
from models.text_cnn import TextCNN
from trainers.trainer import Trainer
from utils.checkpoint_manager import CheckpointManager
import torch

def main(args):
    # Set device
    device = torch.device('cuda' if args.gpu and torch.cuda.is_available() else 'cpu')

    # Load and preprocess data
    data_loader = DataLoader(batch_size=args.batch_size, max_length=args.max_length)
    dataset = data_loader.load_data()
    tokenized_datasets = data_loader.preprocess_data(dataset)
    _, _, test_loader = data_loader.get_data_loaders(tokenized_datasets)

    # Initialize model
    model = TextCNN(embedding_dim=args.embedding_dim, kernel_sizes=args.kernel_sizes, max_length=args.max_length)

    # Load checkpoint
    checkpoint_manager = CheckpointManager(output_dir=args.output_dir)
    checkpoint_manager.load_checkpoint(model, args.checkpoint_path)

    # Initialize trainer
    trainer = Trainer(model, device=device)

    # Evaluate the model
    accuracy = trainer.evaluate(test_loader)
    print(f'Test Accuracy: {accuracy}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--batch_size', type=int, default=32)
    parser.add_argument('--max_length', type=int, default=50)
    parser.add_argument('--gpu', action='store_true')
    parser.add_argument('--output_dir', type=str, required=True)
    parser.add_argument('--checkpoint_path', type=str, required=True)
    args = parser.parse_args()
    main(args)
