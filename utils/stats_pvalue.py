'''
-----------------------------------------------
File Name: stats_pvalue.py
Description: Calculate p value.
Author: Jing (zhangjingnm@hotmail.com)
Date: 2021-04-23
-----------------------------------------------
'''

from google.colab import drive 
drive.mount("/content/gdrive", force_remount=True)

import os
root = "/content/gdrive/My Drive/TER/"
os.chdir(root)

import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
from scipy import stats

resnet_mae_file = root + 'results/WITH_DA/RESNET50/mae.npy'
resnet_mse_file = root + 'results/WITH_DA/RESNET50/mse.npy'
resnet_hl_file = root + 'results/WITH_DA/RESNET50/hl.npy'

vgg_mae_file = root + 'results/WITH_DA/VGG16/mae.npy'
vgg_mse_file = root + 'results/WITH_DA/VGG16/mse.npy'
vgg_hl_file = root + 'results/WITH_DA/VGG16/hl.npy'

resnet_mae = np.load(resnet_mae_file)
resnet_mse = np.load(resnet_mse_file)
resnet_hl = np.load(resnet_hl_file)

vgg_mae = np.load(vgg_mae_file)
vgg_mse = np.load(vgg_mse_file)
vgg_hl = np.load(vgg_hl_file)

# visualize distrib

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.title('resnet_mae')
sns.distplot(resnet_mae)

plt.subplot(1,2,2)
sns.distplot(resnet_mse)
plt.title('resnet_mse')
plt.show()

def wilco_pvalue(a, b): 
  for e in b: 
    stat, p = stats.wilcoxon(a, b)
    print('p =', round(p,4))

m = [resnet_mae, resnet_hl, vgg_mse, vgg_mae, vgg_hl]
wilco_pvalue(resnet_mse,m)