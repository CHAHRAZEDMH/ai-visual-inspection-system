# AI Visual Inspection System 

Industrial anomaly detection using PatchCore and the MVTec AD dataset.

## Project Overview

This project implements an industrial visual inspection pipeline for anomaly detection using:

- PyTorch
- Anomalib
- PatchCore
- MVTec AD Dataset

The objective is to automatically detect defects on industrial products without requiring defect samples during training.

## Dataset

Dataset used:
- MVTec Anomaly Detection Dataset

Categories tested:
- Capsule
- Bottle
- Cable
- Grid
- Leather
- Hazelnut
- etc.

## Results

PatchCore achieved:

| Metric | Score |
|----------|----------|
| Image AUROC | 0.9916 |
| Image F1-Score | 0.9813 |
| Pixel AUROC | 0.9899 |
| Pixel F1-Score | 0.5152 |

## Technologies

- Python
- PyTorch
- Anomalib
- OpenCV
- Jupyter Notebook

## Author
Chahrazed MAHDHI 








Chahrazed Mahdhi
PhD Student in Artificial Intelligence and Medical Imaging
