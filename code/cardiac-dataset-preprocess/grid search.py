'''
-----------------------------------------------
File Name: grid search$
Description:
Author: Jing$
Date: 8/23/2021$
-----------------------------------------------
'''

import copy
import numpy as np
from imgaug import augmenters as iaa
from PIL import Image,ImageChops
import SimpleITK as sitk ## using simpleITK to load and save data.
import glob, os
from tqdm import tqdm
import numpy as np
import cv2
from matplotlib import pyplot as plt

class Solution(object):
    result = []
    temp = []

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        del self.result[:]
        del self.temp[:]

        if nums == []:
            return self.result
        else:
            self.backtrack(nums, 0)
            return self.result

    def backtrack(self, nums, startIndex):

        length = len(nums)
        self.result.append(copy.deepcopy(self.temp))  # 收集所有节点
        if startIndex >= length:
            return

        for i in range(startIndex, length):  # startIndex决定遍历宽度，有序
            self.temp.append(nums[i])
            self.backtrack(nums, i + 1)  # i决定遍历深度，i+1表示无重复
            self.temp = self.temp[:-1]

def aug_rotate(image):
    angle = 10
    height, width = image.shape
    rotate_around = (width // 2, height // 2)
    M = cv2.getRotationMatrix2D(rotate_around, angle, 1)
    image = cv2.warpAffine(image, M, (width, height))
    return image
def aug_rotate_r(image):
    angle = -5
    height, width = image.shape
    rotate_around = (width // 2, height // 2)
    M = cv2.getRotationMatrix2D(rotate_around, angle, 1)
    image = cv2.warpAffine(image, M, (width, height))
    return image
def aug_trans_x(image):
    shiftX = 5
    shiftY = 0
    M = np.float32([ [1, 0, shiftX], [0, 1, shiftY] ])
    height, width = image.shape
    image = cv2.warpAffine(image, M, (width, height))
    return image
def aug_trans_y(image):
    shiftX = 0
    shiftY = 5
    M = np.float32([ [1, 0, shiftX], [0, 1, shiftY] ])
    height, width = image.shape
    image = cv2.warpAffine(image, M, (width, height))
    return image
def aug_flip_h(image):
    image = cv2.flip(image, 1)  # 1 for Horizontal,0 for vertical
    return image
def aug_flip_v(image):
    image = cv2.flip(image, 0)  # 1 for Horizontal,0 for vertical
    return image
def aug_shear_x(image):
    shearX = 0.1
    shearY = 0
    shearM = np.array([
        [1, shearX, 0],# x direction rate is tan =0.1
        [shearY, 1, 0]
    ])
    height, width = image.shape
    img_shear = cv2.warpAffine(image, shearM,(width, height))
    return img_shear
def aug_shear_y(image):
    shearX = 0
    shearY = 0.1
    shearM = np.array([
        [1, shearX, 0],# x direction rate is tan =0.3
        [shearY, 1, 0]
    ])
    height, width = image.shape
    img_shear = cv2.warpAffine(image, shearM,(width, height))
    return img_shear
def aug_gauss(image):
    blur = cv2.GaussianBlur(image, (3,3), 0)#kernel size, sigma, bigger, blurer
    return blur
def aug_gamma_correct(image):
    g = 1.5
    out = np.power(image / float(np.max(image)), 1 / g)# gamma bigger, brighter
    out = out*255.0
    out = out.astype(np.uint8)
    return out

#image = cv2.imread('./example/p001_fm01.png')
# example
#image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# imager = aug_gamma_correct(image)
# cv2.imshow('result',imager)
# cv2.waitKey()

func_list=['aug_rotate','aug_rotate_r','aug_flip_h','aug_flip_v','aug_trans_x','aug_trans_y',
           'aug_shear_x','aug_shear_y','aug_gauss','aug_gamma_correct']
func_index=[0,1,2,3,4,5,6,7,8,9]

solu = Solution()
aug_array = sorted(solu.subsets(func_index),key=len)

# test
print(aug_array[:29]) # subsets
print(len(aug_array[:29])) # the length of selected subsets
img_path = 'ACDC_3D_multi_slice/dataset1/gt_ori'
save_path = 'ACDC_3D_multi_slice/dataset1/gt_ori/aug/'

def grid_aug_image():
    for i in range(1,len(aug_array[:29])):
        if len(aug_array[i])==1: # 0 1 2 3 4 5 6 7 8 9
            print(aug_array[i][0])
            imagelist = sorted(glob.glob(os.path.join(img_path, '*.png')))  # sorted as name
            for m in range(len(imagelist)):
                print(imagelist[m])
                image = cv2.imread(imagelist[m])
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                image_aug = globals()[func_list[aug_array[i][0]]](image)
                cv2.imshow('result',image_aug)
                path = save_path+str(aug_array[i][0])+'/'
                if not os.path.exists(path): os.makedirs(path)
                # name way: path+imagename+_subsetname+imagesuffix
                cv2.imwrite(path + imagelist[m][-13:-4] + '_'+str(aug_array[i][0])  + imagelist[m][-4:], image_aug)

        if len(aug_array[i]) == 2: #01 02 03 04 05 06 07 08 09 12 13 14 15 16 17 18 19 23
            print(aug_array[i])
            imagelist = sorted(glob.glob(os.path.join(img_path, '*.png')))
            for m in range(len(imagelist)):
                print(imagelist[m])
                image = cv2.imread(imagelist[m])
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                image = globals()[func_list[aug_array[i][0]]](image)
                image = globals()[func_list[aug_array[i][1]]](image)
                path = save_path+str(aug_array[i][0])+str(aug_array[i][1])+'/'
                if not os.path.exists(path): os.makedirs(path)
                cv2.imwrite(path+imagelist[m][-13:-4]+'_'+str(aug_array[i][0])+str(aug_array[i][1])+imagelist[m][-4:],image)

grid_aug_image()

def grid_aug_medimage():
    for i in range(1, len(aug_array[:29])):
        if len(aug_array[i]) == 1:
            print(aug_array[i][0])
            imagelist = sorted(glob.glob(os.path.join(img_path, '*.nii.gz')))
            for m in range(len(imagelist)):
                print(imagelist[m])
                itk_img = sitk.ReadImage(imagelist[m])
                image = sitk.GetArrayFromImage(itk_img)
                print(image.shape[0])
                for k in range(0, image.shape[0]):  # for each slice
                    image[k] = globals()[func_list[aug_array[i][0]]](image[k])

                image_aug = sitk.GetImageFromArray(image)
                path = save_path + str(aug_array[i][0]) + '/'
                if not os.path.exists(path): os.makedirs(path)
                sitk.WriteImage(image_aug, path + imagelist[m][-28:-7] + '_' + str(aug_array[i][0]) + imagelist[m][-7:])

        if len(aug_array[i]) == 2:
            print(aug_array[i])
            imagelist = sorted(glob.glob(os.path.join(img_path, '*.nii.gz')))
            for m in range(len(imagelist)):
                print(imagelist[m])
                itk_img = sitk.ReadImage(imagelist[m])
                image = sitk.GetArrayFromImage(itk_img)

                for k in range(0, image.shape[0]):  # for each slice
                    image[k] = globals()[func_list[aug_array[i][0]]](image[k])
                    image[k] = globals()[func_list[aug_array[i][1]]](image[k])

                image_aug = sitk.GetImageFromArray(image)
                path = save_path + str(aug_array[i][0]) + str(aug_array[i][1]) + '/'
                if not os.path.exists(path): os.makedirs(path)
                sitk.WriteImage(image_aug, path + imagelist[m][-28:-7] + '_' + str(aug_array[i][0]) + str(aug_array[i][1]) + imagelist[m][-7:])

#grid_aug_medimage()

def Info(images_path):
    imagelist = sorted(glob.glob(os.path.join(images_path, '*.png')))  # sorted按名称排序,glob.glob 匹配,os.path.join字符串拼接
    for i in (range(len(imagelist))):
        print(imagelist[i][-16:])

#Info('ACDC_3D_multi_slice/dataset1_aug/23')
