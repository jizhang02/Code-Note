import numpy as np
import tifffile as tiff
import matplotlib.image as mpimg # mpimg 用于读取图片
from PIL import Image

def split_img():
    tifpath = "C:/Users/Jing/Desktop/tiffdata/"
    dirtype = ("train", "label", "test")
    #split a tif volume into single tif
    for t in dirtype:
        imgarr = tiff.imread(tifpath + t + "-volume.tif")  # dimension 30x512x512
        for i in range(imgarr.shape[0]):
            imgname = tifpath + t + "/" + str(i) + ".tif"
            tiff.imsave(imgname, imgarr[i])

def split_tif():
    imgarr = tiff.imread('colon.tif')
    print(imgarr.shape)
    for i in range(imgarr.shape[0]):
        imgname = str(i)+'.tif'
        tiff.imsave(imgname,imgarr[i])
#split_img()
split_tif()
def merge_img():
    #merge single tif into a tif volume
    path = "C:/Users/Jing/Desktop/tiffdata/train/"
    merged_name = "train.tif"
    imgarr = []
    for i in range(30):
        img = tiff.imread(path + str(i) + ".tif")
        imgarr.append(img)
    tiff.imsave(path + merged_name, np.array(imgarr))

#merge_img()
def readoneimg(imagepath):
    # 3 matplotlib 类似matlab的方式
    #im1 = mpimg.imread(imagepath)
    #im1=Image.open(imagepath).convert("RGB")
    #im1 = np.array(im1)  # 获得numpy对象,RGB
    #for i in range(216):
       # for j in range(182):
          #  r, g ,b= im1.getpixel((i, j))
           # print(r, g,b)
    im1=Image.open(imagepath).convert("L")
    im1 = np.array(im1)  # 获得numpy对象,RGB
    #print((im1),np.mean(im1),np.max(im1))  # np.array
    print(im1.shape)
    print(np.where(im1==0))
    im1[np.where(im1==85)]=1
    im1[np.where(im1==170)]=2
    im1[np.where(im1==255)]=3
    im = Image.fromarray(im1)
    im.save('new.png')

