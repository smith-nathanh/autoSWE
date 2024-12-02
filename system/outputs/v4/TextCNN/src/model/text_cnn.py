import torch
import torch.nn as nn
import torch.nn.functional as F


class TextCNN(nn.Module):
    def __init__(self, embedding_dim, kernel_sizes, max_length):
        super(TextCNN, self).__init__()
        self.embedding_dim = embedding_dim
        self.kernel_sizes = kernel_sizes
        self.max_length = max_length

        self.embedding = nn.EmbeddingBag(embedding_dim, max_length, sparse=True)
        self.convs = nn.ModuleList([
            nn.Conv2d(1, 100, (k, embedding_dim)) for k in kernel_sizes
        ])
        self.fc = nn.Linear(len(kernel_sizes) * 100, 2)  # Assuming binary classification

    def forward(self, x):
        x = self.embedding(x)
        x = x.unsqueeze(1)  # Add channel dimension
        x = [F.relu(conv(x)).squeeze(3) for conv in self.convs]
        x = [F.max_pool1d(i, i.size(2)).squeeze(2) for i in x]
        x = torch.cat(x, 1)
        x = self.fc(x)
        return x
