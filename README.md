# OpenData

Blue Brain Open Data represents an extensive neuroscience dataset encompassing a diverse range of data types, including experimental, model, and simulation data, along with images and videos depicting reconstructed neurons and brain regions.

The experimental data includes reconstructed morphologies of neurons, astrocytes, and microglia in different brain regions and for different species; single-cell and paired neuron electrophysiological recordings from different brain regions, and ion channels recordings.

The model data contains annotation volumes of the mouse brain atlas with cell composition as well as morphological and electrical neuron type densities in different brain regions. It also includes synapse, morphological, electrical, and morpho-electrical neuron models for different cell types as well as ion channels and neuro-glia-vasculature models.
The simulation data consists of different in-silico simulation campaigns with detailed experiments that have been conducted at the Blue Brain Project (BBP) and published in several articles. These simulations have proven to be very valuable as a benchmark in many simulation neuroscience contexts.

The images and videos provide a collection of high-fidelity rendering of reconstructed neurons, microcircuits and brain regions as well as videos of different brain regions detailing their cellular and molecular composition and their electrical behavior.

The majority of the dataset was created by the Blue Brain Project and its collaborators during the last 18 years and is supplemented by publicly available data integrated within the same framework to ensure comprehensiveness.

# General Usage

The data can be leveraged by the computational and simulation neuroscience community to accelerate fundamental and translational neuroscience research. Some of the applications
include, but are not limited to:
* Train machine learning models to classify neurons based on their morphologies and electrophysiologies.
* Extract electrical-features that can be used to optimize single neuronal models.
* Build single, paired, and clustered neuron models.
* Build morphologically constrained electrical neuron models.
* Reverse engineer cell type densities and distributions from brain images.
* Run simulation experiments using different circuit models.
* Analyze and explore the connectivity within different brain regions.
* Use existing or develop new tools to analyze and validate brain circuit models.
* Run neuro-glia-vasculature simulations for studying the brain’s metabolic system.

# Directory Structure

1. Experimental_Data
* Reconstructed_morphologies
  * Categorized
    * Neurons
      * Mouse
        * Cortex
        * Hippocampus
        * Thalamus
      * Rat
        * Cortex
        * Hippocampus
        * Thalamus
    * Astrocytes
      * Mouse
        * Cortex
      * Rat
        * Cortex
        * Hippocampus
    * Microglia
      * Mouse
        * Cortex
        * Hippocampus
  * Uncategorized
* Electrophysiological_recordings
  * Single-cell_recordings
    * SSCx
    * Thalamus
    * Amygdala
    * Hippocampus
    * Others
  * Paired_Recordings
    * SSCx
    * Thalamus
    * Amygdala
    * Hippocampus
    * Others
  * Ion_channels
    * Kv
    * Nav
    * HCN
    * Kir
    * K2P
    * Cav
    * KCa
* Brain_Images
  * Image_Stack
  * Terafly
* Bouton_density
* Neuron_density
* Neuron_composition
* Optical_microscopy_reconstructions
* Transcriptomics
  * Neocortex
  * Whole_brain
* Literature_curated_data

2. Model_Data
* Morphological_models
  * SSCx
  * Thalamus
  * Amygdala
  * Hippocampus
  * Others
* Electrophysiological_models
  * SSCx
  * Thalamus
  * Amygdala
  * Hippocampus
  * Others
* Morpho-Electrical_models
  * SSCx
  * Thalamus
  * Amygdala
  * Hippocampus
  * Others
* Synapse_models
  * SSCx
  * Thalamus
  * Amygdala
  * Hippocampus
  * Others
* Ion_Channel_models
  * SSCx
  * Thalamus
  * Amygdala
  * Hippocampus
  * Others
* Circuits
  * Circuits_analysis
    * Electrical_models
      * SSCx
      * Thalamus
      * Amygdala
      * Hippocampus
      * Others
    * Electrical_model_analysis
      * SSCx
      * Thalamus
      * Amygdala
      * Hippocampus
      * Others
    * Electrical_model_validation
      * SSCx
      * Thalamus
      * Amygdala
      * Hippocampus
      * Others
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
* Brain_atlas
  * Annotation_volume
  * Parcellation_ontology
  * Brain_template
  * Cell_orientation_field
  * Direction_vector
  * Hemisphere_volume
  * Placement_hints
  * Cell_composition
    * Morphological-electrical_neuron_type_Densities
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
  * Thalamus
  * Amygdala
  * Hippocampus
  * Others
* Experiment_Simulation
  * SSCx
  * Thalamus
  * Amygdala
  * Hippocampus
  * Others

 4. Images_Videos
* Brain_Systems
  * Whole_Brain
  * Multiple_Brain_Areas
* Brain_Regions
  * Hippocampus
  * Neocortex
  * Thalamus
  * Multiple_Brain_Regions
  * Somatosensory_Cortex
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

