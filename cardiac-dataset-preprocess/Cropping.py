'''
Title: cropping the cardiac area from images.
If the largest boundingbox is larger than certain image, make the border.
Author: Jing Zhang
Date: 2021-04-23
'''
## using simpleITK to load and save data.
import SimpleITK as sitk
import glob, os
from tqdm import tqdm
import numpy as np
import cv2
from matplotlib import pyplot as plt

area1 = 0
area2 = 0
area3 = 0
def boundingbox(src):
    #src = cv2.imread(src)
    #contours = cv2.findContours(src, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = cv2.Canny(src,0,1)
    x, y, w, h = cv2.boundingRect(contours)

    #print(x,y,w,h)
    cv2.rectangle(src, (x, y), (x + w, y + h), (100,10,200), 1, 8, 0)
    cv2.imshow('bb',src)
    #cv2.waitKey(0)
    return x,y,w,h

def Findboundingbox(images_path):
    imagelist = sorted(glob.glob(os.path.join(images_path, '*.nii.gz')))  # sorted按名称排序,glob.glob 匹配,os.path.join字符串拼接
    for i in tqdm(range(len(imagelist))) :
        #print(imagelist[i])
        itk_img = sitk.ReadImage(imagelist[i])
        img = sitk.GetArrayFromImage(itk_img)
        #print(img.shape)
        #print((img.shape[0]))
        # calculating areas
        min_x1 = 100
        min_y1 = 100
        max_x2 = 100
        max_y2 = 100
        for k in range(0,img.shape[0]):# for each slice
           x, y, w, h = boundingbox(img[k])
           max_xw = x + w
           max_yh = y + h
           if (x < min_x1 and x != 0): min_x1 = x
           if (y < min_y1 and y != 0): min_y1 = y
           if (max_xw > max_x2): max_x2 = max_xw
           if (max_yh > max_y2): max_y2 = max_yh
       # print('the biggest boundingbox:', min_x1, min_y1, max_x2, max_y2)
        print(min_x1, min_y1, max_x2, max_y2)

        #print(area3)
        # # calculating areas
        # for k in range(0,img.shape[0]):# for each slice
        #     area1 += (img[k]== 1).sum()#RV
        #     area2 += (img[k]==2).sum()#MYO
        #     area3 += (img[k]==3).sum()#LV
        # #print(area3)

def CropnMakeBorder(images_path):
    imagelist = sorted(glob.glob(os.path.join(images_path, '*.nii.gz')))  # sorted按名称排序,glob.glob 匹配,os.path.join字符串拼接
    for i in tqdm(range(len(imagelist))) :
        #print(imagelist[i])
        itk_img = sitk.ReadImage(imagelist[i])
        img = sitk.GetArrayFromImage(itk_img)
        #print(img.shape)
        #print((img.shape[0]))
        # calculating areas
        min_x1 = 28
        min_y1 = 21
        max_x2 = 175
        max_y2 = 207
        #print('shape is',len(img))#10
        width = max_x2-min_x1
        height = max_y2-min_y1
        cropped_patch = np.zeros(((len(img), height, width)))#(slice,183,147)

        print(cropped_patch.shape)

        for k in range(0,img.shape[0]):# for each slice
            print(img[k].shape)
            print(img[k].shape[1])
            if img[k].shape[1]<max_x2 or img[k].shape[0]<max_y2:#
                print('need to make border.')
                patch = cv2.copyMakeBorder(img[k], 0, np.abs(max_y2-img[k].shape[0]), 0, np.abs(max_x2-img[k].shape[1]) , cv2.BORDER_REPLICATE,
                                                 value=(0, 0, 0))  # top, bottom, left, right,
                cropped_patch[k] = patch[min_y1:max_y2, min_x1:max_x2]
            else:
                cropped_patch[k] = img[k][min_y1:max_y2, min_x1:max_x2]
            cv2.imshow('bb', cropped_patch[k].astype('uint8') * 255)
            cv2.waitKey(0)
        #img = sitk.GetImageFromArray(cropped_patch)
        #sitk.WriteImage(img, imagelist[i])

src = 'ACDC_3D/gt/'
#new = 'ACDC_3D/cropped/'
#CropnMakeBorder(src)
Findboundingbox(src)
