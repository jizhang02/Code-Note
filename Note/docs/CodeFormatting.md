```
""" 

Filename    : main.py 

Author      : Jing Zhang 

Date        : 2025-01-23 

Description : training script -> 3D xxx prediction 

              (specific content) using UNET or VIT. 

""" 

print(__doc__) 

# -------------------- 1. import modules -------------------- 

import torch 

import pandas as pd 

import numpy as np 

import SimpleITK as sitk 

from torch.utils.data import Dataset, DataLoader 

import torch.nn as nn 

import os, sys 

import torch.optim as optim 

from torch.utils.tensorboard import SummaryWriter 

from monai.networks.nets import UNETR, SwinUNETR, AttentionUnet, UNet, BasicUnet 

# -------------------- 2. Hyper parameters -------------------- 

data_path = 'xxx' 

batchsize = 4 

epochs = 1 

learning_rate = 1e-4 

weight_decay = 1e-2 

softplus = nn.Softplus() 

criterion = nn.SmoothL1Loss() #nn.L1Loss() # nn.SmoothL1Loss 

device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu') 

torch.manual_seed(21)  

# -------------------- 3. Class definition -------------------- 

# -------------------- 4. Main program -------------------- 

# -------------------- 5. test and evaluate -------------------- 
```