#Auther:ZHANG Jing
#Email address:jing.zhang@insa-rouen.fr
#Date:2018-11-21
#Title:performing Grabcut method to segmentate a image
#Usage:right clicked the mouse to run the code
#url: https://blog.csdn.net/llh_1178/article/details/73321075

import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
from scipy.misc import pilutil
import matplotlib.image as mpimg
#image size
im = Image.open('data/skin1.jpg')
width, height = im.size
print(width)
print(height)
# 首先加载图片，然后创建一个与所加载图片同形状的掩模，并用0填充。load image, build mask filled with 0
img = cv2.imread("data/skin1.jpg")
mask = np.zeros(img.shape[:2], np.uint8)

# 然后创建以0填充的前景和背景模型：creat background model and foreground model
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
# 在实现GrabCut算法前，先用一个标识出想要隔离的对象的矩形来初始化它，这个矩形我们用下面的一行代码定义（x,y,w,h）：
#user define a rectangle
rect = (300, 500, 500, 800)
# 接下来用指定的空模型和掩摸来运行GrabCut算法
# mask, bgdModel, fgdModel = cv2.grabCut(img,mask,None,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_MASK)
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)  # 5是指算法的迭代次数。
# 然后，我们再设定一个掩模，用来过滤之前掩模中的值（0-3）。值为0和2的将转为0，值为1和3的将转化为1，这样就可以过滤出所有的0值像素（背景）。
# filter the background
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")
img = img * mask2[:, :, np.newaxis]

# 最后可视化图像 visualize the image
img = pilutil.toimage(img).convert('LA')#转换为灰度图，十分重要！
width = img.size[0]#长度
height = img.size[1]#宽度
for i in range(0,width):#遍历所有长度的点
    for j in range(0,height):#遍历所有宽度的点
        data = (img.getpixel((i,j)))#打印该图片的所有点
        print (data)#打印每个像素点的颜色RGBA的值(r,g,b,alpha)
        print (data[0])#打印RGBA的r值
        # RGB的r值不等于0的，改为白色
        if (data[0]!=0 and data[1]!=0):
            img.putpixel((i,j),(255,255))

img.save('skingrabcut.png')
img.show()

