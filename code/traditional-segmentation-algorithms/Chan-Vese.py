import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from skimage.color import rgb2gray
from skimage.segmentation import chan_vese
import scipy.misc

imgin = plt.imread('data/orig1.jpg')
image = rgb2gray(imgin)
print(image.shape)
#image = img_as_float(data.camera())
# Feel free to play around with the parameters to see how they impact the result
cv = chan_vese(image, mu=0.25, lambda1=0.10, lambda2=0.10, tol=1e-3, max_iter=200,
               dt=0.5, init_level_set="checkerboard", extended_output=True)
out = np.uint8(cv[0]*255)
imgout = Image.fromarray(out)
img = scipy.misc.toimage(imgout)
img.save('levelset-lamda0.10.1.png')
img.show()



