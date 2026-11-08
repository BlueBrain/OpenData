import torch
import torch.optim as optim
from torch.utils.data import DataLoader
from dataset import CellTypeDataset
from model import CellTypeVAE, vae_loss
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def discover_types():
    SWC_DIR = 'data/morphologies'
    NWB_DIR = 'data/electrophysiology'
    LATENT_DIM = 2
    EPOCHS = 50
    
    try:
        dataset = CellTypeDataset(SWC_DIR, NWB_DIR)
        loader = DataLoader(dataset, batch_size=16, shuffle=True)
    except Exception as e:
        print(f"Data loading failed: {e}. Using synthetic data.")
        features = torch.randn(100, 4) # Dummy 4D features
        loader = DataLoader(features, batch_size=16, shuffle=True)
        dataset = type('obj', (object,), {'features': features})

    model = CellTypeVAE(input_dim=4, latent_dim=LATENT_DIM)
    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    model.train()
    for epoch in range(EPOCHS):
        for batch in loader:
            optimizer.zero_grad()
            recon, mu, logvar = model(batch)
            loss = vae_loss(recon, batch, mu, logvar)
            loss.backward()
            optimizer.step()

    # Extract latent space
    model.eval()
    with torch.no_grad():
        mu, _ = model.encode(dataset.features)
        latent_space = mu.numpy()

    # Cluster types
    kmeans = KMeans(n_clusters=3, n_init=10)
    clusters = kmeans.fit_predict(latent_space)

    plt.figure(figsize=(8, 6))
    plt.scatter(latent_space[:, 0], latent_space[:, 1], c=clusters, cmap='viridis')
    plt.title("Latent Space Cell-Type Discovery")
    plt.xlabel("Dimension 1")
    plt.ylabel("Dimension 2")
    plt.colorbar(label="Cluster ID")
    plt.savefig('cell_type_clusters.png')
    print("Discovery complete. Clusters saved to cell_type_clusters.png")

if __name__ == "__main__":
    discover_types()
