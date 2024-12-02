import os
import torch


class CheckpointManager:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def save_checkpoint(self, model, epoch, accuracy):
        checkpoint_path = os.path.join(self.output_dir, f'model_epoch_{epoch}_acc_{accuracy:.2f}.pt')
        torch.save(model.state_dict(), checkpoint_path)

    def load_checkpoint(self, model, checkpoint_path):
        model.load_state_dict(torch.load(checkpoint_path))
        return model