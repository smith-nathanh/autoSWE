class Logger:
    def log_training_loss(self, epoch, batch, loss):
        print(f'Epoch [{epoch}], Batch [{batch}], Loss: {loss:.4f}')

    def log_accuracy(self, epoch, train_accuracy, val_accuracy):
        print(f'Epoch [{epoch}], Train Accuracy: {train_accuracy:.4f}, Validation Accuracy: {val_accuracy:.4f}')

    def log_test_accuracy(self, accuracy):
        print(f'Test Accuracy: {accuracy:.4f}')