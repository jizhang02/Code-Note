'''
-----------------------------------------------
File Name: error_bar$
Description:
Author: Jing$
Date: 8/20/2021$
-----------------------------------------------
'''
import matplotlib.pyplot as plt
import numpy as np
import os

RV = [48.108, 46.283, 40.397, 40.848, 41.834, 42.492, 38.423, 42.32, 40.922, 36.655, 35.281,
      35.206, 34.751, 36.504, 34.973, 35.876, 37.911, 36.924, 35.058, 34.132, 35.754, 37.193,
      34.208, 31.583, 32.886, 33.631, 35.246, 35.907, 36.07, ]  # mae of RV
MYO = [33.888, 34.67, 31.532, 27.198, 29.206, 29.142, 29.165, 29.482, 30.907, 27.962, 28.174,
       28.825, 29.201, 30.066, 26.977, 28.441, 29.174, 29.65, 27.833, 28.586, 27.384, 28.106,
       29.431, 27.512, 29.356, 27.697, 26.145, 30.154, 27.896, ]  # mae of MYO
LV = [41.05, 44.084, 38.406, 37.603, 41.783, 37.126, 36.592, 36.807, 37.647, 34.451, 33.202,
      34.014, 30.489, 35.371, 32.097, 33.732, 35.896, 33.473, 29.666, 33.749, 32.722, 33.024,
      31.872, 30.228, 33.763, 33.455, 28.859, 34.716, 33.302, ]  # mae of LV
RV = np.array(RV)
MYO = np.array(MYO)
LV = np.array(LV)  # normalization
RV = RV / np.max(RV)
MYO = MYO / np.max(MYO)
LV = LV / np.max(LV)
error_RV = [43.971, 43.519, 40.761, 42.415, 43.677, 42.681, 46.124, 42.063, 39.499, 42.329,
            44.906, 43.378, 37.955, 43.856, 40.562, 43.119, 43.304, 41.144, 44.943, 42.489,
            42.364, 38.908, 41.983, 41.2, 39.51, 41.611, 43.739, 39.509, 41.874, ]  # error range of RV
error_MYO = [34.021, 33.526, 33.079, 29.999, 31.87, 34.231, 35.224, 33.432, 30.262, 32.492,
             30.511, 31.916, 31.817, 32.569, 32.648, 31.157, 32.9, 32.398, 31.801, 32.221,
             31.583, 30.797, 32.271, 30.406, 33.141, 32.333, 31.504, 31.618, 33.696, ]  # error range of MYO
error_LV = [38.129, 43.755, 36.769, 37.566, 39.075, 38.492, 38.736, 35.305, 34.577, 34.485,
            35.935, 35.017, 29.915, 31.965, 34.783, 33.241, 34.636, 33.928, 30.092, 34.131,
            34.016, 29.125, 31.92, 28.885, 33.813, 32.174, 27.926, 34.684, 34.274, ]  # error range of LV
error_RV = np.array(error_RV)
error_MYO = np.array(error_MYO)
error_LV = np.array(error_LV)  # normalization
error_RV = RV / np.max(error_RV)
error_MYO = MYO / np.max(error_MYO)
error_LV = LV / np.max(error_LV)
x_axis = np.linspace(0, 29, 29)  # generate 16 numers

plt.errorbar(x_axis, RV, yerr=error_RV, color='blue', fmt='o-',
             ecolor='blue', elinewidth=3, ms=4,
             mfc='blue', mec='blue', capsize=6, label='mae_RV')
plt.errorbar(x_axis, MYO, yerr=error_MYO, color='lime', fmt='o-',
             ecolor='red', elinewidth=3, ms=4,
             mfc='lime', mec='lime', capsize=6, label='mae_MYO')
plt.errorbar(x_axis, LV, yerr=error_LV, color='magenta', fmt='o-',
             ecolor='gold', elinewidth=3, ms=4,
             mfc='magenta', mec='magenta', capsize=6, label='mae_LV')
plt.legend()
plt.xlabel('Original + x* augmented data')
plt.ylabel('Prediction error')
plt.ylim((0.6, 1))
plt.xlim(0, 30)
savepath = './'
plt.savefig(os.path.join(savepath, "errorbar_plot.pdf"), dpi=200, orientation='landscape', format='pdf')

plt.show()
