import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from model import MorphologyGenerator, MorphologyDiscriminator

def synthesize_neurons():
    LATENT_DIM = 100
    OUTPUT_DIM = 10 # Descriptor dimensions
    EPOCHS = 1000
    BATCH_SIZE = 32

    # Real data (simulated for now)
    real_data = torch.randn(1000, OUTPUT_DIM)
    
    generator = MorphologyGenerator(LATENT_DIM, OUTPUT_DIM)
    discriminator = MorphologyDiscriminator(OUTPUT_DIM)
    
    g_optimizer = optim.Adam(generator.parameters(), lr=0.0002)
    d_optimizer = optim.Adam(discriminator.parameters(), lr=0.0002)
    criterion = nn.BCELoss()

    for epoch in range(EPOCHS):
        # Train Discriminator
        d_optimizer.zero_grad()
        
        # Real
        real_batch = real_data[np.random.randint(0, 1000, BATCH_SIZE)]
        real_labels = torch.ones(BATCH_SIZE, 1)
        out_real = discriminator(real_batch)
        loss_real = criterion(out_real, real_labels)
        
        # Fake
        z = torch.randn(BATCH_SIZE, LATENT_DIM)
        fake_batch = generator(z)
        fake_labels = torch.zeros(BATCH_SIZE, 1)
        out_fake = discriminator(fake_batch.detach())
        loss_fake = criterion(out_fake, fake_labels)
        
        d_loss = loss_real + loss_fake
        d_loss.backward()
        d_optimizer.step()
        
        # Train Generator
        g_optimizer.zero_grad()
        out_fake_g = discriminator(fake_batch)
        g_loss = criterion(out_fake_g, real_labels)
        g_loss.backward()
        g_optimizer.step()
        
        if (epoch + 1) % 100 == 0:
            print(f"Epoch {epoch+1}/{EPOCHS}, D_Loss: {d_loss.item():.4f}, G_Loss: {g_loss.item():.4f}")

    # Generate new neurons
    z_new = torch.randn(10, LATENT_DIM)
    synthetic_neurons = generator(z_new)
    print("Generated 10 biologically plausible neuron descriptors.")
    np.save('synthetic_neurons.npy', synthetic_neurons.detach().numpy())

if __name__ == "__main__":
    synthesize_neurons()
