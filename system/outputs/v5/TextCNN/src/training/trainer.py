import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader


class Trainer:
    def __init__(self, model, train_data, val_data, test_data, learning_rate, batch_size, num_epochs, device, logger, checkpoint_manager, train_log_per_k_batch, save_every_n_epoch):
        self.model = model
        self.train_data = train_data
        self.val_data = val_data
        self.test_data = test_data
        self.learning_rate = learning_rate
        self.batch_size = batch_size
        self.num_epochs = num_epochs
        self.device = device
        self.logger = logger
        self.checkpoint_manager = checkpoint_manager
        self.train_log_per_k_batch = train_log_per_k_batch
        self.save_every_n_epoch = save_every_n_epoch

        self.criterion = nn.BCEWithLogitsLoss()
        self.optimizer = optim.Adam(self.model.parameters(), lr=self.learning_rate)

    def train(self):
        self.model.train()
        train_loader = DataLoader(self.train_data, batch_size=self.batch_size, shuffle=True)
        val_loader = DataLoader(self.val_data, batch_size=self.batch_size)

        best_val_accuracy = 0

        for epoch in range(self.num_epochs):
            total_loss = 0
            correct = 0
            total = 0

            for i, batch in enumerate(train_loader):
                inputs, labels = batch['input_ids'].to(self.device), batch['label'].to(self.device)
                self.optimizer.zero_grad()
                outputs = self.model(inputs)
                loss = self.criterion(outputs, labels.float())
                loss.backward()
                self.optimizer.step()

                total_loss += loss.item()
                predicted = torch.round(torch.sigmoid(outputs))
                correct += (predicted == labels).sum().item()
                total += labels.size(0)

                if (i + 1) % self.train_log_per_k_batch == 0:
                    self.logger.log_training_loss(epoch, i, total_loss / (i + 1))

            train_accuracy = correct / total
            val_accuracy = self.evaluate(val_loader)

            self.logger.log_accuracy(epoch, train_accuracy, val_accuracy)

            if val_accuracy > best_val_accuracy:
                best_val_accuracy = val_accuracy
                self.checkpoint_manager.save_checkpoint(self.model, epoch, best_val_accuracy)

            if (epoch + 1) % self.save_every_n_epoch == 0:
                self.checkpoint_manager.save_checkpoint(self.model, epoch, val_accuracy)

    def evaluate(self, data_loader=None):
        self.model.eval()
        if data_loader is None:
            data_loader = DataLoader(self.test_data, batch_size=self.batch_size)

        correct = 0
        total = 0

        with torch.no_grad():
            for batch in data_loader:
                inputs, labels = batch['input_ids'].to(self.device), batch['label'].to(self.device)
                outputs = self.model(inputs)
                predicted = torch.round(torch.sigmoid(outputs))
                correct += (predicted == labels).sum().item()
                total += labels.size(0)

        accuracy = correct / total
        self.logger.log_test_accuracy(accuracy)
        return accuracy