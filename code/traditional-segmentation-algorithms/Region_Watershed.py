#Auther:ZHANG Jing
#Email address:jing.zhang@insa-rouen.fr
#Date:2018-11-21
#Title:performing Watershed algorithm to segmentate a image
#Usage:right clicked the mouse to run the code

import numpy as np
import cv2
import scipy
from scipy.ndimage import label

a = cv2.imread('data/verbe_axial.png')
# covnerting image from color to grayscale
a1 = cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
# thresholding the image to obtain cell pixels
thresh,b1 = cv2.threshold(a1,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# since Otsu's method has over segmented the image
# erosion operation is performed
b2 = cv2.erode(b1,None,iterations=2)
# distance transform is performed
dist_trans = cv2.distanceTransform(b2,2,3)
# thresholding the distance transform image to obtain
# pixels that are foreground
thresh,dt = cv2.threshold(dist_trans,1,255,cv2.THRESH_BINARY)
# performing labeling
labelled,ncc = label(dt)
# labelled is converted to 32-bit integer
labelled = labelled.astype(np.int32)
# performing watershed
cv2.watershed(a,labelled)
dt1 = scipy.misc.toimage(labelled)
dt1.save('watershed.png')
dt1.show()
