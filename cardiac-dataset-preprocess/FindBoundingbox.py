'''
Author: Jing Zhang
Date: 2021-01-14
Function:
1.Find boundingbox of each patient according to ground truth.
2.Find the largest boundingbox of each slice.
3.Crop the image according to the current largest boundingbox.
4.Do the same operation to 200 patients.
5.Then make borders of each cropped patients.
'''
## using simpleITK to load and save data.
import SimpleITK as sitk
import glob, os
import numpy as np
import cv2
def Info(images_path):
    imagelist = sorted(glob.glob(os.path.join(images_path, '*.nii.gz')))  # sorted按名称排序,glob.glob 匹配,os.path.join字符串拼接
    for i in (range(len(imagelist))):
        #print(imagelist[i][11:])
        itk_img = sitk.ReadImage(imagelist[i])
        img = sitk.GetArrayFromImage(itk_img)
        #print('original:', img.shape)
        print(img.shape)
path ='ACDC_3D_FindBoundbox/img_cropped/'
Info(path)


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

def Findboundingbox(images_path,i):
    imagelist = sorted(glob.glob(os.path.join(images_path, '*.nii.gz')))
    print(imagelist[i])
    itk_img = sitk.ReadImage(imagelist[i])
    img = sitk.GetArrayFromImage(itk_img)
    min_x1 = 100
    min_y1 = 100
    max_x2 = 100
    max_y2 = 100
    max_width = 20
    max_height = 20
    for k in range(0,img.shape[0]):# for each slice
        x, y, w, h = boundingbox(img[k])
        max_xw = x + w
        max_yh = y + h
        if (x < min_x1 and x != 0): min_x1 = x
        if (y < min_y1 and y != 0): min_y1 = y
        if (max_xw > max_x2): max_x2 = max_xw
        if (max_yh > max_y2): max_y2 = max_yh
        if (w>max_width):max_width = w
        if (h>max_height):max_height = h
    print('the biggest boundingbox:', min_x1, min_y1, max_x2, max_y2)
    #print('the biggest boundingbox:', max_width,max_height)
    return min_x1, min_y1, max_x2, max_y2

def CropnMakeBorder(images_path,i):
    min_x1, min_y1, max_x2, max_y2 = Findboundingbox(src_gt,i)# the boundingbox of ground truth
    imagelist = sorted(glob.glob(os.path.join(images_path, '*.nii.gz')))
    print(imagelist[i])
    itk_img = sitk.ReadImage(imagelist[i])
    img = sitk.GetArrayFromImage(itk_img)

    width = max_x2-min_x1
    height = max_y2-min_y1
    cropped_patch = np.zeros(((len(img), height, width)))#(slice,183,147)

    print("The shape of cropped image: ",cropped_patch.shape)

    for k in range(0,img.shape[0]):# for each slice
        #print(img[k].shape)
        cropped_patch[k] = img[k][min_y1:max_y2, min_x1:max_x2]
        cv2.imshow('bb', cropped_patch[k].astype('uint8') * 255)
        #cv2.waitKey(0)
    img = sitk.GetImageFromArray(cropped_patch)
    sitk.WriteImage(img, imagelist[i])
src_gt = 'ACDC_3D/gt/'
src_img = 'ACDC_3D/img/'
n=0
# while(n<200):
#     print("*****The patient number: *****", n)
#     CropnMakeBorder(src_img,n)
#     n=n+1

def MakeBorder(images_path):
    imagelist = sorted(glob.glob(os.path.join(images_path, '*.nii.gz')))  # sorted按名称排序,glob.glob 匹配,os.path.join字符串拼接
    for i in (range(len(imagelist))) :
        #print(imagelist[i])
        itk_img = sitk.ReadImage(imagelist[i])
        img = sitk.GetArrayFromImage(itk_img)
        height = 235
        width = 167
        patch = np.zeros(((len(img), height, width)))  # (slice,183,147)

        for k in range(0,img.shape[0]):# for each slice
            print(img[k].shape)
            if img[k].shape[1]<width or img[k].shape[0]<height:
                patch[k] = cv2.copyMakeBorder(img[k], 0,
                np.abs(height-img[k].shape[0]), 0, np.abs(width-img[k].shape[1]) , cv2.BORDER_CONSTANT,
                                                 value=(0, 0, 0))  # top, bottom, left, right,
            print(patch.shape)
            cv2.imshow('bb', patch[k].astype('uint8') * 255)
            #cv2.waitKey(0)
        img = sitk.GetImageFromArray(patch)
        sitk.WriteImage(img, imagelist[i])

src = 'ACDC_3D/img_cropped/'
#MakeBorder(src)
