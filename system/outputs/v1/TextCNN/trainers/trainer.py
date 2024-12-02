import torch
import torch.nn as nn
import torch.optim as optim
from utils.logger import Logger
from utils.checkpoint_manager import CheckpointManager

class Trainer:
    def __init__(self, model, learning_rate=1e-3, batch_size=32, num_epochs=10, device='cpu'):
        self.model = model
        self.learning_rate = learning_rate
        self.batch_size = batch_size
        self.num_epochs = num_epochs
        self.device = device
        self.logger = Logger()
        self.checkpoint_manager = CheckpointManager()

    def train(self, train_loader, val_loader):
        self.model.to(self.device)
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(self.model.parameters(), lr=self.learning_rate)

        for epoch in range(self.num_epochs):
            self.model.train()
            total_loss = 0
            for batch in train_loader:
                inputs, labels = batch['input_ids'].to(self.device), batch['label'].to(self.device)
                optimizer.zero_grad()
                outputs = self.model(inputs)
                loss = criterion(outputs, labels)
                loss.backward()
                optimizer.step()

                total_loss += loss.item()

            avg_loss = total_loss / len(train_loader)
            self.logger.log_training_loss(epoch, avg_loss)

            # Validation
            self.evaluate(val_loader)

            # Save checkpoint
            self.checkpoint_manager.save_checkpoint(self.model, epoch)

    def evaluate(self, data_loader):
        self.model.eval()
        correct = 0
        total = 0
        with torch.no_grad():
            for batch in data_loader:
                inputs, labels = batch['input_ids'].to(self.device), batch['label'].to(self.device)
                outputs = self.model(inputs)
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        accuracy = correct / total
        self.logger.log_accuracy(accuracy)
        return accuracy
