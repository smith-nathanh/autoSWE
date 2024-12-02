import torch
import os

class CheckpointManager:
    def __init__(self, output_dir='./outputs'):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def save_checkpoint(self, model, epoch):
        checkpoint_path = os.path.join(self.output_dir, f'model_epoch_{epoch}.pt')
        torch.save(model.state_dict(), checkpoint_path)

    def load_checkpoint(self, model, checkpoint_path):
        model.load_state_dict(torch.load(checkpoint_path))
