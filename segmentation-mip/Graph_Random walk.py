#Auther:ZHANG Jing
#Email address:jing.zhang@insa-rouen.fr
#Date:2018-11-28
#Title:performing Random walk method to segmentate a image
#Usage:right clicked the mouse to run the code

import numpy as np
import matplotlib.pyplot as plt

from skimage.segmentation import random_walker
from skimage.data import binary_blobs
from skimage.exposure import rescale_intensity
import skimage
import scipy.misc
from scipy.misc import pilutil

# Generate noisy synthetic data
#data = skimage.img_as_float(binary_blobs(length=128, seed=1))
data = pilutil.Image.open('data/verbe_axial.png').convert('L')
data = scipy.misc.fromimage(data)
sigma = 0.35
#data += np.random.normal(loc=0, scale=sigma, size=data.shape)
#data = rescale_intensity(data, in_range=(-sigma, 1 + sigma),out_range=(-1, 1))

# The range of the binary image spans over (-1, 1).
# We choose the hottest and the coldest pixels as markers.
markers = np.zeros(data.shape, dtype=np.uint)
markers[data ==0] = 1
markers[data > 0.95] = 2

# Run random walker algorithm
labels = random_walker(data, markers, beta=10, mode='bf')
b = scipy.misc.toimage(labels)
b.save('random_walk.png')
b.show()

# Plot results
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(8, 3.2),sharex=True, sharey=True)
ax1.imshow(data, cmap='gray', interpolation='nearest')
ax1.axis('off')
ax1.set_title('data')
ax2.imshow(markers, cmap='magma', interpolation='nearest')
ax2.axis('off')
ax2.set_title('Markers')
ax3.imshow(labels, cmap='gray', interpolation='nearest')
ax3.axis('off')
ax3.set_title('Segmentation')

fig.tight_layout()
plt.show()