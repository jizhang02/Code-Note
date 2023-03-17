'''
-----------------------------------------------
File Name: log_curve$
Description:
Author: Jing$
Date: 7/5/2021$
-----------------------------------------------
'''
'''
Title: Drawing learning curve in training, validation, test stage
from log file.
Author: Jing Zhang
Date: 2021-04-23
'''

import glob
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy import stats
import seaborn as sns
import scipy.stats as stats

def p_value():
    csv_file = 'HCdata/test/HC_ori_test-results.csv'
    df = pd.read_csv(csv_file)
    # U-net-ori Unet-resno W-net psp-resnet xnet-resnet unet-resnet link-resnet fpn-resnet
    # hc-reg-efn-mae hc-reg-efn-mse hc-reg-efn-hl
    obj1 = df['unet-resnet'].values
    obj2 = df['hc-reg-efn-mse'].values

    t_statistic0, p_value0 = stats.ttest_rel(obj1, obj2)
    print("The p_value is : ",'%.3f'%p_value0)
p_value()

def MaxMinNormalization(x):
    Max = np.max(x)
    Min = np.min(x)
    x = (x - Min) / (Max - Min)
    return x

def Learningcurve_3loss():
    path0 = "7977719/unet-hc18/logs/log5.csv"
    path1 = "7980741/unet-hc18/logs/log5.csv"
    path2 = "7977821/unet-hc18/logs/log5.csv"

    data0 = pd.read_csv(path0)
    data1 = pd.read_csv(path1)
    data2 = pd.read_csv(path2)

    xdata0 = data0.loc[:, 'epoch']
    ydata0 = data0.loc[:, 'IOU']
    ydata1 = data1.loc[:, 'IOU']
    ydata2 = data2.loc[:, 'IOU']
    ydata0 = MaxMinNormalization(ydata0)
    ydata1 = MaxMinNormalization(ydata1)
    ydata2 = MaxMinNormalization(ydata2)
    plt.figure(1)
    plt.title('Learning curve')
    plt.plot(xdata0, ydata0, color='green', label='Kappa+Focal')
    plt.plot(xdata0, ydata1, color='blue', label='Kappa loss')
    plt.plot(xdata0, ydata2, color='purple', label='Dice loss')
    plt.legend()
    plt.xlabel('Epochs')
    plt.ylabel('Value')
    plt.tight_layout()
    plt.savefig(os.path.join(save_fig_dir, save_fig_filename), dpi=200, orientation='landscape', format='pdf')
    plt.show()


def Learningcurve_train_valid():
    path0 = "logs/log-1-linknet.csv"
    data0 = pd.read_csv(path0)
    xdata0 = data0.loc[:, 'epoch']
    #ydata0 = data0.loc[:, 'iou_score'] #iou_score;mean_absolute_error
    #ydata1 = data0.loc[:, 'val_iou_score']#val_iou_score;val_mean_absolute_error
    ydata2 = data0.loc[:, 'loss']
    ydata3 = data0.loc[:, 'val_loss']
    #plt.xlim((0, 100))
    #plt.ylim((0, 0.2))

    plt.figure(figsize=(5,4))# figsize=(10,8)
    #plt.title('Learning curve')
    #plt.plot(xdata0, ydata0, color='blue', label='iou_score')#
    #plt.plot(xdata0, ydata1, color='red', label='val_iou_score')#
    #plt.plot(xdata0, ydata2, color='green', label='tra_loss')
    #plt.plot(xdata0, ydata3, color='purple', label='val_loss')

    plt.plot(xdata0, ydata2, 'bo-', label=u'train loss', linewidth=1)
    plt.plot(xdata0, ydata3, 'or-', label=u'valid loss', linewidth=1)
    #plt.legend()
    plt.legend(loc = 0, prop = {'size':14})

    #plt.xlabel('Epochs')
    #plt.ylabel('Value')
    plt.tight_layout()
    plt.savefig(os.path.join(save_fig_dir, save_fig_filename), dpi=200, orientation='landscape', format='pdf')
    plt.show()


save_fig_dir = os.path.join(os.getcwd(), './')
save_fig_filename = 'curve_seglinknet.pdf'
# Learningcurve_3loss()
#Learningcurve_train_valid()

def read_test_set(img_path, csv_path):
    # for a test
    array = np.load('cv_array/train4.npy')
    df_ori = pd.read_csv(csv_path)
    hc_mm = df_ori['head circumference(mm)'].values
    hc_px = df_ori['head circumference(px)'].values
    pxsiz = df_ori['pixel size(mm)'].values
    # print(len(array))
    # print(sorted(array))
    imageindex = sorted(array)
    imagelist = sorted(glob.glob(os.path.join(img_path, '*.png')))
    for i in (imageindex):
        img = cv2.imread(imagelist[i])
        #cv2.imwrite('HCdata/test/gt/' + imagelist[i][14:], img)
        #print(imagelist[i][14:])
        # print(hc_mm[i])
        print(hc_px[i])
        # print(pxsiz[i])


# path = 'HCdata/gt_ori/'
# csv_path = 'HCdata/HC_ori.csv'
# read_test_set(path,csv_path)



def bland_altman_arg(data1, data2):
    data1 = np.asarray(data1)
    data2 = np.asarray(data2)
    mean = np.mean([data2, data1], axis=0)
    diff = data1 - data2  # Difference between data1 and data2
    md = np.mean(diff)  # Mean of the difference
    sd = np.std(diff, axis=0)  # Standard deviation of the difference
    return mean, diff, md, sd


def bland_altman_plots(filename, *args, **kwargs):
    path1 = "HCdata/test/HC_ori_test.csv"
    savepath = "HCdata/test/"
    file = pd.read_csv(path1)
    #
    data1a = file.loc[:, 'head circumference(mm)']  ## ground truth
    data1b = file.loc[:, 'link-resnet']  ## prediciton
    mean3, diff3, md3, sd3 = bland_altman_arg(data1a, data1b)
    print("mean difference:",md3,"stand deviation:",sd3)
    plt.figure(figsize=(5,4))
    plt.xlim(0, 350)
    plt.ylim(-10, 10)
    plt.scatter(mean3, diff3, *args, **kwargs)
    plt.axhline(md3, color='green', linestyle='--')
    plt.axhline(md3 + 1.96 * sd3, color='red')
    plt.axhline(md3 - 1.96 * sd3, color='red')
    plt.text(10, 9, '+1.96 SD :', fontdict={'size': 14, 'color': 'r'})
    plt.text(105, 9, str(round(md3 + 1.96 * sd3, 2)), fontdict={'size': 14, 'color': 'r'})
    plt.text(45, 7.5, 'Mean :', fontdict={'size': 14, 'color': 'r'})
    plt.text(105, 7.5, str(round(md3, 2)), fontdict={'size': 14, 'color': 'r'})
    plt.text(18, 6, '-1.96 SD :', fontdict={'size': 14, 'color': 'r'})
    plt.text(105, 6, str(round(md3 - 1.96 * sd3, 2)), fontdict={'size': 14, 'color': 'r'})
    #plt.title('U-Net(VGG) w/o pp')

    plt.tight_layout()
    plt.savefig(os.path.join(savepath, filename), dpi=200, orientation='landscape', format='pdf')
    plt.show()

#bland_altman_plots("bland_altmanseg2.pdf")


def correlation_plots():
    path = "HCdata/test/HC_ori_test.csv"
    file = pd.read_csv(path)

    data1a = file.loc[:, 'head circumference(mm)'] ## ground truth
    data1b = file.loc[:, 'hc-reg-efn-mse'] ## prediciton unet-resnet


    # r1,p1 = stats.pearsonr(data1a,data1b)  # 相关系数和P值
    # print('相关系数r为 = %6.3f，p值为 = %6.3f'%(r1,p1))
    # r2,p2 = stats.pearsonr(data2a,data2b)  # 相关系数和P值
    # print('相关系数r为 = %6.3f，p值为 = %6.3f'%(r2,p2))
    # r3,p3 = stats.pearsonr(data3a,data3b)  # 相关系数和P值
    # print('相关系数r为 = %6.3f，p值为 = %6.3f'%(r3,p3))
    # r4,p4 = stats.pearsonr(data4a,data4b)  # 相关系数和P值
    # print('相关系数r为 = %6.3f，p值为 = %6.3f'%(r4,p4))
    # 线性拟合，可以返回斜率，截距，r 值，p 值，标准误差
    slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(data1a, data1b)

    plt.figure(figsize=(5,4))
    plt.scatter(data1a, data1b, alpha=0.6)  # 绘制散点图，透明度为0.6（这样颜色浅一点，比较好看）
    plt.text(250, 100, 'r = '+str(round(r_value1,3)), fontdict={'size': 14, 'style':'italic','color': 'b'})
    plt.text(80, 300, 'y = '+str(round(slope1,3))+'x + '+ str(round(intercept1,3)), fontdict={'size': 14, 'style':'italic','color': 'b'})
    plt.xlim(50, 350)
    plt.ylim(50, 350)
    #plt.title('U-Net(VGG) w/o pp')

    plt.tight_layout()
    savepath = "HCdata/test/"

    plt.savefig(os.path.join(savepath, "reg2cor_plot.pdf"), dpi=200, orientation='landscape', format='pdf')
    plt.show()
#correlation_plots()

def bars():
    size = 4
    x = np.arange(size)
    #a = np.random.random(size)
    #b = np.random.random(size)
    #c = np.random.random(size)
    a = (29.0,68.26+1.38,3.06,1.84,)#seg
    b = (38.0,36.95,2.29,2.68,) #seg-free
    total_width, n = 0.8, 3
    width = total_width / n
    x = x - (total_width - width) / 2
    labels = ['Train(s/epoch)', 'Test(s/test set)', 'Mem-M(GB)', 'Mem-P(GB)']
    plt.bar(x, a, width=width,label='U-Net-B2')
    plt.bar(x + width, b, width=width, label='Reg-B3-L1',hatch='/')
    plt.xticks((-0.14,0.88,1.88,2.88), labels,fontsize=12)
    plt.text(-0.28,a[0] , str(a[0]), ha='center', va='bottom', fontsize=14, rotation=0)
    plt.text(0,b[0] , str(b[0]), ha='center', va='bottom', fontsize=14, rotation=0)

    plt.text(0.72,a[1] , str(a[1]), ha='center', va='bottom', fontsize=14, rotation=0)
    plt.text(1.05,b[1] , str(b[1]), ha='center', va='bottom', fontsize=14, rotation=0)

    plt.text(1.70,a[2] , str(a[2]), ha='center', va='bottom', fontsize=14, rotation=0)
    plt.text(2.02,b[2] , str(b[2]), ha='center', va='bottom', fontsize=14, rotation=0)

    plt.text(2.72,a[3] , str(a[3]), ha='center', va='bottom', fontsize=14, rotation=0)
    plt.text(3.03,b[3] , str(b[3]), ha='center', va='bottom', fontsize=14, rotation=0)

    #plt.barh(x, a,  label='a') # horizontal
    #plt.barh(x + width, b,  label='b')
    #plt.barh(x + 2 * width, c, label='c',hatch='o')
    plt.legend(fontsize=14)
    plt.tight_layout()
    savepath = "HCdata/test/"
    plt.savefig(os.path.join(savepath, "TM_cost_bar.pdf"), dpi=200, orientation='landscape', format='pdf')
    plt.show()
#bars()

