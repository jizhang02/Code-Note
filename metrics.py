from PIL import Image
import os, sys
import glob
import sklearn.metrics
from scipy.spatial.distance import directed_hausdorff
import numpy as np


def IOU(y_true, y_pred):
    smooth = 1
    y_true_f = y_true.flatten()
    y_pred_f = y_pred.flatten()
    intersection = sum(y_true_f * y_pred_f)
    return (2. * intersection +smooth) / (sum(y_true_f) + sum(y_pred_f) +smooth)

label_path = "./data/melanoma1/test/label/*.png"
predict_path = "./data/melanoma1/test/predict/*.png"
gt = []
seg = []

for filename in glob.glob(label_path):
    iml = Image.open(filename)
    iml = np.array(iml).astype(int)
    gt.append(iml)

for filename in glob.glob(predict_path):
    imp = Image.open(filename)
    imp = np.array(imp).astype(int)
    seg.append(imp)
print(seg[0])
array_length = len(gt)
print(array_length)

for item in range(array_length):
    print("IOU is: ",IOU(gt[item],seg[item]))
    hsdf0 = directed_hausdorff(gt[item], seg[item])[0]
    hsdf1 = directed_hausdorff(seg[item], gt[item])[0]
    print("The AverageHausdorffDistance is: ", (hsdf1+hsdf0)/2)
    acc =  sklearn.metrics.accuracy_score(gt[item], seg[item])
    print("The Accuracy is: ", acc)
    loss = sklearn.metrics.log_loss(gt[item], seg[item])
    print("The Loss is: ", loss)