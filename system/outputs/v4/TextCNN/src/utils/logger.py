class Logger:
    def log_training_loss(self, batch, loss):
        print(f'Batch {batch}: Training Loss: {loss:.4f}')

    def log_accuracy(self, epoch, accuracy):
        print(f'Epoch {epoch}: Validation Accuracy: {accuracy:.4f}')
