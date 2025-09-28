# 🌍 HSACNet: Hierarchical Scale-Aware Consistency Regularized Semi-Supervised Change Detection


The code is coming soon.


---

## 🔍 Abstract

Semi-supervised change detection (SSCD) aims to detect changes between bi-temporal remote sensing images by utilizing limited labeled data and abundant unlabeled data. Existing methods struggle in complex scenarios, exhibiting poor performance when confronted with noisy data. They typically neglect intra-layer multi-scale features while emphasizing inter-layer fusion, harming the integrity of change objects with different scales. In this paper, we propose HSACNet, a Hierarchical Scale-Aware Consistency regularized Network for SSCD. Specifically, we integrate Segment Anything Model 2 (SAM2), using its Hiera backbone as the encoder to extract inter-layer multi-scale features and applying adapters for parameter-efficient fine-tuning. Moreover, we design a Scale-Aware Differential Attention Module (SADAM) that can precisely capture intra-layer multi-scale change features and suppress noise. Additionally, a dual-augmentation consistency regularization strategy is adopted to effectively utilize the unlabeled data. Extensive experiments across four CD benchmarks demonstrate that our HSACNet achieves state-of-the-art performance, with reduced parameters and computational cost.

---

## 📊 Results

### 1. Quantitative Results on WHU-CD and LEVIR-CD

The two numbers in each cell denote the **changed-class IoU** and **overall accuracy (OA)**, respectively.  
Results are reported under semi-supervised settings with varying labeled ratios: **5%, 10%, 20%, 40%**.  
**Bold values indicate state-of-the-art performance**.

#### 🔹 WHU-CD

| Method       | 5%             | 10%            | 20%            | 40%            |
|--------------|----------------|----------------|----------------|----------------|
| AdvEnt       | 57.7 / 97.87   | 60.5 / 97.79   | 69.5 / 98.50   | 76.0 / 98.91   |
| s4GAN        | 57.3 / 97.94   | 58.0 / 97.81   | 67.0 / 98.41   | 74.3 / 98.85   |
| SemiCDNet    | 56.2 / 97.78   | 60.3 / 98.02   | 69.1 / 98.47   | 70.5 / 98.59   |
| SemiCD       | 65.8 / 98.37   | 68.0 / 98.45   | 74.6 / 98.83   | 78.0 / 99.01   |
| RC-CD        | 58.0 / 98.01   | 61.7 / 98.00   | 74.0 / 98.83   | 73.9 / 98.85   |
| SemiPTCD     | 74.1 / 98.85   | 74.2 / 98.86   | 76.9 / 98.95   | 80.8 / 99.17   |
| UniMatch     | 78.7 / 99.11   | 79.6 / 99.11   | 81.2 / 99.18   | 83.7 / 99.29   |
| CBFF         | 79.0 / 99.11   | 80.5 / 99.15   | 82.0 / 99.23   | 82.5 / 99.26   |
| Sup-only     | 56.4 / 97.90   | 66.1 / 98.38   | 74.4 / 98.82   | 84.3 / 99.34   |
| **Ours**     | **81.7 / 99.23** | **81.3 / 99.20** | **84.9 / 99.35** | **86.3 / 99.42** |
| Sup-fully    | \multicolumn{4}{c}{IoU = 89.5, OA = 99.27} |

#### 🔹 LEVIR-CD

| Method       | 5%             | 10%            | 20%            | 40%            |
|--------------|----------------|----------------|----------------|----------------|
| AdvEnt       | 67.1 / 98.15   | 70.8 / 98.38   | 74.3 / 98.59   | 75.9 / 98.67   |
| s4GAN        | 66.6 / 98.16   | 72.2 / 98.48   | 75.1 / 98.63   | 76.2 / 98.68   |
| SemiCDNet    | 67.4 / 98.11   | 71.5 / 98.42   | 74.9 / 98.58   | 75.5 / 98.63   |
| SemiCD       | 74.2 / 98.59   | 77.1 / 98.74   | 77.9 / 98.79   | 79.0 / 98.84   |
| RC-CD        | 74.0 / 98.52   | 76.1 / 98.65   | 77.1 / 98.70   | 77.6 / 98.72   |
| SemiPTCD     | 71.2 / 98.39   | 75.9 / 98.65   | 76.6 / 98.65   | 77.2 / 98.74   |
| UniMatch     | 82.1 / 99.03   | 82.8 / 99.07   | 82.9 / 99.07   | 83.0 / 99.08   |
| CBFF         | 82.1 / 99.03   | 82.8 / 99.06   | **83.2 / 99.09** | 83.3 / 99.08   |
| Sup-only     | 72.0 / 98.38   | 77.1 / 98.72   | 81.1 / 98.96   | 82.2 / 99.03   |
| **Ours**     | **82.2 / 99.03** | **83.1 / 99.07** | **83.2 / 99.08** | **83.5 / 99.10** |
| Sup-fully    |                     {IoU = 83.8, OA = 99.11}                      |

---

### 2. Quantitative Results on GZ-CD and EGY-BCD

The two numbers in each cell denote the **changed-class IoU** and **overall accuracy (OA)**, respectively.  
Results are reported under semi-supervised settings with varying labeled ratios: **5%, 10%, 20%, 40%**.  
**Bold values indicate state-of-the-art performance**.

#### 🔹 GZ-CD

| Method       | 5%             | 10%            | 20%            | 40%            |
|--------------|----------------|----------------|----------------|----------------|
| AdvEnt       | 56.7 / 95.52   | 57.5 / 95.99   | 70.3 / 97.28   | 70.8 / 97.29   |
| s4GAN        | 59.4 / 96.13   | 61.6 / 96.23   | 68.5 / 97.10   | 69.4 / 97.08   |
| SemiCDNet    | 57.9 / 95.38   | 54.9 / 95.52   | 68.9 / 97.16   | 69.7 / 97.20   |
| SemiCD       | 59.5 / 96.27   | 58.6 / 96.03   | 67.0 / 97.03   | 71.5 / 97.36   |
| RC-CD        | 62.2 / 96.26   | 63.9 / 96.55   | 74.1 / 97.69   | 74.2 / 97.57   |
| UniMatch     | 68.7 / 97.06   | 69.5 / 97.41   | 72.8 / 97.71   | 71.1 / 97.48   |
| CBFF         | 67.4 / 97.05   | 69.3 / 97.24   | 72.0 / 97.62   | 76.4 / 97.99   |
| Sup-only     | 64.8 / 96.51   | 64.2 / 96.75   | 69.8 / 97.23   | 78.2 / 98.08   |
| **Ours**     | **72.5 / 97.44** | **73.1 / 97.64** | **80.1 / 98.27** | **81.4 / 98.40** |
| Sup-fully    |                      IoU = 83.3, OA = 98.54                       |

#### 🔹 EGY-BCD

| Method       | 5%             | 10%            | 20%            | 40%            |
|--------------|----------------|----------------|----------------|----------------|
| AdvEnt       | 52.0 / 95.30   | 58.1 / 96.26   | 59.8 / 96.46   | 63.8 / 96.94   |
| s4GAN        | 53.2 / 95.62   | 56.5 / 96.26   | 59.4 / 96.62   | 64.1 / 96.83   |
| SemiCDNet    | 52.7 / 95.36   | 56.9 / 96.02   | 59.8 / 96.53   | 63.6 / 96.96   |
| SemiCD       | 54.3 / 95.79   | 59.2 / 96.29   | 61.8 / 96.61   | 65.4 / 96.96   |
| RC-CD        | 59.0 / 96.17   | 61.6 / 96.51   | 64.6 / 96.79   | 67.7 / 97.09   |
| UniMatch     | 62.8 / 96.74   | 65.5 / 97.10   | 63.6 / 96.91   | 67.3 / 97.26   |
| CBFF         | 63.7 / 96.64   | 64.3 / 96.95   | 63.8 / 96.95   | 67.7 / 97.21   |
| Sup-only     | 58.2 / 96.05   | 59.6 / 96.26   | 65.0 / 96.95   | 69.1 / 97.35   |
| **Ours**     | **68.5 / 97.25** | **68.1 / 97.28** | **69.6 / 97.43** | **70.6 / 97.50** |
| Sup-fully    |                         IoU = 71.7, OA = 97.62                    |


