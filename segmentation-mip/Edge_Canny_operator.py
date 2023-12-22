#Auther:ZHANG Jing
#Email address:jing.zhang@insa-rouen.fr
#Date:2018-11-21
#Title:performing Canny filter to segmentate a image
#Usage:right clicked the mouse to run the code

import numpy as np
import scipy.misc
from scipy.misc import pilutil
from skimage import feature

a = pilutil.Image.open('data/verbe_axial.png').convert('L')
a = scipy.misc.fromimage(a)
b = feature.canny(a,sigma=1)
print(b)
out = np.uint8(feature.canny(a, sigma=3, ) * 255)
print(out)
pilutil.Image.fromarray(out, mode='L')
# b is converted from an ndarray to an image
b = scipy.misc.toimage(out)
b.save('canny.png')
b.show()