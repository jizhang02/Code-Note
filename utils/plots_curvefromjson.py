'''
-----------------------------------------------
File Name: plots_curvefromjson.py
Description: Drawing learning curve in training,
validation, test stage from log file.
Author: Jing (zhangjingnm@hotmail.com)
Date: 7/5/2021
-----------------------------------------------
'''

import matplotlib.pyplot as plt
import os
from sklearn.preprocessing import MinMaxScaler
import json
import numpy as np
import matplotlib as mpl
json_path0 = 'data/epoch200ISIC2016Dice.json'
json_path1 = 'data/epoch200kappaISIC2016.json'
json_path2 = 'data/log2.json'
json_path3 = 'C:/Users/Jing/Desktop/PycharmProjects/experiments results/Melanoma/log/Dicesm50.json'
json_path4 = 'C:/Users/Jing/Desktop/PycharmProjects/experiments results/Melanoma/log/Dicesm100.json'

save_fig_dir = os.path.join(os.getcwd(), 'figures') # folder where to save the png file corresponding to the computed curves
save_fig_filename = 'fig.png'                        # filename of the png file saved in the folder defined above

def multifigurecurve():
    #多个图
    with open(json_path0, 'r') as f:
        temp = json.loads(f.read())
        loss0 = temp['loss']
        loss0 = MaxMinNormalization(loss0, np.max(loss0), np.min(loss0))
        acc0 = temp['acc']
        IOU0 = temp['IOU']
        epoch = len(loss0)
    with open(json_path1, 'r') as f:
        temp = json.loads(f.read())
        loss1 = temp['loss']
        loss1 = MaxMinNormalization(loss1, np.max(loss1), np.min(loss1))
        acc1 = temp['acc']
        IOU1 = temp['IOU']
    # with open(json_path2, 'r') as f:
    #     temp = json.loads(f.read())
    #     loss2 = temp['loss']
    #     loss2 = MaxMinNormalization(loss2, np.max(loss2), np.min(loss2))
    #     acc2 = temp['acc']
    #     IOU2 = temp['IOU']
    # with open(json_path3, 'r') as f:
    #     temp = json.loads(f.read())
    #     loss3 = temp['loss']
    #     loss3 = MaxMinNormalization(loss3, np.max(loss3), np.min(loss3))
    #     acc3 = temp['acc']
    #     IOU3 = temp['IOU']
    # with open(json_path4, 'r') as f:
    #     temp = json.loads(f.read())
    #     loss4 = temp['loss']
    #     loss4 = MaxMinNormalization(loss4, np.max(loss4), np.min(loss4))
    #     acc4 = temp['acc']
    #     IOU4 = temp['IOU']

        # Retrieve values from the log
        time_steps = range(epoch)
        if not os.path.isdir(save_fig_dir):
            os.makedirs(save_fig_dir)

        # Display loss and metrics curves
        fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4), dpi=600)
        #first figure
        ax[0].plot(time_steps, loss0, 'r', label='Dice')#first curve
        ax[0].plot(time_steps, loss1, 'g', label='Kappa')#second curve
        #ax[0].plot(time_steps, loss2, 'b', label='ce')#third curve

        ax[0].legend()
        ax[0].set_xlabel('Epoch')
        ax[0].set_ylabel('Value')
        ax[0].set_title('Loss')
        #second figure
        ax[1].plot(time_steps, IOU0, 'r', label='Dice')
        ax[1].plot(time_steps, IOU1, 'g', label='Kappa')
        #ax[1].plot(time_steps, IOU2, 'b', label='ce')

        ax[1].legend()
        ax[1].set_xlabel('Epoch')
        ax[1].set_ylabel('Value')
        ax[1].set_title('Dice Index')
        #third figure
        # ax[2].plot(time_steps, loss2, 'r', label='Dice')
        # ax[2].plot(time_steps, loss22, 'g', label='Kappa')
        # ax[2].legend()
        # ax[2].set_xlabel('Epoch')
        # ax[2].set_ylabel('Value')
        # ax[2].set_title('smooth = 10')

        #ax[3].plot(time_steps, loss3, 'r', label='Dice')
        #ax[3].plot(time_steps, loss33, 'g', label='Kappa')
        #ax[3].legend()
        #ax[3].set_xlabel('Epoch')
        #ax[3].set_ylabel('Value')
        #ax[3].set_title('smooth = 50')

        # ax[3].plot(time_steps, loss4, 'r', label='Dice')
        # ax[3].plot(time_steps, loss44, 'g', label='Kappa')
        # ax[3].legend()
        # ax[3].set_xlabel('Epoch')
        # ax[3].set_ylabel('Value')
        # ax[3].set_title('smooth = 100')

        fig.tight_layout()
        fig.savefig(os.path.join(save_fig_dir, save_fig_filename), dpi=200, orientation='landscape', format='png')

def MaxMinNormalization(x,Max,Min):
    x = (x - Min) / (Max - Min)
    return x

def multicurvefigure():
    # -*- coding: UTF-8 -*-
    # python 一个折线图绘制多个曲线
    with open(jsonpath0, 'r') as f:
        temp = json.loads(f.read())
        loss0 = temp['loss']
        loss0 = MaxMinNormalization(loss0,np.max(loss0),np.min(loss0))
        acc0 = temp['acc']
        IOU0 = temp['IOU']
        epoch = len(loss0)
    with open(jsonpath1, 'r') as f:
        temp = json.loads(f.read())
        loss1 = temp['loss']
        loss1 = MaxMinNormalization(loss1, np.max(loss1), np.min(loss1))
        acc1 = temp['acc']
        IOU1 = temp['IOU']
    with open(jsonpath2, 'r') as f:
        temp = json.loads(f.read())
        loss2 = temp['loss']
        loss2 = MaxMinNormalization(loss2,np.max(loss2),np.min(loss2))
        acc2 = temp['acc']
        IOU2 = temp['IOU']
    # with open(json_path3, 'r') as f:
    #     temp = json.loads(f.read())
    #     loss3 = temp['loss']
    #     loss3 = MaxMinNormalization(loss3,np.max(loss3),np.min(loss3))
    #     acc3 = temp['acc']
    #     IOU3 = temp['IOU']
    # with open(json_path4, 'r') as f:
    #     temp = json.loads(f.read())
    #     loss4 = temp['loss']
    #     loss4 = MaxMinNormalization(loss4, np.max(loss4), np.min(loss4))
    #     acc4 = temp['acc']
    #     IOU4 = temp['IOU']
    # 开始画图

    time_steps = range(epoch)
    plt.title('Loss changing')
    plt.plot(time_steps, loss0, color='green', label='no smooth')
    plt.plot(time_steps, loss1, color='red', label='smooth = 1')
    plt.plot(time_steps, loss2, color='skyblue', label='smooth = 10')
    # plt.plot(time_steps, loss3, color='yellow', label='smooth = 50')
    # plt.plot(time_steps, loss4, color='black', label='smooth = 100')

    #plt.title('Accuracy')
    #plt.plot(time_steps, acc0, color='green', label='no smooth')
    #plt.plot(time_steps, acc1, color='red', label='smooth = 1')
    #plt.plot(time_steps, acc2, color='skyblue', label='smooth = 10')
    #plt.plot(time_steps, acc3, color='yellow', label='smooth = 50')
    #plt.plot(time_steps, acc4, color='black', label='smooth = 100')

    #plt.title('Intersection over Union')
    #plt.plot(time_steps, IOU0, color='green', label='no smooth')
    #plt.plot(time_steps, IOU1, color='red', label='smooth = 1')
    #plt.plot(time_steps, IOU2, color='skyblue', label='smooth = 10')
    #plt.plot(time_steps, IOU3, color='yellow', label='smooth = 50')
    #plt.plot(time_steps, IOU4, color='black', label='smooth = 100')

    plt.legend()  # 显示图例

    plt.xlabel('Epochs')
    plt.ylabel('Value')
    plt.tight_layout()
    plt.savefig(os.path.join(save_fig_dir, save_fig_filename), dpi=200, orientation='landscape', format='png')

multifigurecurve()
#multicurvefigure()
#
# #hausdorff distance
# from PIL import Image
# import os, sys
# import glob
# import sklearn.metrics
# from binary import *
# import numpy as np
# from scipy.spatial.distance import directed_hausdorff
# from sklearn import preprocessing
# label_path = "data/skin data set/test/label/*.png"
# predict_path = "data/skin data set/test/predict/*.png"
# gt = []
# seg = []
# IOU = []
# hausdorff = []
# acc = []
# loss = []
# precision = []
#
# #img = Image.open("./data/melanoma1/test/predict/0_predict.png")
# #img = np.array(img).astype(int)
# #print (img.shape)#(128,128)
# #print (img.dtype)#bool
# #img[img>1]=1#let the pixel only have 0 or 1
# #print(img[99][90])#0 or 1
# #print (img.size)#16384
# #print (type(img))#<class 'numpy.ndarray'>
# def zscore(X):
#     X = (X-np.mean(X))/np.std(X)**2
#     return X
# for filename in glob.glob(label_path):
#     imlabel = Image.open(filename)
#     imlabels = np.array(imlabel).astype(int)
#     #imlabel_scaled = preprocessing.scale(imlabel_scaled)#z-score (x-mean)/std
#     imlabel[imlabels>1] = 1
#     #imlabel_scaled = zscore(imlabel_scaled)
#     #print("the mean is :",imlabel_scaled.mean(axis=0))
#     #print("the std is :",imlabel_scaled.std(axis=0))
#     gt.append(imlabel)
#
# for filename in glob.glob(predict_path):
#     impred = Image.open(filename)
#     impred_scaled = np.array(impred)
#     #impred_scaled = zscore(impred_scaled)
#     #impred_scaled = preprocessing.scale(impred_scaled)  # z-score (x-mean)/std
#     #impred = (impred - np.average(impred)) / np.std(impred)
#     impred[impred_scaled>1] = 1
#     seg.append(impred)
#
# array_length = len(gt)
# print("the number of images: ",array_length)#20
#
# for item in range(array_length):
#     IOU.append(dc(gt[item],seg[item]))
#     #print("IOU is: ",IOU[item])
#     #hausdorff.append(hd(seg[item], gt[item]))
#     hausdorff.append(max(directed_hausdorff(seg[item], gt[item])[0], directed_hausdorff(gt[item],seg[item])[0]))
#     #print("The Hausdorff Distance is: ", hausdorff[item])
#     #acc.append(sklearn.metrics.accuracy_score(gt[item], seg[item]))
#     #print("The Accuracy is: ", acc[item])
#     #loss.append(sklearn.metrics.log_loss(gt[item], seg[item]))
#     #print("The Loss is: ", loss[item])
#     #precision.append(precision(gt[item], seg[item]))
#
# print("The mean and std test IOU is: ",'%.2f'%np.mean(IOU),'%.2f'%np.std(IOU))
# print("The mean amd std test Hausdorff Distance is: ",'%.2f'%np.mean(hausdorff),'%.2f'%np.std(hausdorff))
# #print("The mean and std test accuracy is: ",'%.2f'%np.mean(acc),'%.2f'%np.std(acc))
# #print("The mean and std test loss is: ",'%.2f'%np.mean(loss),'%.2f'%np.std(loss))
