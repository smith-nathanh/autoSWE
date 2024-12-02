import torch
import torch.nn as nn
import torch.optim as optim
from train.logger import Logger


class Trainer:
    def __init__(self, config, model, train_data, val_data, test_data):
        self.config = config
        self.model = model
        self.train_data = train_data
        self.val_data = val_data
        self.test_data = test_data
        self.device = torch.device('cuda' if config.gpu and torch.cuda.is_available() else 'cpu')
        self.model.to(self.device)
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.Adam(self.model.parameters(), lr=config.learning_rate)
        self.logger = Logger()

    def train(self):
        for epoch in range(self.config.num_epochs):
            self.model.train()
            total_loss = 0
            for i, batch in enumerate(self.train_data):
                inputs, labels = batch['input_ids'].to(self.device), batch['label'].to(self.device)
                self.optimizer.zero_grad()
                outputs = self.model(inputs)
                loss = self.criterion(outputs, labels)
                loss.backward()
                self.optimizer.step()

                total_loss += loss.item()
                if (i + 1) % self.config.train_log_per_k_batch == 0:
                    self.logger.log_training_loss(epoch, i, total_loss / self.config.train_log_per_k_batch)
                    total_loss = 0

            self.evaluate(epoch)

            if (epoch + 1) % self.config.save_every_n_epoch == 0:
                self.save_checkpoint(epoch)

    def evaluate(self, epoch=None):
        self.model.eval()
        correct = 0
        total = 0
        with torch.no_grad():
            for batch in self.val_data:
                inputs, labels = batch['input_ids'].to(self.device), batch['label'].to(self.device)
                outputs = self.model(inputs)
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        accuracy = correct / total
        if epoch is not None:
            self.logger.log_accuracy(epoch, accuracy)
        return accuracy

    def save_checkpoint(self, epoch):
        torch.save(self.model.state_dict(), f'{self.config.output_dir}/model_epoch_{epoch}.pth')