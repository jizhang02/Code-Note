'''
-----------------------------------------------
File Name: image_seg_evaluation.py
Description: Calculate Dice score, hausdorff distance, assd
between segmented images and ground truth images.
Compute p-value between two same metrics.
Author: Jing (zhangjingnm@hotmail.com)
Date: 2021-04-23
-----------------------------------------------
'''

from PIL import Image
import os, sys
import glob
from binary import *
import numpy as np
from scipy import stats
from medpy.metric.binary import dc, hd, assd
import pandas as pd

def reading_gt(path):
    gt = []
    img_list = os.listdir(path)
    #img_list.sort(key=lambda x: int(x[3:-4]))  ##the format of image: gt_0.png
    for i in range(len(img_list)):
        img_name = path + img_list[i]
        #print(img_name)
        imlabel = Image.open(img_name).convert('L')
        imlabel = np.array(imlabel).astype(int)
        # print(np.shape(imlabel))
        if np.shape(imlabel) != (540, 800): print(img_name)
        imlabel[imlabel > 1] = 1
        gt.append(imlabel)
    return gt

def reading_seg(path):
    seg = []
    img_list = os.listdir(path)
    img_list.sort(key=lambda x: int(x[:-12]))
    for i in range(len(img_list)):
        img_name = path + img_list[i]
        #print(img_name)
        img = Image.open(img_name).convert('L')
        img = np.array(img).astype(int)
        # print(np.shape(imlabel))
        if np.shape(img) != (540, 800): print(img)
        img[img > 1] = 1
        seg.append(img)
    return seg

def Dice_score(gt0,seg0):
    DI0 = []
    DI1 = []
    for item in range(array_length):
        DI0.append(dc(gt0[item],seg0[item]))
        DI1.append(dc(gt1[item], seg1[item]))
    #print('Dice score of first group is:')
    #for i in range(array_length): print(DI0[i])
    #print('Dice score of second group is:')
    #for i in range(array_length): print(DI1[i])
    print("The mean and std dice score0 is: ", '%.2f' % np.mean(DI0), '%.2f' % np.std(DI0))
    print("The mean and std dice score1 is: ", '%.2f' % np.mean(DI1), '%.2f' % np.std(DI1))
    t_statistic, p_value = stats.ttest_rel(DI0, DI1)
    print("The p_value of two dice is: ", '%.3f' % p_value)

def HausdorffDistance_score(gt0,seg0):
    hausdorff0 = []
    hausdorff1 = []
    for item in range(array_length):
        if np.sum(seg0[item]) > 0:  # If the structure is predicted on at least one pixel
           hausdorff0.append(hd(seg0[item], gt0[item], voxelspacing=[pixelsize[item], pixelsize[item]]))
        if np.sum(seg1[item]) > 0:
           hausdorff1.append(hd(seg1[item], gt1[item], voxelspacing=[pixelsize[item], pixelsize[item]]))
    print("the length of hausdorffs:",len(hausdorff0),len(hausdorff1))
   # print('HD of first group is:')
    #for i in range(array_length): print(hausdorff0[i])
   # print('HD of second group is:')
   # for i in range(array_length): print(hausdorff1[i])
    print("The mean amd std Hausdorff Distance0 is: ", '%.2f' % np.mean(hausdorff0), '%.2f' % np.std(hausdorff0))
    print("The mean amd std Hausdorff Distance1 is: ", '%.2f' % np.mean(hausdorff1), '%.2f' % np.std(hausdorff1))
    t_statistic, p_value = stats.ttest_rel(hausdorff0, hausdorff1)
    print("The p_value of two Hausdorff is: ", '%.3f' % p_value)

def ASSD_score(gt0,seg0):
    ASSD0 = []
    ASSD1 = []
    for item in range(array_length):
        ASSD0.append(assd(seg0[item], gt0[item], voxelspacing=[pixelsize[item], pixelsize[item]]))
        ASSD1.append(assd(seg1[item], gt1[item], voxelspacing=[pixelsize[item], pixelsize[item]]))
    print("the length of assd:",len(ASSD0),len(ASSD1))
    #print('ASSD of first group is:')
    #for i in range(array_length): print(ASSD0[i])
    #print('ASSD of second group is:')
    #for i in range(array_length): print(ASSD1[i])
    print("The mean and std ASSD0 is: ", '%.2f' % np.mean(ASSD0), '%.2f' % np.std(ASSD0))
    print("The mean and std ASSD1 is: ", '%.2f' % np.mean(ASSD1), '%.2f' % np.std(ASSD1))
    t_statistic, p_value = stats.ttest_rel(ASSD0, ASSD1)
    print("The p_value of two ASSD is: ", '%.3f' % p_value)


label_path0 = "HCdata/test/gt/"
predict_path0 = "HCdata/test/cv5-linknet/"
label_path1 = "HCdata/test/gt/"
predict_path1 = "HCdata/test/cv5-psp/"
pixelsize_path = "HCdata/test/HC_ori_test.csv"
csv = pd.read_csv(pixelsize_path)
pixelsize = csv.loc[:, 'pixel size(mm)']
seg0 = reading_seg(predict_path0)
seg1 = reading_seg(predict_path1)
gt0 = reading_gt(label_path0)
gt1 = reading_gt(label_path1)
array_length = len(gt0)
print("the number of images: ",array_length)
Dice_score(gt0,seg0)
HausdorffDistance_score(gt0,seg0)
ASSD_score(gt0,seg0)