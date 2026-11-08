import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GCNConv, global_mean_pool

class StructuralFunctionalGNN(torch.nn.Module):
    """
    GNN for predicting functional properties from structural morphology.
    """
    def __init__(self, input_dim, output_dim):
        super(StructuralFunctionalGNN, self).__init__()
        
        # Graph Convolutional Layers
        self.conv1 = GCNConv(input_dim, 64)
        self.conv2 = GCNConv(64, 128)
        self.conv3 = GCNConv(128, 64)
        
        # Fully connected layers for final prediction
        self.fc1 = nn.Linear(64, 32)
        self.fc2 = nn.Linear(32, output_dim)

    def forward(self, x, edge_index, batch):
        # 1. Node embeddings via GCN
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        x = F.relu(x)
        x = self.conv3(x, edge_index)
        x = F.relu(x)
        
        # 2. Global pooling: Aggregate node features into a single cell-level embedding
        x = global_mean_pool(x, batch)
        
        # 3. MLP for functional prediction
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        
        return x
