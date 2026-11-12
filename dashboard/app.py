import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os
import sys

# Add project root to path so we can import the toolkit
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analysis_toolkit.morphology_helper import MorphologyHelper
from analysis_toolkit.electrophysiology_helper import ElectrophysiologyHelper

# Page Config
st.set_page_config(page_title="Blue Brain Open Data Hub", layout="wide", page_icon="🧠")

# Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.title("🧠 Blue Brain Open Data Hub")
st.markdown("""
**Welcome to the interactive gateway for the Blue Brain Project's Open Data.**
This hub allows researchers to quickly analyze neuronal morphologies and electrophysiological recordings without needing to write complex boilerplate code.
""")

st.divider()

# Sidebar Navigation
menu = st.sidebar.selectbox("Navigation", ["Home", "Morphology Analysis", "Electrophysiology Analysis", "About Project"])

if menu == "Home":
    st.subheader("🚀 Get Started")
    col1, col2 = st.columns(2)
    with col1:
        st.info("### 🦴 Morphology\nUpload an `.swc` or `.h5` file to analyze the structural properties of a neuron.")
    with col2:
        st.success("### ⚡ Electrophysiology\nUpload an `.nwb` file to visualize voltage traces and signal activity.")

    st.markdown("""
    ### How to use this Hub:
    1. Select the analysis type from the sidebar.
    2. Upload your data file.
    3. Get instant statistics and interactive visualizations.
    """)

elif menu == "Morphology Analysis":
    st.header("🦴 Neuronal Morphology Analysis")
    uploaded_file = st.file_uploader("Upload a morphology file (.swc, .h5)", type=["swc", "h5"])

    if uploaded_file is not None:
        # Save uploaded file temporarily to disk for MorphoIO to read it
        temp_path = f"temp_{uploaded_file.name}"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        try:
            helper = MorphologyHelper(temp_path)
            stats = helper.get_basic_stats()
            types = helper.get_section_count_by_type()

            # Display Metrics
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Length", f"{stats['total_length']:.2f} μm")
            col2.metric("Total Sections", stats['num_sections'])
            col3.metric("Format", stats['file_format'].upper())

            st.subheader("Soma Position")
            st.write(f"X: {stats['soma_position'][0]:.2f}, Y: {stats['soma_position'][1]:.2f}, Z: {stats['soma_position'][2]:.2f}")

            st.subheader("Section Type Distribution")
            type_df = pd.DataFrame(list(types.items()), columns=['Type', 'Count'])
            st.bar_chart(type_df.set_index('Type'))

        except Exception as e:
            st.error(f"Error processing file: {e}")
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

elif menu == "Electrophysiology Analysis":
    st.header("⚡ Electrophysiology Analysis")
    uploaded_file = st.file_uploader("Upload an NWB file (.nwb)", type=["nwb"])

    if uploaded_file is not None:
        temp_path = f"temp_{uploaded_file.name}"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        try:
            helper = ElectrophysiologyHelper(temp_path)
            time, voltage = helper.get_voltage_trace(electrode_id=0)

            if time is not None:
                st.subheader("Voltage Trace Visualization")

                # Use Plotly for interactive zooming
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=time, y=voltage, mode='lines', line=dict(color='royalblue', width=1)))
                fig.update_layout(
                    title="Electrode 0 - Voltage over Time",
                    xaxis_title="Time (s)",
                    yaxis_title="Voltage (mV)",
                    template="plotly_white"
                )
                st.plotly_chart(fig, use_container_width=True)

                st.metric("Duration", f"{time[-1]:.2f} s")
                st.metric("Max Peak", f"{max(voltage):.2f} mV")
            else:
                st.warning("No voltage data found in the provided NWB file.")

        except Exception as e:
            st.error(f"Error processing file: {e}")
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

elif menu == "About Project":
    st.header("📖 About Blue Brain Open Data")
    st.markdown("""
    This project is a contribution to the **Blue Brain Open Data** initiative.
    The original dataset is an extensive neuroscience resource encompassing experimental, model, and simulation data.

    ### Our Contribution:
    We have transformed the repository from a static data list into a **functional analysis hub**.
    - **Analysis Toolkit**: A Python library for fast morphological and electrical feature extraction.
    - **Interactive Dashboard**: A web-based tool for instant data visualization.
    - **Educational Tutorials**: Guided paths for researchers to enter the field of computational neuroscience.

    **Goal**: To increase the visibility of Blue Brain data and lower the barrier to entry for new researchers.
    """)
