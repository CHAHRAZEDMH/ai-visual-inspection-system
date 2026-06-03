# AI Visual Inspection System

Industrial anomaly detection using PatchCore and the MVTec AD dataset.

## Project Overview

This project implements an industrial visual inspection pipeline for anomaly detection using:

* PyTorch
* Anomalib
* PatchCore
* OpenCV
* MVTec AD Dataset

The objective is to automatically detect defects on industrial products without requiring defect samples during training.

## Dataset

Dataset used:

* MVTec Anomaly Detection Dataset

Categories available:

* Bottle
* Cable
* Capsule
* Carpet
* Grid
* Hazelnut
* Leather
* Metal Nut
* Pill
* Screw
* Tile
* Toothbrush
* Transistor
* Wood
* Zipper

## Method

PatchCore is an anomaly detection algorithm based on:

1. Feature extraction using a pretrained CNN.
2. Memory bank construction from normal images.
3. Nearest-neighbor anomaly scoring.
4. Anomaly localization through heatmaps.

## Results

Example results obtained on the Capsule category:

| Metric         | Score  |
| -------------- | ------ |
| Image AUROC    | 0.9916 |
| Image F1-Score | 0.9813 |
| Pixel AUROC    | 0.9899 |
| Pixel F1-Score | 0.5152 |

## Technologies

* Python
* PyTorch
* Anomalib
* OpenCV
* Jupyter Notebook
* Git
* GitHub

## Project Structure

ai-visual-inspection-system/

├── notebooks/

├── source/

├── rapports/

├── requirements.txt

├── .gitignore

└── README.md

## Author

Chahrazed Mahdhi

 Deep Learning and Medical Imaging.
