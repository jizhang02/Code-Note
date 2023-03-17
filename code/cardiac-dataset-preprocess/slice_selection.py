'''
Date: 2021-04-22
Author: Jing Zhang
E-Mail: jing.zhang@insa-rouen.fr
Function:
Selecting 3 slices from each patient which has 9 slices
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

def SliceSelection(images_path):
    imagelist = sorted(glob.glob(os.path.join(images_path, '*.nii.gz')))  # sorted按名称排序,glob.glob 匹配,os.path.join字符串拼接
    for i in tqdm(range(len(imagelist))):
        itk_img = sitk.ReadImage(imagelist[i])
        img = sitk.GetArrayFromImage(itk_img)
        #print('original:',img.shape)
        compound_patch = []
        for k in range(0, img.shape[0]):  # for each slice
            if k==4 or k==5 or k==6:
                compound_patch.append(img[k])
        compound_patch = np.array(compound_patch)# convert list to array
        #print('the shape after slice selection:',compound_patch.shape)

        img = sitk.GetImageFromArray(np.array(compound_patch))
        sitk.WriteImage(img, imagelist[i])

src = 'ACDC_3D_multi_slice/dataset456/img_ori/'
SliceSelection(src)
#Info('ACDC_3D_cropedsliced/gt/')