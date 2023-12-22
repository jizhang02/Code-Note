'''
-----------------------------------------------
File Name: image_reading.py
Description: Different image reading methods.
Author: Jing (zhangjingnm@hotmail.com)
Date: 7/5/2021
-----------------------------------------------
'''

#encoding=utf8
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import skimage
import sys
from skimage import io

#PIL
#相关:scipy.misc.imread, scipy.ndimage.imread
#misc.imread 提供可选参数mode，但本质上是调用PIL，具体的模式可以去看srccode或者document
#https://github.com/scipy/scipy/blob/v0.17.1/scipy/misc/pilutil.py
imagepath='0.png'
#im1=Image.open(imagepath).convert("L")
im1=Image.open(imagepath)
im1=np.array(im1)#获得numpy对象,RGB
print(type(im1))
print(im1.shape)

#2 opencv
im2=cv2.imread(imagepath)
#im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)  # the problem sovled by changing the img reading methods!
print(type(im2))#numpy BGR
print(im2.shape)#[width,height,3]

#3 matplotlib 类似matlab的方式
im3 = mpimg.imread(imagepath)
print(type(im3))#np.array
print(im3.shape)

#4 skimge
#caffe.io.load_iamge()也是调用的skimage实现的，返回的是0-1 float型数据
im4 = io.imread(imagepath, as_gray=False)
print(type(im4))#np.array
print(im4.shape)
#print(im4)


# cv2.imshow('test',im4)
# cv2.waitKey()
#统一使用plt进行显示，不管是plt还是cv2.imshow,在python中只认numpy.array，但是由于cv2.imread 的图片是BGR，cv2.imshow 时相应的换通道显示
plt.subplot(221)
plt.title('PIL read')
plt.imshow(im1)
plt.subplot(222)
plt.title('opencv read')
plt.imshow(im2)
plt.subplot(223)
plt.title('matplotlib read')
plt.imshow(im3)
plt.subplot(224)
plt.title('skimage read')
plt.imshow(im4)
#plt.axis('off') # 不显示坐标轴
plt.show()
plt.savefig("image encoder.png")

##################################### cmd output################################
# <class 'numpy.ndarray'>
# (851, 1279, 3)
# <class 'numpy.ndarray'>
# (851, 1279, 3)
# <class 'numpy.ndarray'>
# (851, 1279, 3)
# <class 'numpy.ndarray'>
# (851, 1279, 3)