'''
-----------------------------------------------
File Name: file_mat.py
Description: Processing mat file.
Author: Jing (zhangjingnm@hotmail.com)
Date: 7/5/2021
-----------------------------------------------
'''

import cv2
import scipy.io as scio
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import math
# 数据矩阵转图片的函数

def singlemat():
    dataFile = r'C:/Users/Jing/Desktop/hk_data/dr/PSTDR008_OD_sn57247.mat' # 单个的mat文件
    # Import to a python dictionary
    data = scio.loadmat(dataFile)
    print(data.items())
    # 取出需要的数据矩
    im = data['IM']
    print(np.shape(im))
    im = np.uint8(im)
    list = np.dsplit(im,128)
    print(list[0])
    print("shape of list[0]",np.shape(list[0]))
    print("this is",list[2])
    img = list[0].reshape(1024,512)#如果是-1则表示可以自动推测出。
    print("shape after reshape:",np.shape(img),img)
    img = Image.fromarray(img, 'L')
    #img.save('my.png')
    img.show()
    #im = Image.fromarray(im)
    #img = Image.fromarray(im.astype(np.uint8))
    #plt.imshow(im, cmap=plt.gray, interpolation='nearest')
    #im.show()
    ##im.save('reggae.00041.bmp') # 保存图片
singlemat()

def batchmat2img():
    # 添加路径，metal文件夹下存放mental类的特征的多个.mat文件
    folder = r'/Users/Desktop/metal'
    path = os.listdir(folder)
    #print(os.listdir(r'/Users/hjy/Desktop/blues'))
    for each_mat in path:
        if each_mat == '.DS_Store':
            pass
        else:
            first_name, second_name = os.path.splitext(each_mat)
            # 拆分.mat文件的前后缀名字，注意是**路径**
            each_mat = os.path.join(folder, each_mat)
            # print(each_mat)
            array_struct = scio.loadmat(each_mat)
            array_data = array_struct['data']# 取出需要的数字矩阵部分
            img = Image.fromarray(array_data.astype(np.uint8))
            plt.imshow(img, cmap=plt.gray, interpolation='nearest')
            img.show()
            print(first_name)
            img.save(first_name+'.bmp')# 保存图片