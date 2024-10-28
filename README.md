# Open Data

Blue Brain Open Data represents an extensive neuroscience dataset encompassing a diverse range of data types, including experimental, model, and simulation data, along with images and videos depicting reconstructed neurons and brain regions.

The **experimental data** includes reconstructed morphologies of neurons, astrocytes, and microglia in different brain regions and for different species; single-cell and paired neuron electrophysiological recordings from different brain regions, and ion channels recordings.

The **model data** contains annotation volumes of the mouse brain atlas with cell composition as well as morphological and electrical neuron type densities in different brain regions. It also includes synapse, morphological, electrical, and morpho-electrical neuron models for different cell types as well as ion channels and neuro-glia-vasculature models.

The **simulation data** consists of different in-silico simulation campaigns with detailed experiments that have been conducted at the Blue Brain Project (BBP) and published in several articles. These simulations have proven to be very valuable as a benchmark in many simulation neuroscience contexts.

The **images and videos** provide a collection of high-fidelity rendering of reconstructed neurons, microcircuits and brain regions as well as videos of different brain regions detailing their cellular and molecular composition and their electrical behavior.

The majority of the dataset was created by the Blue Brain Project and its collaborators during the last 18 years and is supplemented by publicly available data integrated within the same framework to ensure comprehensiveness.

# General Usage

The data can be leveraged by the computational and simulation neuroscience community to accelerate fundamental and translational neuroscience research. Some of the applications include, but are not limited to:
* Train machine learning models to classify neurons based on their morphology and electrophysiology.
* Extract electrical-features that can be used to optimize single neuronal models.
* Build single, paired, and clustered neuron models.
* Build morphologically constrained electrical neuron models.
* Reverse engineer cell type densities and distributions from brain images.
* Run simulation experiments using different circuit models.
* Analyze and explore the connectivity within different brain regions.
* Use existing or develop new tools to analyze and validate brain circuit models.
* Run neuro-glia-vasculature simulations for studying the brain’s metabolic system.

# Reconstructed Morphologies

Reconstructed morphologies are provided in one or more formats (swc, asc, or h5v1). All of them can be read with the MorphoIO library.

The [MorphIO](https://morphio.readthedocs.io/en/latest/) library can be used for reading and writing neuron morphology files. It supports the following formats: SWC, ASC (aka. neurolucida), and H5 v1.

It provides 3 C++ classes that are the starting point of every morphology analysis:
* Soma: contains the information related to the soma.
* Section: a section is the succession of points between two bifurcations. To the bare minimum the Section object will contain the section type, the position and diameter of each point.
* Morphology: the morphology object contains general information about the loaded cell but also provides accessors to the different sections.

One important concept is that MorphIO is split into a read-only part and a read/write one. Morphology usage can be split into two APIs: mutable and immutable. Mutable is for creating or editing morphologies. Immutable is for read-only operations. Both are represented in C++ and Python.
 
Examples of MorphoIO usage: https://morphio.readthedocs.io/en/latest/morphology.html
 
The python-based toolkit [NeuroM](https://neurom.readthedocs.io/en/latest/?badge=latest) can be used for the analysis and processing of neuronal morphologies.

Tutorial for using NeuroM: https://neurom.readthedocs.io/en/latest/tutorial.html<br>
Examples of NeuroM usage: https://neurom.readthedocs.io/en/latest/examples.html
 
The python package [TMD](https://tmd.readthedocs.io/en/latest/?badge=latest) performs the topological analysis of neuronal morphologies and extracts the persistence barcodes of trees. This module includes:
* Basic loading of neuronal morphologies in swc and h5 file format.
* Extraction of the topological descriptors of tree morphologies.
* Visualization of neuronal trees and neurons.
* Plotting persistence diagrams, barcodes and images.

Examples of TMD usage:
https://tmd.readthedocs.io/en/latest/?badge=latest#usage
 
Related publications
Comprehensive Morpho-Electrotonic Analysis Shows 2 Distinct Classes of L2 and L3 Pyramidal Neurons in Human Temporal Cortex, Cerebral Cortex
Deitcher Y., Eyal G., Kanari L., et al., Comprehensive Morpho-Electrotonic Analysis Shows 2 Distinct Classes of L2 and L3 Pyramidal Neurons in Human Temporal Cortex, Cerebral Cortex, Volume 27, Issue 11, November 2017, Pages 5398–5414, https://doi.org/10.1093/cercor/bhx226
 
Objective Morphological Classification of Neocortical Pyramidal Cells
Lida Kanari, Srikanth Ramaswamy, Ying Shi, Sebastien Morand, Julie Meystre, Rodrigo Perin, Marwan Abdellah, Yun Wang, Kathryn Hess, Henry Markram, Objective Morphological Classification of Neocortical Pyramidal Cells, Cerebral Cortex, Volume 29, Issue 4, April 2019, Pages 1719-1735, https://doi.org/10.1093/cercor/bhy339
 
The [NeuroTS](https://neurots.readthedocs.io/en/latest/) library can be used for the computational generation of artificial neuronal trees based on the topology of reconstructed cells and their statistical properties. It can be used to perfor the following:
* Synthesize a single neuron from a basic set of inputs
* Synthesize many neurons with the same input parameters and distributions
* Synthesize a single neuron with its diameters using a simple method
* Synthesize a single neuron with its diameters using an external diametrizer
* Extract parameters and distributions that can be used as synthesis inputs

Examples of NeuroTS usage:
https://neurots.readthedocs.io/en/stable/examples/index.html

# Electrophysiological Recordings

Experimental electrophysiological data are available in one or more formats (nwb or abf). The experimental electrophysiology data can be explored via several graphical and command line tools.

*Graphical Tools*:<br>
The following page provides list of tools which you can use locally on your PC to explore and visualize the data:
https://nwb-overview.readthedocs.io/en/latest/tools/analysis_tools_home.html
 
Some useful ones are:
Blue Brain eFEL using Neo:<br>
https://github.com/BlueBrain/eFEL/blob/master/examples/neo/load_nwb.ipynb
 
HDF Tools:<br>
For JupyterLab : https://github.com/silx-kit/jupyterlab-h5web<br>
VS Code plugin, H5Web: https://marketplace.visualstudio.com/items?itemName=h5web.vscode-h5web
 
Command Line Tools:<br>
Using python packages:<br>
pynwb: https://pynwb.readthedocs.io/en/stable/tutorials/general/plot_read_basics.html

e.g.

    from pynwb import NWBHDF5IO
	filepath = "xyz.nwb"
	with NWBHDF5IO(filepath, mode="r") as io2:
    	nwbfile = io2.read()
	nwbfile
 
h5py: https://docs.h5py.org/en/latest/quick.html

e.g

	import h5py
	f = h5py.File('mytestfile.hdf5', 'r')
	f.keys()
 
 # Electrical Models
 
The electrical model folder for different brain regions ( e.g. SSCx, Thalamus) contains two folders:
1. emodels : This folder contains final electrical neuronal models
2. optimisations.tar.gz: the optimisation code used to optimise the cell models in the tar.gz file (optional)

The emodels folder contains subfolders for each electrical type (e-type). Each e-type folder has
* a hoc file usually named model.hoc
* morphology files in the .asc, .swc and .h5 formats
* mechanisms folder contains mod files used for the models
* *.json files used for creating the emodels using BluePyEModel (optional)

To use the e-model you just need the model.hoc file, mechanisms folder and a morphology file in the .asc or swc format. To find the morphology format used in the e-model, please check the hoc file for a line similar to
load_morphology($s2, "C060114A5.asc")

If you want to use the e-models locally on your PC, you can use the BlueCellulab python package:<br>
https://github.com/BlueBrain/BlueCelluLab/tree/main 

Here is an example of how to use the emodels using BlueCellulab:<br>
https://github.com/BlueBrain/BlueCelluLab/blob/main/examples/1-singlecell/singlecell.ipynb 

The optimisation folder (optional) contains 2 main folders:
1. detailed: this folder is used to optimize detailed morphology models.
2. point_neuron: this folder is used to optimize point-neuron models with a simplified ball-and-stick morphology representing soma and axon

These folders use the BluePyEModel pipeline as described in this example:<br> https://github.com/BlueBrain/BluePyEModel/blob/main/examples/L5PC/README.rst 

# Ion Channel Recordings & Models

The Ion Channel experimental data can be processed and analysed using two APIs (Matlab and Python). The documentation of these APIs can be accessed on:<br>
https://channelpedia.epfl.ch/expdata/help/ and comprehensive tutorials can be found on: https://lnmcdata.bbp.epfl.ch/tutorials

# Circuit models and Simulation Campaigns

Circuit models comprise several sub-models (morphologies, electrical models, ion channel models, etc.) and connect them with a set of modeled synapses. They are provided in the [SONATA format](https://sonata-extension.readthedocs.io/en/latest/sonata_overview.html).

Purposes are as follows:
* Running simulations. This can be achieved using [Neurodamus](https://github.com/BlueBrain/neurodamus) as documented [here](https://github.com/BlueBrain/neurodamus/blob/main/README.rst).
* Analyzing simulations: The result of simulations can be analyzed in the context of the circuit that generated it. For this purpose, use [bluepysnap](https://github.com/BlueBrain/snap) as documented [here](https://github.com/BlueBrain/snap/blob/master/README.rst). Note that we provide the output of several scientifically useful simulation campaigns. That means, analyses of simulations can be performed even on systems that do not have the capability of running the simulations themselves (analyses requires fewer resources than running a simulation).
* Further examples of analyses of simulation campaigns can be found in paper-specific data sets on [Zenodo/BlueBrain](https://zenodo.org/communities/bluebrain/).
* Analyzing circuitry: The morphologies contained in a circuit model and the synaptic connectivity of the model can be analyzed and evaluated. For that purpose use [bluepysnap](https://github.com/BlueBrain/snap) as documented [here](https://github.com/BlueBrain/snap/blob/master/README.rst). Useful for more in-depth analyses is our toolbox [Connectome-Utilities](https://github.com/BlueBrain/ConnectomeUtilities).

Circuits are provided in subdirectories that name the type of circuit and organism / region being modeled. 

Simulation campaigns provide the output of simulating a circuit model under specified conditions and with specified stimuli applied. The stimuli and conditions are detailed in simulation-specific simulation_config.json files.
The outputs are:
* Spike times and identities of neurons firing during the simulation (always)
* Soma voltage traces of neurons (optional)
* Extracellular voltages as specified locations (optional)
* Time series of plastic states of synapses (optional)

Analysis of simulations is best performed using [bluepysnap](https://github.com/BlueBrain/snap) as documented [here](https://github.com/BlueBrain/snap/blob/master/README.rst). Note that most useful analyses additionally require the circuit model: E.g., the simulation output specifies identifiers of neurons firing, but to look up their locations and types the circuit model must be referenced. Bluepysnap provides that functionality.

# Brain Images

The software NeuroLucida (https://www.mbfbioscience.com/products/neurolucida/) or Fiji (https://imagej.net/software/fiji/) can be used to view the image stacks obtained the collaboration between Wenzhou Medical University (WMU) and BBP.

The software Vaa3D (https://home.penglab.com/proj/vaa3d/home/index.html) can be used to view the terafly brain image volumes from the collaboration between Southeast University (SEU, China) and BBP.

# Images & Videos

The images and videos folder contains a gallery of images and videos generated from the scientific data that has been generated by or shared with the Blue Brain Project.
A number of different applications have been used to generate these contents,
ranging from commercial photo and video editing tools -- like Maya, Blender,
Photoshop, Houdini, ... -- to in-house developed cutting-edge applications -- like
Brayns, RTNeuron, NeuroMorphoVis, etc.

The visualization of scientific data has been done with the aim of giving a highly
realistic view of the data at a very large scale and level of detail.
 
The data is structured in folders depending on the biological scale: molecular,
cellular or extra-cellular levels and at the end of the folder hierarchy there are
always two subfolders: one for images and another one for videos.
 
The folder structure is as follows, from large to small scale:
- Brain_Systems:
  Visualizations of different brain areas (larger scale than brain regions) and
  whole brain visuals.
 
- Brain_Regions:
  Visualizations of different brain regions:
  - Cerebellum
  - Hippocampus
  - Multiple_Brain_Regions: when more than one brain region is visualized in the
	same visual.
  - Neocortex, with a dedicated subdirectory for the Somatosensory Cortex area.
  - Olfactory_Bulb
  - Thalamus
  - Visual_Cortex
 
- Circuits:
  Visualizations of small neuronal circuits (smaller scale than brain regions),
  called microcircuits. A dedicated subdirectory contains the visuals of the
  neuro-glia-vascular system (NGV).
 
- Paired_Neurons:
  Visualizations of a few, connected neurons.
 
- Single_Neurons:
  Visualizations of single neurons, either alone or inside a circuit.
 
- Molecular_Systems:
  Visualizations of molecular systems mainly related to the brain, including
  ion channel visuals and metabolism-related visuals. A dedicated subdirectory
  contains the visuals of a special project developed at BBP with respect to
  the COVID19 task force effort.
 
- Other:
  Other visualizations that would not fit in the aforementioned categories. A dedicated
  subdirectory contains visuals related to the spinal cord.

# Overall Directory Structure

1. Experimental_Data
* Reconstructed_morphologies
  * Categorized
    * Neurons
      * Mouse
        * Cortex
        * Hippocampus
        * Thalamus
        * Claustrum
        * Olfactory_areas
        * Striatum
        * Endopiriform_nucleus
        * Main_olfactory_bulb
        * Cerebellum
      * Rat
        * Cortex
        * Hippocampus
        * Striatum
        * Basal_ganglia
      * Other
        * Basal_ganglia
  * Uncategorized
    * Neurons
* Electrophysiological_recordings
  * Single-cell_recordings
    * SSCx
    * Thalamus
    * Amygdala
    * Neuromodulation
    * Mouse
      * Hippocampus
      * Substantia_nigra_compact_part
    * Others
  * Paired_Recordings
    * Neuromodulation
      * paired_cells
  * Ion_channels
    * Kv
    * Nav
    * HCN
    * Kir
    * K2P
    * Cav
    * KCa
* Brain_Images
  * Rat_Nissl
  * Image_Stack
  * Terafly
* Bouton_density
* Neuron_density
  * rat_P14
* Transcriptomics
  * Whole_brain
* Literature_curated_data

2. Model_Data
* Morphological_models
  * Rat
    * Hippocampus
  * Mouse
    * BarrelCortex
  * Others
    * Cerebellum
    * Main_olfactory_bulb
    * Striatum
* Electrophysiological_models
  * SSCx
  * Thalamus
  * Others
    * Striatum
* Morpho-Electrical_models
  * Rat
    * Hippocampus
* Synapse_models
  * Others
    * Striatum
* Ion_Channel_models
  * Others
    * Striatum
* Circuits
  * Simplified_connectome
    * Topological_characterization
      * SSCx
      * Thalamus
      * Amygdala
      * Hippocampus
      * Others
    * Connectivity_model
      * SSCx
      * Thalamus
      * Amygdala
      * Hippocampus
      * Others
  * Brain_regions
    * Rat
    * Hybrid
* Brain_atlas
  * Mouse
* NGV

3. Simulation_data
* Simulation_Campaigns
  * SSCx
  * Thalamus
  * Amygdala
  * Hippocampus
  * Others
* Simulation_Analysis
  * SSCx
  
 4. Images_Videos
* Brain_Systems
  * Whole_Brain
* Brain_Regions
  * Hippocampus
  * Neocortex
  * Thalamus
  * Multiple_Brain_Regions
  * Cerebellum
  * Olfactory_Bulb
  * Visual_Cortex
* Circuits
  * Microcircuits
  * NGV
* Molecular_Systems
  * Ion_Channels
  * Metabolism
  * COVID19
* Paired_Neurons
* Single_Neurons
* Other
  * Spinal_Cord
  * Videos
  * Images

