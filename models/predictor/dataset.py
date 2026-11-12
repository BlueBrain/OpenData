import torch
from torch_geometric.data import Data
import numpy as np
import os
from analysis_toolkit.morphology_helper import MorphologyHelper
from analysis_toolkit.electrophysiology_helper import ElectrophysiologyHelper

class NeuronDataset(torch.utils.data.Dataset):
    """
    REAL DATASET for Structural-to-Functional prediction.
    Pairs real morphology (.swc) with real electrophysiology (.nwb).
    """
    def __init__(self, swc_dir, nwb_dir):
        self.swc_files = sorted([f for f in os.listdir(swc_dir) if f.endswith('.swc')])
        self.nwb_dir = nwb_dir
        self.data_list = []

        print(f"Loading real data from {swc_dir}...")
        for swc_file in self.swc_files:
            swc_path = os.path.join(swc_dir, swc_file)
            base_name = os.path.splitext(swc_file)[0]
            nwb_path = os.path.join(nwb_dir, f"{base_name}.nwb")

            if os.path.exists(nwb_path):
                try:
                    # 1. REAL Graph Extraction
                    morph = MorphologyHelper(swc_path)
                    node_features, edge_index = morph.get_graph_data()

                    # 2. REAL Functional Target
                    electro = ElectrophysiologyHelper(nwb_path)
                    time, voltage = electro.get_voltage_trace(electrode_id=0)

                    if voltage is not None:
                        # Use the average absolute voltage as a proxy for "activity level"
                        # In a full PhD, we would use a Spike-Sorted firing rate
                        target = np.mean(np.abs(voltage))

                        x = torch.tensor(node_features, dtype=torch.float)
                        edge_index = torch.tensor(edge_index, dtype=torch.long)
                        y = torch.tensor([target], dtype=torch.float)

                        self.data_list.append(Data(x=x, edge_index=edge_index, y=y))

                    electro.close()
                except Exception as e:
                    print(f"Error processing {swc_file}: {e}")

        print(f"Successfully loaded {len(self.data_list)} real neuron pairs.")

    def __len__(self):
        return len(self.data_list)

    def __getitem__(self, idx):
        return self.data_list[idx]
