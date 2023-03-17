#Auther:ZHANG Jing
#Email address:jing.zhang@insa-rouen.fr
#Date:2018-11-21
#Title:performing Otsu method to segmentate a image
#Usage:right clicked the mouse to run the code

import numpy as np
import scipy.misc
from skimage.filters.thresholding import threshold_otsu
from scipy.misc import pilutil

im = pilutil.Image.open('data/verbe_axial.png').convert('L')
im = scipy.misc.fromimage(im)
#performing Otsu's thresholding
thresh = threshold_otsu(im)
#pixels with intensity greater than threshold are kept
b = im>thresh
b = np.uint8(b)*255
print(b)
b = scipy.misc.toimage(b)
b.save('Otsu.png')
b.show()