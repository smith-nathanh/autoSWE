class Logger:
    def log_training_loss(self, epoch, loss):
        print(f'Epoch {epoch}, Loss: {loss}')

    def log_accuracy(self, accuracy):
        print(f'Accuracy: {accuracy}')
