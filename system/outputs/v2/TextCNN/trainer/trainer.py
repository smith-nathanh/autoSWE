import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader as TorchDataLoader
from evaluate import load


class Trainer:
    def __init__(self, learning_rate, batch_size, num_epochs, save_every_n_epoch, output_dir, train_log_per_k_batch):
        self.learning_rate = learning_rate
        self.batch_size = batch_size
        self.num_epochs = num_epochs
        self.save_every_n_epoch = save_every_n_epoch
        self.output_dir = output_dir
        self.train_log_per_k_batch = train_log_per_k_batch
        self.criterion = nn.CrossEntropyLoss()
        self.metric = load('accuracy')

    def train(self, model, train_data, val_data, device):
        optimizer = optim.Adam(model.parameters(), lr=self.learning_rate)
        train_loader = TorchDataLoader(train_data, batch_size=self.batch_size, shuffle=True)
        val_loader = TorchDataLoader(val_data, batch_size=self.batch_size)

        for epoch in range(self.num_epochs):
            model.train()
            for i, batch in enumerate(train_loader):
                inputs, labels = batch['input_ids'].to(device), batch['labels'].to(device)
                optimizer.zero_grad()
                outputs = model(inputs)
                loss = self.criterion(outputs, labels)
                loss.backward()
                optimizer.step()

                if i % self.train_log_per_k_batch == 0:
                    print(f'Epoch [{epoch+1}/{self.num_epochs}], Step [{i+1}/{len(train_loader)}], Loss: {loss.item():.4f}')

            self.evaluate(model, val_loader, device)

            if (epoch + 1) % self.save_every_n_epoch == 0:
                torch.save(model.state_dict(), f'{self.output_dir}/model_epoch_{epoch+1}.pth')

    def evaluate(self, model, data_loader, device):
        model.eval()
        total_loss = 0
        total_accuracy = 0
        with torch.no_grad():
            for batch in data_loader:
                inputs, labels = batch['input_ids'].to(device), batch['labels'].to(device)
                outputs = model(inputs)
                loss = self.criterion(outputs, labels)
                total_loss += loss.item()
                accuracy = self.metric.compute(predictions=outputs.argmax(dim=1), references=labels)
                total_accuracy += accuracy['accuracy']

        avg_loss = total_loss / len(data_loader)
        avg_accuracy = total_accuracy / len(data_loader)
        print(f'Validation Loss: {avg_loss:.4f}, Validation Accuracy: {avg_accuracy:.4f}')

    def save_checkpoint(self):
        pass

    def log_metrics(self):
        pass