import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.filters import gaussian
from skimage.segmentation import active_contour

img = plt.imread('data/orig1.jpg')
img = rgb2gray(img)
print(img.shape)
s = np.linspace(0, 2*np.pi, 400)
x = 255 + 225*np.cos(s)
y = 220 + 225*np.sin(s)
init = np.array([x, y]).T

snake = active_contour(gaussian(img, 3), init, alpha=0.013, beta=0.51, gamma=0.02,max_iterations=3000)

fig, ax = plt.subplots(figsize=(7, 7))
ax.imshow(img, cmap=plt.cm.gray)
ax.plot(init[:, 0], init[:, 1], '--r', lw=3)
ax.plot(snake[:, 0], snake[:, 1], '-b', lw=3)
ax.set_xticks([]), ax.set_yticks([])
ax.axis([0, img.shape[1], img.shape[0], 0])
plt.savefig('snake-iter-3000.png')
plt.show()
