from PIL import Image
import os, sys
#from libtiff import TIFF3D,TIFF

#path = "/root/Desktop/python/images/"
#path = "C:/Users/Jing/Desktop/dermIS/train/"
#path = "C:/Users/Jing/Desktop/dermquest2/test/"
path = "./data/melanoma2/train/image/"
dirs = os.listdir(path)

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((128,128), Image.ANTIALIAS)
            imResize.save(f + "%d.png", 'PNG', quality=90)

def flip():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f,e= os.path.splitext(path+item)
            out = im.transpose(Image.ROTATE_180)
            out.save(f+'flip.png','PNG')

def rename():
    i = 0
    for item in os.listdir(path):  # 进入到文件夹内，对每个文件进行循环遍历
        os.rename(os.path.join(path, item),
                  os.path.join(path, (str(i) + '.png')))  # os.path.join(path_name,item)表示找到每个文件的绝对路径并进行拼接操作
        i += 1

def convert():
    for item in dirs:
        if os.path.isfile(path + item):
            im = Image.open(path + item)
            f, e = os.path.splitext(path + item)
            im.save(f + 'con.tif')


#split 30 single images from an array of images :
# train-volume.tif label-volume.tif test-volume.tif
def split_img():
    # split a tif volume into single tif
    for t in os.listdir(path):
        imgdir = TIFF3D.open("./data/"+t + "-volume.tif")
        imgarr = imgdir.read_image()
    for i in range(imgarr.shape[0]):
        imgname = t + "/" + str(i) + ".tif"
        img = TIFF.open(imgname,'w')
        img.write_image(imgarr[i])

#merge single tif into a tif volume
def merge_img():
    path = '/home/zhixuhao/Downloads/imgs_mask_test_server2/'
    imgdir = TIFF3D.open("test_mask_volume_server2.tif",'w')
    imgarr = []
    for i in range(30):
        img = TIFF.open(path + str(i) + ".tif")
        imgarr.append(img.read_image())
        imgdir.write_image(imgarr)


#split_img()
#resize()#调用函数需要顶格，才能运行 for train
#flip() #for test
rename()
#convert()
