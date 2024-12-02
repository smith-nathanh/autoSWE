import torch
import torch.nn as nn
import torch.nn.functional as F


class TextCNN(nn.Module):
    def __init__(self, config):
        super(TextCNN, self).__init__()
        self.embedding = nn.Embedding(30522, config.embedding_dim)  # Assuming BERT tokenizer vocab size
        self.convs = nn.ModuleList([
            nn.Conv2d(1, 100, (k, config.embedding_dim)) for k in config.kernel_sizes
        ])
        self.fc = nn.Linear(len(config.kernel_sizes) * 100, 2)  # Binary classification

    def forward(self, x):
        x = self.embedding(x)
        x = x.unsqueeze(1)  # Add channel dimension
        x = [F.relu(conv(x)).squeeze(3) for conv in self.convs]
        x = [F.max_pool1d(i, i.size(2)).squeeze(2) for i in x]
        x = torch.cat(x, 1)
        x = self.fc(x)
        return x