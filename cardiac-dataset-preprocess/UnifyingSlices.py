'''
Date: 2021-01-27
Author: Jing Zhang
E-Mail: jing.zhang@insa-rouen.fr
Function:
Making the number of slice the same in each patient
'''
## using simpleITK to load and save data.
import SimpleITK as sitk
import glob, os
from tqdm import tqdm
import numpy as np
import cv2
from matplotlib import pyplot as plt
def Info(images_path):
    imagelist = sorted(glob.glob(os.path.join(images_path, '*.nii.gz')))  # sorted按名称排序,glob.glob 匹配,os.path.join字符串拼接
    for i in tqdm(range(len(imagelist))):
        itk_img = sitk.ReadImage(imagelist[i])
        img = sitk.GetArrayFromImage(itk_img)
        print('original:', img.shape)

def SliceProcess(images_path):
    imagelist = sorted(glob.glob(os.path.join(images_path, '*.nii.gz')))  # sorted按名称排序,glob.glob 匹配,os.path.join字符串拼接
    gold_slice = 9
    # 1. remove the all black slice
    for i in tqdm(range(len(imagelist))):
        itk_img = sitk.ReadImage(imagelist[i])
        img = sitk.GetArrayFromImage(itk_img)
        print('original:',img.shape)
        novoid_patch = []
        minarea = img[4].sum()
        mindex = 0
        for k in range(0, img.shape[0]):  # for each slice
            if(img[k].sum()!=0):
                novoid_patch.append(img[k])
                # find the smallest area to make up or remove for later use
                if (img[k].sum()<minarea):
                    minarea = img[k].sum()
                    mindex = k
        novoid_patch = np.array(novoid_patch)# convert list to array
        print('after remove void slice:',novoid_patch.shape)

        # print(img.shape)
        # print((img.shape[0]))
        while (np.array(novoid_patch).shape[0] < gold_slice):
            novoid_patch = np.array(novoid_patch).tolist()
            novoid_patch.append(img[mindex])
        print('after add slice:',np.array(novoid_patch).shape)
        while (np.array(novoid_patch).shape[0] > gold_slice):
            novoid_patch = np.array(novoid_patch).tolist()
            del novoid_patch[-1]
        print('after remove slice:',np.array(novoid_patch).shape)

        img = sitk.GetImageFromArray(np.array(novoid_patch))
        sitk.WriteImage(img, imagelist[i])

src = 'ACDC_3D_cardiac_target/gt/'
SliceProcess(src)
#Info('ACDC_3D_cropedsliced/gt/')