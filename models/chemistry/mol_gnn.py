import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GATConv, global_mean_pool

class MolecularGNN(torch.nn.Module):
    """
    Advanced GNN for Molecular Design and Protein-Ligand Interaction.
    Uses Graph Attention Networks (GAT) to identify critical atoms
    in a chemical structure.
    """
    def __init__(self, atom_features_dim, output_dim):
        super(MolecularGNN, self).__init__()

        # Graph Attention Layers: Learns which atoms are most important for the property
        self.conv1 = GATConv(atom_features_dim, 32, heads=4, concat=True)
        self.conv2 = GATConv(32 * 4, 64, heads=4, concat=True)
        self.conv3 = GATConv(64 * 4, 32, heads=1, concat=False)

        # Readout layer for global molecular properties
        self.fc1 = nn.Linear(32, 16)
        self.fc2 = nn.Linear(16, output_dim)

    def forward(self, x, edge_index, batch):
        # 1. Multi-head Attention layers
        x = F.elu(self.conv1(x, edge_index))
        x = F.elu(self.conv2(x, edge_index))
        x = F.elu(self.conv3(x, edge_index))

        # 2. Global Pooling to get one vector for the whole molecule
        x = global_mean_pool(x, batch)

        # 3. Property Prediction
        x = F.relu(self.fc1(x))
        x = self.fc2(x)

        return x

if __name__ == "__main__":
    print("MolecularGNN initialized. Ready for chemical design tasks.")
