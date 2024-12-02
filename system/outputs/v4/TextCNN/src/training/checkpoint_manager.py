import torch
import os


class CheckpointManager:
    def save_checkpoint(self, model, epoch, output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        checkpoint_path = os.path.join(output_dir, f'model_epoch_{epoch}.pth')
        torch.save(model.state_dict(), checkpoint_path)

    def load_checkpoint(self, path):
        model = TextCNN()  # Assuming TextCNN is imported or defined elsewhere
        model.load_state_dict(torch.load(path))
        return model
