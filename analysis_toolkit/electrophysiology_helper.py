import numpy as np
import matplotlib.pyplot as plt
try:
    from pynwb import NWBHDF5IO
except ImportError:
    NWBHDF5IO = None

class ElectrophysiologyHelper:
    """
    A utility class to simplify the loading and analysis of electrophysiological
    recordings using the PyNWB library.
    """

    def __init__(self, file_path):
        """
        Initialize the helper and load the NWB file.

        :param file_path: Path to the NWB file (.nwb)
        """
        if NWBHDF5IO is None:
            raise ImportError("pynwb library not found. Please install it via pip: pip install pynwb")

        self.file_path = file_path
        self.io = NWBHDF5IO(file_path, mode="r")
        self.nwbfile = self.io.read()

    def get_voltage_trace(self, electrode_id=0):
        """
        Extract the voltage trace from the NWB file.

        :param electrode_id: The index of the electrode to extract.
        :return: Tuple of (time_axis, voltage_values)
        """
        # In NWB files, electrical data is usually stored in acquisitions
        # We search for the first available electrical series
        try:
            # Attempt to actually find the acquisition series
            # This is a generic approach; specific NWB files might have different structures
            series = self.nwbfile.acquisitions['electrical_series'][electrode_id]
            data = series.data[:]

            # Calculate time axis based on sampling rate
            sampling_rate = series.rate
            time = np.arange(len(data)) / sampling_rate

            return time, data
        except (KeyError, IndexError) as e:
            print(f"Error extracting voltage trace: {e}")
            return None, None

    def plot_voltage(self, electrode_id=0):
        """
        Quickly plot the voltage trace for a specific electrode.

        :param electrode_id: The index of the electrode to extract.
        """
        time, voltage = self.get_voltage_trace(electrode_id)
        if time is not None:
            plt.figure(figsize=(12, 4))
            plt.plot(time, voltage, color='blue', linewidth=0.5)
            plt.title(f"Voltage Trace - Electrode {electrode_id}")
            plt.xlabel("Time (s)")
            plt.ylabel("Voltage (mV)")
            plt.grid(True)
            plt.show()
        else:
            print("No data available to plot.")

    def close(self):
        """
        Close the NWB file handle to free up resources.
        """
        self.io.close()

if __name__ == "__main__":
    print("ElectrophysiologyHelper initialized. Provide a valid .nwb path to analyze signals.")
