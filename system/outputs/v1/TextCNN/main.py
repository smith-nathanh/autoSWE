import argparse
from scripts.train import main as train_main
from scripts.test import main as test_main

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', action='store_true', help='Train the model')
    parser.add_argument('--test', action='store_true', help='Test the model')
    parser.add_argument('--learning_rate', type=float, default=1e-3)
    parser.add_argument('--batch_size', type=int, default=32)
    parser.add_argument('--num_epochs', type=int, default=10)
    parser.add_argument('--embedding_dim', type=int, default=500)
    parser.add_argument('--kernel_sizes', nargs='+', type=int, default=[3, 4, 5])
    parser.add_argument('--max_length', type=int, default=50)
    parser.add_argument('--save_every_n_epoch', type=int, default=1)
    parser.add_argument('--output_dir', type=str, required=True)
    parser.add_argument('--gpu', action='store_true')
    parser.add_argument('--train_log_per_k_batch', type=int, default=10)
    parser.add_argument('--random_seed', type=int, default=42)
    parser.add_argument('--checkpoint_path', type=str, help='Path to the checkpoint file for testing')
    args = parser.parse_args()

    if args.train:
        train_main(args)
    elif args.test:
        test_main(args)
    else:
        print("Please specify --train or --test")
