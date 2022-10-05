# DeepRestClassification-Proboscis_labelling
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Version](https://badge.fury.io/gh/tterb%2FHyde.svg)](https://badge.fury.io/gh/tterb%2FHyde)

This repository is part of the analysis pipeline of https://github.com/NeLy-EPFL/Ascending_neuron_screen_analysis_pipeline/ for the manuscripts [**Ascending neurons convey behavioral state to integrative sensory and action selection centers in the brain**] in bioRxiv (https://www.biorxiv.org/content/10.1101/2022.02.09.479566v1), which focuses on isolating the proboscis extension event from videographies. The behaviroal classification is based on the post estimation from DeepLabCut (DLC) module and optimized by additional denoisng, waveform analysis, binarization to isolate the event periods of interest.

## Content
- [Installation](#installation)
- [Steps of the classification pipeline]((#Steps-of-the-classification-pipeline))
  - [Overview]((#overview))
  - [Steps]((#Steps))
  - [Raw predictions vs. Denoised predictions]((#Raw-DLC-predictions-vs.-Denoised-predictions))



## Installation
To install the AN environment for Python scripts and DeepLabCut of CPU version, please refer to https://github.com/NeLy-EPFL/Ascending_neuron_screen_analysis_pipeline/



## Steps of the classification pipeline

### Overview
1. A DLC model is trained to label the landmark of both ends of proboscis.
2. The script is created to predict the proboscis landmark through the video.
3. The length between two ends of proboscis is calculated and preprocessed.
4. The extension event is classified through a series of derivation, onset and end timing determnation, condition fitering to remove false positive detection, and finally binarize the period to indicate the epochs of the targeted behavior.
<p align="left">
  <img align="center" width="780" src="/images/Diagram.png">
</p>


### Steps

1. [Optional] Generate the video from videoframes:
If there are only image frames, convert them into a video which is the input for DeepLabCut.

  Prerequisite: ffmpeg (https://ffmpeg.org/download.html)
```bash
python 0-make_video_for_single_camera.py
```


2. Predict landmarks in the video using DeepLabCur trained model:
```bash
source activate DLC-CPU
python 1-Predict_dlc_batch_with_existing_model.py
```
```bash
conda deactivate
```

![Alt text](./images/dlc_pred.gif?raw=true "dlc_pred")


3. Denoise the trace of the length, detect the extension period, binarize into behavioral epcohs:
```bash
source activate AN
python 2-quantify_extensionLength_filter_binEvent.py
```

<p align="left">
  <img align="center" width="780" src="/outputs/PE_classification_results/PER_event.png">
</p>

Finally, the proboscis extension length is calculated and the events are detected (top). The event period are converted into a binary trace (bottom). The intermediate step of derivatation is shown in the middle to illusrate the peak detection (green dot) and onset time searching (blue arrowhead). The event end timing of the event is also found in the raw trace as indicated (top; red arrowhead).




### Raw DLC predictions vs. Denoised DLC predictions




The raw prediction is not perfect and still has noisy trace due to jumping predictions.
This filter examination shows that the stability of prediction can be improved by the posthoc denoising on the trace. Denosied predictions are projected back to the video.

The median filter (top-right) was chosen for the following event detection because it not only removes most of the noise but also preserves the waveform pattern. The Savitsky-Golay filter (bottom left) was not used because it causes skewed waveform which leads to significant time shift of event onset in the following steps of event detection. 


[Optional] Check the effect of filter on the raw traces by visualizing them in the video:
```bash
python 3-Make_filtered_coordinates_movie.py
```

![Alt text](./images/Raw_vs_Filtered.gif?raw=true "Raw_vs_Filtered")



