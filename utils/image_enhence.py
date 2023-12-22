'''
-----------------------------------------------
File Name: image_enhence.py
Description: Different image enhence methods.
Author: Jing (zhangjingnm@hotmail.com)
Date: 7/5/2021
-----------------------------------------------
'''
import numpy as np
import cv2

def replaceZeroes(data):
    min_nonzero = min(data[np.nonzero(data)])
    data[data == 0] = min_nonzero
    return data

def SSR(src_img, size):
# Structure Similarity Region
    L_blur = cv2.GaussianBlur(src_img, (size, size), 0)
    img = replaceZeroes(src_img)
    L_blur = replaceZeroes(L_blur)

    dst_Img = cv2.log(img/255.0)
    dst_Lblur = cv2.log(L_blur/255.0)
    dst_IxL = cv2.multiply(dst_Img,dst_Lblur)
    log_R = cv2.subtract(dst_Img, dst_IxL)

    dst_R = cv2.normalize(log_R,None,0,255,cv2.NORM_MINMAX)
    log_uint8 = cv2.convertScaleAbs(dst_R)
    return log_uint8


def MSR(img, scales):
# Multi-scale Retinex with Color Restoration
    weight = 1 / 3.0
    h, w = img.shape[:2]
    log_R = np.zeros((h, w), dtype=np.float32)

    for i in range(len(scales)):
        img = replaceZeroes(img)
        L_blur = cv2.GaussianBlur(img, (scales[i], scales[i]), 0)
        L_blur = replaceZeroes(L_blur)
        dst_Img = cv2.log(img/255.0)
        dst_Lblur = cv2.log(L_blur/255.0)
        dst_Ixl = cv2.multiply(dst_Img, dst_Lblur)
        log_R += weight * cv2.subtract(dst_Img, dst_Ixl)

    dst_R = cv2.normalize(log_R,None, 0, 255, cv2.NORM_MINMAX)
    log_uint8 = cv2.convertScaleAbs(dst_R)
    return log_uint8


if __name__ == '__main__':
    img = './test.png'
    scales = [3,5,9]  # [3,5,9]  #看不出效果有什么差别
    src_img = cv2.imread(img)
    b_gray, g_gray, r_gray = cv2.split(src_img)
    b_gray = MSR(b_gray, scales)
    g_gray = MSR(g_gray, scales)
    r_gray = MSR(r_gray, scales)
    result = cv2.merge([b_gray, g_gray, r_gray])

    cv2.imshow('img',src_img)
    cv2.imshow('MSR_result',result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main1__':
    img = './test.png'
    size = 3
    src_img = cv2.imread(img)
    b_gray, g_gray, r_gray = cv2.split(src_img)
    b_gray = SSR(b_gray, size)
    g_gray = SSR(g_gray, size)
    r_gray = SSR(r_gray, size)
    result = cv2.merge([b_gray, g_gray, r_gray])

    cv2.imshow('img',src_img)
    cv2.imshow('result',result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
