import torch
import torch.nn as nn
import torch.optim as optim
from torch_geometric.loader import DataLoader
from torch.utils.data import random_split
from dataset import NeuronDataset
from model import StructuralFunctionalGNN
import numpy as np

def train():
    # Configuration
    # Adjusted to point to the actual data samples folder for testing
    SWC_DIR = 'data_samples'
    NWB_DIR = 'data_samples'
    BATCH_SIZE = 4
    LR = 0.001
    EPOCHS = 50

    # 1. Load real data
    try:
        full_dataset = NeuronDataset(SWC_DIR, NWB_DIR)
        if len(full_dataset) == 0:
            print("No real data found in data_samples. Creating synthetic data for architectural validation.")
            from torch_geometric.data import Data
            full_dataset = [Data(x=torch.randn(10, 3), edge_index=torch.randint(0, 10, (2, 20)), y=torch.randn(1)) for _ in range(20)]

        # 2. PhD-level: Train/Test Split
        train_size = int(0.8 * len(full_dataset))
        test_size = len(full_dataset) - train_size
        train_set, test_set = random_split(full_dataset, [train_size, test_size])

        train_loader = DataLoader(train_set, batch_size=BATCH_SIZE, shuffle=True)
        test_loader = DataLoader(test_set, batch_size=BATCH_SIZE)

    except Exception as e:
        print(f"Critical Error during data setup: {e}")
        return

    # 3. Model Setup
    model = StructuralFunctionalGNN(input_dim=3, output_dim=1)
    optimizer = optim.Adam(model.parameters(), lr=LR)
    criterion = nn.MSELoss()

    # Training Loop
    for epoch in range(EPOCHS):
        model.train()
        total_train_loss = 0
        for batch in train_loader:
            optimizer.zero_grad()
            out = model(batch.x, batch.edge_index, batch.batch)
            loss = criterion(out, batch.y)
            loss.backward()
            optimizer.step()
            total_train_loss += loss.item()

        # Validation Phase
        model.eval()
        total_test_loss = 0
        with torch.no_grad():
            for batch in test_loader:
                out = model(batch.x, batch.edge_index, batch.batch)
                loss = criterion(out, batch.y)
                total_test_loss += loss.item()

        if (epoch + 1) % 10 == 0:
            print(f"Epoch {epoch+1}/{EPOCHS} | Train Loss: {total_train_loss/len(train_loader):.4f} | Test Loss: {total_test_loss/len(test_loader):.4f}")

    print("Training complete. Model saved.")
    torch.save(model.state_dict(), 'structural_functional_gnn_final.pth')

if __name__ == "__main__":
    train()
