from PIL import Image,ImageChops
import os, sys
import numpy as np
import cv2
from libtiff import TIFF3D,TIFF


#path = "data/training_set_1998/label/"
#dirs = os.listdir(path)


def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray

def rgbconvertgrey():
    for item in dirs:
        if os.path.isfile(path + item):
            img = Image.open(path + item).convert('LA')
            #img.save('greyscale.png')
            #im = np.array(im)
            f, e = os.path.splitext(path + item)
            #img = rgb2gray(im)
            #img = Image.fromarray(im, 'L')
            img.save(f + "%d.png", 'PNG', quality=90)

def creatblack():
    for i in range(999):
        img_0 = np.zeros((64,64))
        img_0 = Image.fromarray(img_0, 'L')
        img_0.save(path+str(i)+".png",'PNG')



def rotate(degree):
    for item in dirs:
        if os.path.isfile(path + item):
            img = Image.open(path + item)
            f, e = os.path.splitext(path + item)
            img_rotate = img.rotate(degree)
            img_rotate.save(f+'rotate.png','PNG')

def flip():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f,e= os.path.splitext(path+item)
            out = im.transpose(Image.FLIP_LEFT_RIGHT)
            out.save(f+'_flip.png','PNG')

def shift(offset):
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f,e= os.path.splitext(path+item)
            out = ImageChops.offset(im, offset)
            out.save(f+'_shift.png','PNG')

def augment():
    offset = 5
    degree = 10
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f,e= os.path.splitext(path+item)
            img_rotate = im.rotate(degree)
            out = ImageChops.offset(img_rotate, offset)
            out = out.transpose(Image.FLIP_LEFT_RIGHT)
            out.save(f+'_rtf.png','PNG')
def augment1():
    offset = 5
    degree = 10
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f,e= os.path.splitext(path+item)
            out = im.transpose(Image.FLIP_LEFT_RIGHT)
            out = ImageChops.offset(out, offset)
            img_rotate = out.rotate(degree)
            img_rotate.save(f+'_ftr.png','PNG')
def augmentshift():
    offset_x = 40 # 1/20 of width
    offset_y = 27 # 1/20 of height

    #degree = 10
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f,e= os.path.splitext(path+item)
            #out = im.transpose(Image.FLIP_LEFT_RIGHT)
            out = ImageChops.offset(im, offset_x,offset_y)#x,y offset
            #img_rotate = out.rotate(degree)
            out.save(f+'_shift.png','PNG')
def augmentrotate():
    #offset = 5
    degree = 10
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f,e= os.path.splitext(path+item)
            #out = im.transpose(Image.FLIP_LEFT_RIGHT)
            #out = ImageChops.offset(im, offset)
            out = im.rotate(degree)
            out.save(f+'_rotate.png','PNG')
def augmentresize():
    offset = 5
    #degree = 10
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f,e= os.path.splitext(path+item)
            #out = im.transpose(Image.FLIP_LEFT_RIGHT)
            out = ImageChops.offset(im, offset)
            out = out.crop((100,50,700,500))#(left, upper, right, lower)
            out = out.resize((800,540))
            #img_rotate = out.rotate(degree)
            out.save(f+'_resize.png','PNG')
#path = "data/training_set999_800_540/hc/cv5/train - resize/"
#path = "data/training_set999_800_540/hc/cv5/train - rotation/"
#path = "data/training_set999_800_540/hc/cv5/train - shift/"

#dirs = os.listdir(path)
#augment()
#augmentresize()
#augmentrotate()
#augmentshift()



def normalization(img):
    #img_mean = np.mean(img)
    #img_std = np.std(img)
    #img_norm = (1 / img_std) * (img - img_mean)
    img_norm = (img-np.min(img))/(np.max(img)-np.min(img))
    return img_norm



def resize(image_size=(224,224)):
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item).convert('RGB')
            f, e = os.path.splitext(path+item)
            imResize = im.resize(image_size, Image.ANTIALIAS)
            #imResize = Image.fromarray(normalization(np.array(imResize)).astype('uint8'),'RGB') # normalization, u=0, std=1, labels don't need to do this
            imResize.save(f + "_224.png", quality=90)
path='data/training_set999_800_540/hc-10-07/cv5/valid/'
dirs = os.listdir(path)
resize()
def rename():
    i = 0
    for item in os.listdir(path):  # 进入到文件夹内，对每个文件进行循环遍历
        os.rename(os.path.join(path, item),
                  os.path.join(path, (str(i)+'.png')))  # os.path.join(path_name,item)表示找到每个文件的绝对路径并进行拼接操作
        i += 1
#rename()
def convertformat():
    for item in dirs:
        if os.path.isfile(path + item):
            im = Image.open(path + item)
            f, e = os.path.splitext(path + item)
            im.save(f + 'con.tif')

#画多条曲线在一个区域里
import json
from pprint import pprint
import pylab as pl
def curve_draw():
    #reading json file
    with open('file.json') as f:
        data = json.load(f)
        pprint(data['IOU'])
    #drawing plot
    x1 = [1, 2, 3, 4, 5]  # Make x, y arrays for each graph
    y1 = [1, 4, 9, 16, 25]
    x2 = [1, 2, 4, 6, 8]
    y2 = [2, 4, 8, 12, 16]
    x3 = []
    y3 = []
    pl.plot(x1, y1, 'r')  # use pylab to plot x and y
    pl.plot(x2, y2, 'g')
    pl.plot(x3, y3, 'b')


    pl.title('Plot of y')  # give plot a title
    pl.xlabel('x axis')  # make axis labels
    pl.ylabel('y axis')


    pl.xlim(0.0, 9.0)  # set axis limits
    pl.ylim(0.0, 30.)

    pl.show()  # show the plot on the screen

from scipy.optimize import fsolve    #导入扩展库scipy(求解线性方程组，矩阵、数值计算等)
import scipy
from scipy import integrate          #导入扩展库scipy（积分函数）
import matplotlib.pyplot as plt       #导入扩展库matplotlib(数据可视化、作图工具等)

plt.rcParams['font.sans-serif'] = ['SimHei']      #图像中正常显示中文字体
#显示图像格式
def channels():
    im = Image.open("C:/Users/Jing/Desktop/PycharmProjects/unet-finetune-crossvalid/data/notmelanoma/train/image/8.png")
    im.getbands()

def f3():
    #求解非线性方程组
    # def f(x):
    #     x1 = x[0]
    #     x2 = x[1]
    #     return [2*x1-x2**2-1,x1**2-x2-2]
    # result = fsolve(f,[1,1])
    # print(result[0],result[1])
    x = np.linspace(0,1,100)          #作图的自变量x
    #y = np.sqrt(2*x-1)                  #因变量y
    a = 0.9
    y = (a-x)/(1-x)
    #z = np.square(x)-2                  #因变量z
    plt.figure(figsize=(8,4))           #设置图像大小
    plt.plot(x,y,label = '$(Pa-Pc)/(1-Pc)$',color = 'red',linewidth = 2)  #作图，设置标签、线条颜色、线条大小
    #plt.plot(x,z,'b--',label = '$\cosx^3+1$',linewidth = 1)                      #作图，设置标签、
    plt.xlabel('Pc')            #x轴名称
    plt.ylabel('Kappa')                 #y轴名称
    plt.title('Kappa index')     #标题
    plt.ylim(0,1.1)                     #y轴的范围
    plt.legend()                        #显示图例

    plt.savefig('function.png')         #保存作图结果
    plt.show()                          #显示作图结果
#curve_draw()
#resize(image_size=(128,128))#调用函数需要顶格，才能运行 for train
#rename()
#flip() #for test

#normalization()
#convert()
#f3()
#rgbconvertgrey()
