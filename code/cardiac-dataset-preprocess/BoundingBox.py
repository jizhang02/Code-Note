'''
Title: Finding the biggest bounding box among many images,
the bounding box is done by edge detection.
Author: Jing Zhang
Date: 2020-04-23
'''
import cv2
import numpy as np
import glob, os
def boundingbox(src):
    src = cv2.imread(src)
    #contours = cv2.findContours(src, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contours = cv2.Canny(src,30,100)
    x, y, w, h = cv2.boundingRect(contours)

    print(x,y,w,h)
    cv2.rectangle(src, (x, y), (x + w, y + h), (100,10,200), 1, 8, 0)
    cv2.imshow('bb',src)
    #cv2.waitKey(0)
    return x,y,w,h

path = 'ACDC_2D/ED/gt/'
def FindCord():
    imagelist = sorted(glob.glob(os.path.join(path, '*.png')))
    min_x1 = 100
    min_y1 = 100
    max_x2 = 100
    max_y2 = 100
    for i in range(len(imagelist)):
        x,y,w,h = boundingbox(imagelist[i])
        max_xw = x+w
        max_yh = y+h
        if(x<min_x1&x!=0): min_x1 = x
        if(y<min_y1&y!=0):min_y1 = y
        if(max_xw>max_x2):max_x2 = max_xw
        if(max_yh>max_y2):max_y2 = max_yh
    print('the biggest boundingbox:',min_x1,min_y1,max_x2,max_y2)
FindCord()