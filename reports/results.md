# PatchCore Results - MVTec AD Capsule

## Model
PatchCore anomaly detection model using Anomalib.

## Dataset
MVTec AD - Capsule category.

## Results

| Metric | Score |
|---|---:|
| image_AUROC | 0.9916 |
| image_F1Score | 0.9813 |
| pixel_AUROC | 0.9900 |
| pixel_F1Score | 0.5152 |

## Interpretation

The model performs very well at image-level anomaly detection and global pixel-level localization.  
The lower pixel F1-score suggests that precise defect segmentation can still be improved.