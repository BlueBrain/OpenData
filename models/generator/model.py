import torch
import torch.nn as nn
import torch.nn.functional as F

class MorphologyGenerator(nn.Module):
    """
    Generator to synthesize biologically plausible neuron structural descriptors.
    """
    def __init__(self, latent_dim, output_dim):
        super(MorphologyGenerator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(latent_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, output_dim),
            nn.Tanh() # Normalize output to [-1, 1]
        )

    def forward(self, z):
        return self.model(z)

class MorphologyDiscriminator(nn.Module):
    """
    Discriminator to distinguish real from synthetic neuron descriptors.
    """
    def __init__(self, input_dim):
        super(MorphologyDiscriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.LeakyReLU(0.2),
            nn.Linear(128, 64),
            nn.LeakyReLU(0.2),
            nn.Linear(64, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.model(x)
