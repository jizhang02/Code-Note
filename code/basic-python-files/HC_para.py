'''
-----------------------------------------------
File Name: HC_para$
Description: Draw the parameters of an ellipse; Sum up the number of pixels of an ellipse
Author: Jing$
Date: 7/21/2021$
-----------------------------------------------
'''
import glob
import math
import os

import matplotlib.pyplot as plt
import numpy as np
import cv2

def angle(a, b, c):
    """
    Return angle between lines ab, bc
    """
    ab = a - b
    cb = c - b
    return math.acos(np.dot(ab, cb) / (np.linalg.norm(ab) * np.linalg.norm(cb)))


def HC_para():
    path = 'HCdata/Challenge/fitted_result_version2/'
    img_list = os.listdir(path)
    img_list.sort(key=lambda x: int(x[:-12]))  ##文件名按数字排序,屏蔽除数字以外的字符
    print(img_list)
    for k in range(0, len(img_list)):
        image = plt.imread(path+img_list[k])  # read an image
        xs, ys, _ = np.where(image >= 1)  # get the position of label
        center = [np.mean(xs), np.mean(ys)]  # return (x, y)
        points = np.hstack((xs.reshape(-1, 1), ys.reshape(-1, 1)))  # reshape to one column, rows aotomatically formed.
        maximum = points[np.argmax(np.linalg.norm(center - points, axis=1))]  # return long axis coordinate
        minimum = points[np.argmin(np.linalg.norm(center - points, axis=1))]  # return short axis coordinate

        plt.figure(figsize=(10, 10))
        plt.scatter(center[1], center[0], c='white')  # center points
        plt.annotate((int(center[1]),int(center[0])), xy=(((center[1] -15) ), ((center[0] -15) )), xycoords='data', fontsize=12.0, textcoords='data',
                     ha='center', color='white')
        plt.scatter(maximum[1], maximum[0], c='green')  # long axis
        plt.annotate((int(maximum[1]), int(maximum[0])), xy=(((maximum[1] + 15)), ((maximum[0] + 15))), xycoords='data',
                     fontsize=12.0, textcoords='data',
                     ha='center', color='white')
        plt.scatter(minimum[1], minimum[0], c='green')  # short axis
        plt.annotate((int(minimum[1]), int(minimum[0])), xy=(((minimum[1] + 15)), ((minimum[0] + 15))), xycoords='data',
                     fontsize=12.0, textcoords='data',
                     ha='center', color='white')
        # draw center_x line
        plt.annotate('', xy=(center[1], 5), xytext=(0, 5), arrowprops={'arrowstyle': '<->', 'ec': 'r', 'lw': 1.5},
                     va='center')
        plt.annotate((int(center[1]),0), xy=((int(center[0])+70),0+20), xycoords='data',
                     fontsize=12.0, textcoords='data',
                     ha='center', color='white')
        plt.annotate('center_x', xy=(((center[1] + 0) / 2), 20), xycoords='data', fontsize=12.0, textcoords='data',
                     ha='center', color='yellow')
        # draw center_y line
        plt.annotate('', xy=(center[1], center[0]), xytext=(center[1], 0),
                     arrowprops={'arrowstyle': '<->', 'ec': 'r', 'lw': 1.5}, va='center')
        plt.annotate('', xy=(center[1], center[0]), xytext=(center[1], 540),
                     arrowprops={'arrowstyle': '<->', 'ec': 'b', 'lw': 1.5}, va='center')
        plt.annotate((int(center[1]), 550), xy=((int(center[1]) + 50), 500), xycoords='data',
                     fontsize=12.0, textcoords='data',
                     ha='center', color='white')
        plt.annotate('center_y', xy=(((center[1] + center[1]) / 2) + 10, (center[0] / 2)), ha='left', color='yellow')
        # draw semi axis a
        plt.annotate('', xy=(maximum[1], maximum[0]), xytext=(center[1], center[0]),
                     arrowprops={'arrowstyle': '<->', 'ec': 'r', 'lw': 1.5}, va='center')
        plt.annotate('semi_axe_a', xy=(((maximum[1] + center[1]) / 2), ((maximum[0] + center[0]) / 2)), ha='left',
                     color='yellow')
        # draw semi axis b
        plt.annotate('', xy=(minimum[1], minimum[0]), xytext=(center[1], center[0]),
                     arrowprops={'arrowstyle': '<->', 'ec': 'r', 'lw': 1.5}, va='center')
        plt.annotate('semi_axe_b', xy=(((minimum[1] + center[1]) / 2), ((minimum[0] + center[0]) / 2)), ha='left',
                     color='yellow')
        # draw angle
        # plt.annotate('', xy=(minimum[1]/2, minimum[0]/2), xycoords='data', xytext=(center[1]/3, center[0]/3), textcoords='data',
        #              arrowprops=dict(arrowstyle="-", ec='white',connectionstyle="arc3"), )

        plt.title(image.shape)
        plt.imshow(image, cmap='gray')
        #plt.show()
        save_path = 'HCdata/Challenge/paras/'
        #plt.savefig(save_path + str(k) + '_para' + ".png")
        #print("center (x,y)---axis_a(x,y)---axis_b(x,y)")
        print(minimum[0])#center[1],center[0],maximum[1], maximum[0],minimum[1], minimum[0]

#HC_para()

def PixelCount():
    img = cv2.imread('HCdata/gt_ori/000_HC.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    BKG = 0
    HEAD = 255

    pixel_count_BKG = (img == BKG).sum()
    pixel_count_HEAD = (img == HEAD).sum()

    print('The number of pixel_count_BKG is: ', pixel_count_BKG)
    print('The number of pixel_count_HEAD is: ', pixel_count_HEAD)

    cv2.namedWindow("opencv")
    cv2.imshow("opencv", img)
    cv2.waitKey(0)
#PixelCount()
def Area():
    img = cv2.imread('HCdata/gt_ori/000_HC.png')
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(img, 80, 80 * 2)
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)#只检测外围轮廓
    (cx, cy), (a, b), angle = cv2.fitEllipse(contours[0])
    print('The length of axis a,b:',a,b)

#Area()
def BatchPixelCount():
    BKG = 0
    HEAD = 255
    for item in dirs:
        #print(item) # already sorted
        if os.path.isfile(path + item):
            img = cv2.imread(path + item)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            pixel_count_BKG = (img == BKG).sum()
            pixel_count_HEAD = (img == HEAD).sum()
            print(pixel_count_HEAD)


path='HCdata/gt_ori/'
dirs = os.listdir(path)
BatchPixelCount()
