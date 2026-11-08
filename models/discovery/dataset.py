import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np
import os
from analysis_toolkit.morphology_helper import MorphologyHelper
from analysis_toolkit.electrophysiology_helper import ElectrophysiologyHelper

class CellTypeDataset(Dataset):
    """
    Dataset for Unsupervised Cell-Type Discovery.
    Extracts features from both morphology and electrophysiology.
    """
    def __init__(self, swc_dir, nwb_dir):
        self.swc_files = sorted([f for f in os.listdir(swc_dir) if f.endswith('.swc')])
        self.nwb_dir = nwb_dir
        self.features = []

        for swc_file in self.swc_files:
            swc_path = os.path.join(swc_dir, swc_file)
            base_name = os.path.splitext(swc_file)[0]
            nwb_path = os.path.join(nwb_dir, f"{base_name}.nwb")

            if os.path.exists(nwb_path):
                try:
                    # Morphology features (e.g., total length, num sections)
                    morph = MorphologyHelper(swc_path)
                    stats = morph.get_basic_stats()
                    m_feat = np.array([stats['total_length'], stats['num_sections']])
                    
                    # Electrophysiology features (e.g., avg voltage, peak freq)
                    electro = ElectrophysiologyHelper(nwb_path)
                    time, voltage = electro.get_voltage_trace()
                    if voltage is not None:
                        e_feat = np.array([np.mean(voltage), np.std(voltage)])
                    else:
                        e_feat = np.zeros(2)
                    electro.close()
                    
                    combined = np.concatenate([m_feat, e_feat])
                    self.features.append(combined)
                except Exception as e:
                    print(f"Error processing {swc_file}: {e}")

        self.features = torch.tensor(np.array(self.features), dtype=torch.float)

    def __len__(self):
        return len(self.features)

    def __getitem__(self, idx):
        return self.features[idx]
