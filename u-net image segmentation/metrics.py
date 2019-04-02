#Auther:ZHANG Jing
#Email address:jing.zhang@insa-rouen.fr
#Date:2019-04-02
#Title:performing metrics on the test data
#Usage:right clicked the mouse to run the code

from PIL import Image
import os, sys
import glob
import sklearn.metrics
from binary import *
import numpy as np

label_path = "./data/melanoma1/test/label/*.png"
predict_path = "./data/melanoma1/test/predict/*.png"
gt = []
seg = []
IOU = []
hausdorff = []
acc = []
loss = []

img = Image.open("./data/melanoma1/test/predict/0_predict.png")
img = np.array(img).astype(int)
print (img.shape)#(128,128)
print (img.dtype)#bool
img[img>1]=1#let the pixel only have 0 or 1
print(img[99][90])#0 or 1
print (img.size)#16384
print (type(img))#<class 'numpy.ndarray'>

for filename in glob.glob(label_path):
    imlabel = Image.open(filename)
    imlabel = np.array(imlabel).astype(int)
    imlabel[imlabel>1] = 1
    gt.append(imlabel)

for filename in glob.glob(predict_path):
    impred = Image.open(filename)
    impred = np.array(impred).astype(int)
    impred[impred>1] = 1
    seg.append(impred)

array_length = len(gt)
print(array_length)#20

for item in range(array_length):
    IOU.append(dc(gt[item],seg[item]))
    #print("IOU is: ",IOU[item])
    hausdorff.append(hd(gt[item], seg[item]))
    #print("The Hausdorff Distance is: ", hausdorff[item])
    acc.append(sklearn.metrics.accuracy_score(gt[item], seg[item]))
    #print("The Accuracy is: ", acc[item])
    loss.append(sklearn.metrics.log_loss(gt[item], seg[item]))
    #print("The Loss is: ", loss[item])

print("The mean IOU is: ",np.mean(IOU))
print("The std IOU is: ",np.std(IOU))
print("The mean Hausdorff Distance is: ",np.mean(hausdorff))
print("The std Hausdorff Distance is: ",np.std(hausdorff))
print("The mean accuracy is: ",np.mean(acc))
print("The std accuracy is: ",np.std(acc))
print("The mean loss is: ",np.mean(loss))
print("The std loss is: ",np.std(loss))