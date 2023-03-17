'''
Title: Reading medical 3D images,
then save them into single slices.
Author: Jing Zhang
Date: 2021-04-23
'''

import SimpleITK as sitk
from matplotlib import pyplot as plt
def showNii(k):
    if k == 1:
        itk_img = sitk.ReadImage('training/patient100/patient100_frame01.nii.gz')#0
        img = sitk.GetArrayFromImage(itk_img)
        print(img.shape)  # (155, 240, 240) 表示各个维度的切片数量
        slices, width, height = img.shape
    if k == 2:
        itk_img = sitk.ReadImage('training/patient100/patient100_frame01_gt.nii.gz')#1
        img = sitk.GetArrayFromImage(itk_img)
        print(img.shape)  # (155, 240, 240) 表示各个维度的切片数量
        slices, width, height = img.shape
    if k == 3:
        itk_img = sitk.ReadImage('training/patient100/patient100_frame13.nii.gz')#2
        img = sitk.GetArrayFromImage(itk_img)
        print(img.shape)  # (155, 240, 240) 表示各个维度的切片数量
        slices, width, height = img.shape
    if k == 4:
        itk_img = sitk.ReadImage('training/patient100/patient100_frame13_gt.nii.gz')#3
        img = sitk.GetArrayFromImage(itk_img)
        print(img.shape)  # (155, 240, 240) 表示各个维度的切片数量
        slices, width, height = img.shape
    for i in range(img.shape[0]):
        plt.imshow(img[i, :, :], cmap='gray')
        plt.axis('off')
        plt.gcf().set_size_inches(width / 100, height / 100)
        plt.gca().xaxis.set_major_locator(plt.NullLocator())
        plt.gca().yaxis.set_major_locator(plt.NullLocator())
        plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
        plt.margins(0, 0)
        plt.axis('off')
        if k==1: plt.savefig('./ED/image/' + 'ED100_' + str(i) + ".png", bbox_inches='tight', pad_inches=0.0)
        if k==2: plt.savefig('./ED/gt/' + 'ED100_' + str(i) + ".png", bbox_inches='tight', pad_inches=0.0)
        if k==3: plt.savefig('./ES/image/' + 'ES100_' + str(i) + ".png", bbox_inches='tight', pad_inches=0.0)
        if k==4: plt.savefig('./ES/gt/' + 'ES100_' + str(i) + ".png", bbox_inches='tight', pad_inches=0.0)

showNii(1)
showNii(2)
showNii(3)
showNii(4)