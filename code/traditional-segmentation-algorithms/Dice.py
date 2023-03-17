# Auther:ZHANG Jing
# Email address:jing.zhang@insa-rouen.fr
# Date:2018-11-26
# Title:using DICE function to evaluate results and ground truth image
# Usage:jpg,png have different dimension

import numpy as np
import scipy.ndimage
from scipy.misc.pilutil import Image

# dice coefficient 2nt/na + nb.
def dice_coefficient(a, b):
    a_bigrams = set(a)
    b_bigrams = set(b)
    overlap = len(a_bigrams & b_bigrams)
    return overlap * 2.0/(len(a_bigrams) + len(b_bigrams))

a = [0,2,3,4,5,7,8,9,4,5,6,1,2,3]
b = [0,2,3,4,8,9,4,5,6,1,2,3]
print(dice_coefficient(a,b))

im1 = Image.open('/home/jing/Desktop/imgseg/data/contour_axial.png')
im2 = Image.open('/home/jing/Desktop/imgseg/random_walk.png')

#width*height*channel*alpha for png
#width*height*channel for jpg
size1 = im1.size[0]*im1.size[1]*4
size2 = im2.size[0]*im2.size[1]#why???

arr1 = scipy.misc.fromimage(im1).reshape(size1)
arr2 = scipy.misc.fromimage(im2).reshape(size2)

print(dice_coefficient(arr1,arr2))