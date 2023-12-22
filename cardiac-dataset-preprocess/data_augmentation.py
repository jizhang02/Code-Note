'''
Title: Medical image data augmentation,
only flipping and translation.
Count pixels in one class, which is the area of the class.
Author: Jing Zhang
Date: 2021-04-23
'''

from PIL import Image,ImageChops
import SimpleITK as sitk ## using simpleITK to load and save data.
import glob, os
from tqdm import tqdm
import numpy as np
import cv2
from matplotlib import pyplot as plt

def Info(images_path):
    imagelist = sorted(glob.glob(os.path.join(images_path, '*.gz')))  # sorted按名称排序,glob.glob 匹配,os.path.join字符串拼接
    for i in (range(len(imagelist))):
        print(imagelist[i][37:])

Info('ACDC_3D_multi_slice/dataset9/img_aug/')
def PixelCount():
    img = cv2.imread('ACDC_3D_cardiac_target/gt-ori/p001_fm01.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    BKG = 0
    RV = 85
    MYO = 170
    LV = 255
    pixel_count_BKG = (img == BKG).sum()
    pixel_count_RV = (img == RV).sum()
    pixel_count_MYO = (img == MYO).sum()
    pixel_count_LV = (img == LV).sum()

    print('The number of pixel_count_BKG is: ', pixel_count_BKG)
    print('The number of pixel_count_RV is: ', pixel_count_RV)
    print('The number of pixel_count_MYO is: ', pixel_count_MYO)
    print('The number of pixel_count_LV is: ', pixel_count_LV)

    cv2.namedWindow("opencv")
    cv2.imshow("opencv", img)
    cv2.waitKey(0)

def BatchPixelCount():
    BKG = 0
    RV = 85
    MYO = 170
    LV = 255
    for item in dirs:
        if os.path.isfile(path + item):
            img = cv2.imread(path + item)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            pixel_count_BKG = (img == BKG).sum()
            pixel_count_RV = (img == RV).sum()
            pixel_count_MYO = (img == MYO).sum()
            pixel_count_LV = (img == LV).sum()
            #print('The number of pixel_BKG is: ', pixel_count_BKG)
            #print('The number of pixel_RV is: ', pixel_count_RV)
            #print('The number of pixel_MYO is: ', pixel_count_MYO)
            #print('The number of pixel_LV is: ', pixel_count_LV)
            print(pixel_count_LV)


#path='ACDC_3D_cardiac_target/gt-ori/'
#dirs = os.listdir(path)
#BatchPixelCount()

def MedShift(images_path,shiftX,shiftY):
    imagelist = sorted(glob.glob(os.path.join(images_path, '*.nii.gz')))  # sorted按名称排序,glob.glob 匹配,os.path.join字符串拼接
    for i in tqdm(range(len(imagelist))) :
        print(imagelist[i])
        itk_img = sitk.ReadImage(imagelist[i])
        img = sitk.GetArrayFromImage(itk_img)
        M = np.float32([
            [1, 0, shiftX],
            [0, 1, shiftY]
        ])
        for k in range(0,img.shape[0]):# for each slice
            height, width= img[k].shape
            img[k] = cv2.warpAffine(img[k], M, (width, height))

        img = sitk.GetImageFromArray(img)
        sitk.WriteImage(img, imagelist[i])
#src = 'dataset_nii/img/'
#MedShift(src,0,2)

def MedRotate(images_path,angle):
    imagelist = sorted(glob.glob(os.path.join(images_path, '*.nii.gz')))  # sorted按名称排序,glob.glob 匹配,os.path.join字符串拼接
    for i in tqdm(range(len(imagelist))):
        print(imagelist[i])
        itk_img = sitk.ReadImage(imagelist[i])
        img = sitk.GetArrayFromImage(itk_img)
        for k in range(0, img.shape[0]):  # for each slice
            #img[k] = cv2.flip(img[k], 0)  # 1 for Horizontal,0 for vertical
            height, width= img[k].shape
            rotate_around = (width // 2, height // 2)
            M = cv2.getRotationMatrix2D(rotate_around, angle, 1)
            img[k] = cv2.warpAffine(img[k], M, (width, height))

        img = sitk.GetImageFromArray(img)
        sitk.WriteImage(img, imagelist[i])
#src = 'dataset_nii/img/'
#MedRotate(src, angle=3)


def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

def normalization(img):
    #img_norm = (1 / np.std(img)) * (img - np.mean(img))
    img_norm = (img-np.min(img))/(np.max(img)-np.min(img))
    return img_norm

def channels():
    im = Image.open("fited.png")
    return im.getbands()#('R', 'G', 'B')

def rgbconvertgrey():
    for item in dirs:
        if os.path.isfile(path + item):
            img = Image.open(path + item).convert('LA')
            f, e = os.path.splitext(path + item)
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
            img_rotate = img.rotate(degree,fillcolor=(0,0,0))
            img_rotate.save(f+'r5.png','PNG')
#path='ACDC_3D_cardiac_target/gt/'
#dirs = os.listdir(path)
#rotate(5)
def flip():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f,e= os.path.splitext(path+item)
            out = im.transpose(Image.FLIP_LEFT_RIGHT)# Image.FLIP_TOP_BOTTOM
            out.save(f+'_flip.png','PNG')

def shift(offset_x,offset_y):
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f,e= os.path.splitext(path+item)
            out = ImageChops.offset(im, offset_x,offset_y)#x,y offset
            out.save(f+'y5.png','PNG')

def augment_rot():
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

def augment_tor():
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
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f,e= os.path.splitext(path+item)
            out = ImageChops.offset(im, offset_x,offset_y)#x,y offset
            out.save(f+'_shift.png','PNG')

def augmentrotate():
    degree = 10
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f,e= os.path.splitext(path+item)
            out = im.rotate(degree)
            out.save(f+'_rotate.png','PNG')

def augmentcropresize():
    offset = 5
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f,e= os.path.splitext(path+item)
            out = ImageChops.offset(im, offset)
            out = out.crop((100,50,700,500))#(left, upper, right, lower)
            out = out.resize((800,540))
            out.save(f+'_resize.png','PNG')
#path = "data/training_set999_800_540/hc/cv5/train - resize/"
#path = "data/training_set999_800_540/hc/cv5/train - rotation/"
#path = "data/training_set999_800_540/hc/cv5/train - shift/"

#dirs = os.listdir(path)
#augment()
#augmentresize()
#augmentrotate()
#augmentshift()


def resize(image_size=(800,540)):
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)#.convert('RGB')
            f, e = os.path.splitext(path+item)
            imResize = im.resize(image_size, Image.ANTIALIAS)
            imResize.save(f + "_ori.png", quality=90)
#path='HC_data/temp/'
#dirs = os.listdir(path)
#resize()

def rename():
    i = 0
    for item in os.listdir(path):
        os.rename(os.path.join(path, item),os.path.join(path, (str(i)+'.png')))
        i += 1
#rename()

def readfiles():
    img_list = os.listdir(path)
    img_list.sort(key=lambda x: int(x[:-4]))  #文件名按数字排序
    for i in range(len(img_list)):
        img_name = path + img_list[i]
        print(img_name)
#readfiles()
def convertformat():
    for item in dirs:
        if os.path.isfile(path + item):
            im = Image.open(path + item)
            f, e = os.path.splitext(path + item)
            im.save(f + 'converted.tif')

#a=np.load('HC_data/Test2.npy')
#print(a)