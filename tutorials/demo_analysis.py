import os
import sys

# Add project root to path so we can import our toolkit
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analysis_toolkit.morphology_helper import MorphologyHelper
from analysis_toolkit.electrophysiology_helper import ElectrophysiologyHelper

def run_demo():
    print("=== Blue Brain Open Data: Integrated Analysis Demo ===\n")

    # 1. Morphology Analysis
    print("[Step 1] Analyzing Neuronal Morphology...")
    # In a real scenario, we would use a path from the dataset
    morph_path = "data_samples/sample_neuron.swc"
    try:
        morph = MorphologyHelper(morph_path)
        stats = morph.get_basic_stats()
        print(f"-> Neuron loaded successfully!")
        print(f"-> Total Length: {stats['total_length']:.2f} microns")
        print(f"-> Number of Sections: {stats['num_sections']}")
        print(f"-> Soma Position: {stats['soma_position']}")
    except Exception as e:
        print(f"-> Skipping Morphology Demo: {e} (No sample file found)")

    print("\n" + "-"*50 + "\n")

    # 2. Electrophysiology Analysis
    print("[Step 2] Analyzing Electrical Activity...")
    ephys_path = "data_samples/sample_recording.nwb"
    try:
        ephys = ElectrophysiologyHelper(ephys_path)
        time, voltage = ephys.get_voltage_trace(electrode_id=0)
        if time is not None:
            print(f"-> Recording loaded successfully!")
            print(f"-> Duration: {time[-1]:.2f} seconds")
            print(f"-> Max Voltage: {np.max(voltage):.2f} mV")
            # ephys.plot_voltage() # This would open a window
        else:
            print("-> No voltage data found in file.")
    except Exception as e:
        print(f"-> Skipping Ephys Demo: {e} (No sample file found)")

    print("\n=== Demo Complete ===")

if __name__ == "__main__":
    import numpy as np # Required for the stats display
    run_demo()
