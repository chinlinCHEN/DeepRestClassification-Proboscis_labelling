# DeepRestClassification-Proboscis_labelling
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Version](https://badge.fury.io/gh/tterb%2FHyde.svg)](https://badge.fury.io/gh/tterb%2FHyde)

This repository is part of the analysis pipeline of https://github.com/NeLy-EPFL/Ascending_neuron_screen_analysis_pipeline/ for the manuscripts [**Ascending neurons convey behavioral state to integrative sensory and action selection centers in the brain**] in bioRxiv (https://www.biorxiv.org/content/10.1101/2022.02.09.479566v1), which focuses on isolating the proboscis extension event from videographies. The behaviroal classification is based on the post estimation from DeepLabCut module and optimized by additional denoisng, waveform analysis, binarization to isolate the event periods of interest.

## Content
- [Installation](#installation)
- [Steps of the classification pipeline](#reproducing-the-figures)
  - [Overview](#overview)
  - [Raw predictions vs. Denoised predictions]((#Raw-DLC-predictions-vs.-Denoised-predictions))



## Installation
To install the AN environment for Python scripts and DeepLabCut of CPU version, please refer to https://github.com/NeLy-EPFL/Ascending_neuron_screen_analysis_pipeline/



## Steps of the classification pipeline

### Overview
<p align="left">
  <img align="center" width="780" src="/images/Diagram.png">
</p>



### Raw DLC predictions vs. Denoised DLC predictions
The raw prediction is not perfect and still has noisy trace due to jumping predictions.
This filter examination show that the stability of prediction can be improved by the posthoc denoising.
Median filter were chosen for the following event detection because it still not only remove most of the noise but also preserve the waveform pattern. 

<p align="left">
  <img align="center" width="780" src="/images/Raw_vs_Filtered.gif">
</p>



