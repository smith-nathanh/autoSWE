import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from utils.logger import Logger
from training.checkpoint_manager import CheckpointManager


class Trainer:
    def __init__(self, learning_rate, batch_size, num_epochs, save_every_n_epoch, train_log_per_k_batch, output_dir, gpu):
        self.learning_rate = learning_rate
        self.batch_size = batch_size
        self.num_epochs = num_epochs
        self.save_every_n_epoch = save_every_n_epoch
        self.train_log_per_k_batch = train_log_per_k_batch
        self.output_dir = output_dir
        self.device = torch.device('cuda' if gpu and torch.cuda.is_available() else 'cpu')
        self.logger = Logger()
        self.checkpoint_manager = CheckpointManager()

    def train(self, model, train_data, val_data):
        model.to(self.device)
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(model.parameters(), lr=self.learning_rate)

        train_loader = DataLoader(train_data, batch_size=self.batch_size, shuffle=True)
        val_loader = DataLoader(val_data, batch_size=self.batch_size)

        for epoch in range(self.num_epochs):
            model.train()
            total_loss = 0
            for i, batch in enumerate(train_loader):
                inputs, labels = batch['input_ids'].to(self.device), batch['label'].to(self.device)
                optimizer.zero_grad()
                outputs = model(inputs)
                loss = criterion(outputs, labels)
                loss.backward()
                optimizer.step()

                total_loss += loss.item()
                if (i + 1) % self.train_log_per_k_batch == 0:
                    self.logger.log_training_loss(i + 1, total_loss / self.train_log_per_k_batch)
                    total_loss = 0

            val_accuracy = self.evaluate(model, val_loader)
            self.logger.log_accuracy(epoch + 1, val_accuracy)

            if (epoch + 1) % self.save_every_n_epoch == 0:
                self.checkpoint_manager.save_checkpoint(model, epoch + 1, self.output_dir)

    def evaluate(self, model, data_loader):
        model.eval()
        correct = 0
        total = 0
        with torch.no_grad():
            for batch in data_loader:
                inputs, labels = batch['input_ids'].to(self.device), batch['label'].to(self.device)
                outputs = model(inputs)
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()
        return correct / total
