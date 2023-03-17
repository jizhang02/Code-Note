#Auther:ZHANG Jing
#Email address:jing.zhang@insa-rouen.fr
#Date:2018-11-28
#Title:performing snake to segmentate a image
#Usage:right clicked the mouse to run the code

import scipy.misc
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import data
from skimage.filters import gaussian
from skimage.segmentation import active_contour
from scipy.misc import pilutil

img = pilutil.Image.open('data/verbe_axial.png').convert('L')
#img = data.astronaut()
#img = rgb2gray(img)
img = scipy.misc.fromimage(img)

s = np.linspace(0, 2*np.pi, 400)
x = 220 + 100*np.cos(s)
y = 200 + 100*np.sin(s)
init = np.array([x, y]).T

snake = active_contour(gaussian(img, 3),init, alpha=0.015, beta=10, gamma=0.001)
print(snake)
b = scipy.misc.toimage(snake)
#b.save('snakemodel.png')
b.show()

fig, ax = plt.subplots(figsize=(7, 7))
ax.imshow(img, cmap=plt.cm.gray)
ax.plot(init[:, 0], init[:, 1], '--r', lw=3)
ax.plot(snake[:, 0], snake[:, 1], '-b', lw=3)
ax.set_xticks([]), ax.set_yticks([])
ax.axis([0, img.shape[1], img.shape[0], 0])

