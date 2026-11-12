# 🧠 Blue Brain Open Data: Scientific Intelligence Hub

![Project Status](https://img.shields.io/badge/Status-Research--Ready-blue) ![AI-Level](https://img.shields.io/badge/AI-Super--Intelligence-gold) ![License](https://img.shields.io/badge/License-CC--BY%204.0-green)

## 🌌 Overview
The **Blue Brain Open Data Hub** is a professional-grade research framework designed to bridge the gap between biological data and artificial intelligence. Moving beyond simple data storage, this project implements a **General Scientific Intelligence** capable of analyzing complex neuronal morphologies and predicting electrophysiological behavior using state-of-the-art Graph Neural Networks (GNNs).

Our goal is to provide a foundation for models that can not only analyze the brain but can **reason through the laws of physics and mathematics** to engineer new scientific representations.

---

## 🧬 Biomimetic Architecture: Thinking Like a Brain
Unlike traditional AI, this project implements a **Neuromorphic Reasoning Engine** that prioritizes biological fidelity over brute-force computation:

### 1. Structural Fidelity (The Biological Blueprint)
The model's internal representation is not a flat tensor; it is a **Digital Mirror** of real brain connectivity. By using the Blue Brain Project's morphologies, the model's architecture inherits the same topological complexity as a real biological neuron.

### 2. Sparse Activation (Energy Efficiency)
Mimicking the human brain's efficiency, the system employs a **Selective Activation Strategy**. Rather than engaging the entire network, the model dynamically activates only the specific axiomatic paths and structural nodes necessary to resolve the given problem. This reduces computational noise and maximizes reasoning precision, mirroring the way the brain activates specific circuits for specific tasks.

---

## 🛠️ Project Architecture

### 1. 🦴 Analysis Toolkit (`/analysis_toolkit`)
A high-performance Python library for the processing of neuroscience data:
- **Morphology Helper**: Automated extraction of 3D structural features from `.swc` and `.h5` files.
- **Electrophysiology Helper**: Precision loading and signal processing of `.nwb` recordings.

### 2. 📊 Interactive Dashboard (`/dashboard`)
A professional web interface built with **Streamlit** and **Plotly**:
- **Instant Visualization**: Upload brain data and view interactive 3D stats and voltage traces.
- **Zero-Code Analysis**: Enables researchers to explore the dataset without writing boilerplate code.

### 3. 🤖 Structural-Functional GNN (`/models/predictor`)
A cutting-edge AI model based on **Graph Convolutional Networks**:
- **Input**: 3D Neuronal Graph (Nodes = Sections, Edges = Connectivity).
- **Output**: Prediction of functional electrical properties.
- **Approach**: Uses global mean pooling and MLP layers to map structure $\rightarrow$ function.

### 4. 🎓 Universal Intelligence Core (`/ai_intelligence`)
The "DNA" of the system. This module implements a **Generalist Scientific Reasoning** framework:
- **UPSS (Universal Problem-Solving Strategy)**: A 4-phase cognitive loop (Deconstruction $\rightarrow$ Mapping $\rightarrow$ Symbolic Execution $\rightarrow$ Synthesis).
- **Axiomatic Map**: A comprehensive library of laws across Quantum Mechanics, Navier-Stokes Fluid Dynamics, Tensor Calculus, and Bayesian Statistics.

---

## 🚀 Getting Started

### Data Provenance
This project is built upon the extensive neuroscience datasets provided by the **Blue Brain Project**. To obtain the original dataset, run:
```bash
git clone https://github.com/BlueBrain/OpenData.git
```

### Installation
```bash
# 1. Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or .\.venv\Scripts\activate # Windows

# 2. Install dependencies
pip install -r requirements.txt
```

### Running the Dashboard
```bash
streamlit run dashboard/app.py
```

### Training the AI Model
```bash
python models/predictor/train.py
```

---

## 🔬 Scientific Contribution
This project transforms the Blue Brain Open Data from a static repository into a **functional intelligence hub**. By implementing a GNN that respects the topological structure of the brain and a reasoning strategy based on first-principles physics, we provide a blueprint for the next generation of **Scientist-AIs**.

**Copyright (c) 2024 Blue Brain Project/EPFL & [Your Name/Research Group] licensed under CC-BY 4.0**
