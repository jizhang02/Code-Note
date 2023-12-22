'''
-----------------------------------------------
File Name: plots_curvefromcsv.py
Description: Drawing learning curve in training,
validation, test stage from log file.
Author: Jing (zhangjingnm@hotmail.com)
Date: 7/5/2021
-----------------------------------------------
'''

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def MaxMinNormalization(x):
    Max = np.max(x)
    Min = np.min(x)
    x = (x - Min) / (Max - Min)
    return x
def Learningcurve_3loss():
    path0 = "7977719/unet-hc18/logs/log5.csv"
    path1 = "7980741/unet-hc18/logs/log5.csv"
    path2 = "7977821/unet-hc18/logs/log5.csv"

    data0 = pd.read_csv(path0)
    data1 = pd.read_csv(path1)
    data2 = pd.read_csv(path2)

    xdata0 = data0.loc[:, 'epoch']
    ydata0 = data0.loc[:, 'IOU']
    ydata1 = data1.loc[:, 'IOU']
    ydata2 = data2.loc[:, 'IOU']
    ydata0 = MaxMinNormalization(ydata0)
    ydata1 = MaxMinNormalization(ydata1)
    ydata2 = MaxMinNormalization(ydata2)
    plt.figure(1)
    plt.title('Learning curve')
    plt.plot(xdata0, ydata0, color='green', label='Kappa+Focal')
    plt.plot(xdata0, ydata1, color='blue', label='Kappa loss')
    plt.plot(xdata0, ydata2, color='purple', label='Dice loss')
    plt.legend()
    plt.xlabel('Epochs')
    plt.ylabel('Value')
    plt.tight_layout()
    plt.savefig(os.path.join(save_fig_dir, save_fig_filename), dpi=200, orientation='landscape', format='pdf')
    plt.show()

def Learningcurve_train_valid():
    path0 = "log-5.csv"
    data0 = pd.read_csv(path0)
    xdata0 = data0.loc[:, 'epoch']
    ydata0 = data0.loc[:, 'mean_absolute_error']
    ydata1 = data0.loc[:,'val_mean_absolute_error']
    ydata2 = data0.loc[:,'loss']
    ydata3 = data0.loc[:,'val_loss']
    #ydata0 = MaxMinNormalization(ydata0)
    #ydata1 = MaxMinNormalization(ydata1)
    #ydata2 = MaxMinNormalization(ydata2)
    #ydata3 = MaxMinNormalization(ydata3)

    plt.figure(1)
    plt.title('Learning curve')
    plt.plot(xdata0, ydata0, color='green', label='tra_MAE')
    plt.plot(xdata0, ydata1, color='red', label='val_MAE')
    plt.plot(xdata0, ydata2, color='blue', label='tra_loss')
    plt.plot(xdata0, ydata3, color='purple', label='val_loss')

    plt.legend()
    plt.xlabel('Epochs')
    plt.ylabel('Value')
    plt.tight_layout()
    #plt.savefig(os.path.join(save_fig_dir, save_fig_filename), dpi=200, orientation='landscape', format='pdf')
    plt.show()
#save_fig_dir = os.path.join(os.getcwd(), 'figures')
#save_fig_filename = 'learningcurve_PD.pdf'
#Learningcurve_3loss()
Learningcurve_train_valid()