'''
Author: Jing Zhang
Date: 2021-01-27
Function:
cropping cardiac targets to (100,100),
the bounding box is obtained from ground truth images.
'''
## using simpleITK to load and save data.
import SimpleITK as sitk
import glob, os
import numpy as np
import cv2
def Info(images_path):
    imagelist = sorted(glob.glob(os.path.join(images_path, '*.nii.gz')))  # sorted按名称排序,glob.glob 匹配,os.path.join字符串拼接
    for i in (range(len(imagelist))):
        itk_img = sitk.ReadImage(imagelist[i])
        img = sitk.GetArrayFromImage(itk_img)
        print(imagelist[i][20:])
        print(img.shape)
path ='ACDC_3D_cardiac_target/img/'
#Info(path)


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

    min_x1 = 120
    min_y1 = 120
    max_x2 = 80
    max_y2 = 80
    max_width = 20
    max_height = 20
    for k in range(0, img.shape[0]):  # for each slice
        x, y, w, h = boundingbox(img[k])
        max_xw = x + w
        max_yh = y + h
        if (x < min_x1 and x != 0): min_x1 = x
        if (y < min_y1 and y != 0): min_y1 = y
        if (max_xw > max_x2): max_x2 = max_xw
        if (max_yh > max_y2): max_y2 = max_yh
        if (w > max_width): max_width = w
        if (h > max_height): max_height = h
    print('the biggest boundingbox:', min_x1, min_y1, max_x2, max_y2)
    # print('the biggest boundingbox:', max_width,max_height)

    return min_x1, min_y1, max_x2, max_y2


def cropping_target(images_path,i):
    min_x1, min_y1, max_x2, max_y2 = Findboundingbox(src_gt,i)# the boundingbox of ground truth
    width = 100
    height = 100
    new_x1 = int(min_x1-(width-(max_x2-min_x1))/2)
    new_y1 = int(min_y1-(height-(max_y2-min_y1))/2)
    new_x2 = int(max_x2+(width-(max_x2-min_x1))/2)
    new_y2 = int(max_y2+(height-(max_y2-min_y1))/2)
    print(new_x1,new_y1,new_x2,new_y2)
    imagelist = sorted(glob.glob(os.path.join(images_path, '*.nii.gz')))
    print(imagelist[i])
    itk_img = sitk.ReadImage(imagelist[i])
    img = sitk.GetArrayFromImage(itk_img)

    cropped_patch = np.zeros(((len(img), height, width)))#(slice,183,147)

    print("The shape of cropped image: ",cropped_patch.shape)

    for k in range(0,img.shape[0]):# for each slice
        #print(img[k].shape)
        cropped_patch[k] = img[k][new_y1:new_y2, new_x1:new_x2]
        cv2.imshow('bb', cropped_patch[k].astype('uint8') * 255)
        #cv2.waitKey(0)
    img = sitk.GetImageFromArray(cropped_patch)
    sitk.WriteImage(img, imagelist[i])
src_gt = 'ACDC_3D_cardiac_target/gt/'
src_img = 'ACDC_3D_cardiac_target/img/'
n=0
# while(n<200):
#     print("*****The patient number: *****", n)
#     cropping_target(src_img, n)
#     n=n+1
