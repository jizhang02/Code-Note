import numpy as np
import cv2
from PIL import Image
from scipy.misc import pilutil

im = Image.open('data/orig3.jpg')
width, height = im.size
print(width)
print(height)
#load image, build mask filled with 0
img = cv2.imread("data/orig3.jpg")
mask = np.zeros(img.shape[:2], np.uint8)
#creat background model and foreground model
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
#user define a rectangle
rect = (300, 500, 500, 800)
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)#5 is iteration
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")
img = img * mask2[:, :, np.newaxis]

# visualize the image
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

img.save('grabcut-iter5.png')
img.show()