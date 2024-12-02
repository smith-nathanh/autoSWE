class Logger:
    def log_training_loss(self, epoch, batch, loss):
        print(f'Epoch [{epoch+1}], Batch [{batch+1}], Loss: {loss:.4f}')

    def log_accuracy(self, epoch, accuracy):
        print(f'Epoch [{epoch+1}], Validation Accuracy: {accuracy:.4f}')

    def log_test_accuracy(self, accuracy):
        print(f'Test Accuracy: {accuracy:.4f}')