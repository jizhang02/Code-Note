import skimage.io as io
from keras.utils import to_categorical
from os.path import join
import numpy as np


def load_camus(path, data_range, size=(256, 256)):
    """Returns images and masks to use in a classic keras generator"""

    x = []
    y = []

    print("Loading images from .png files ... ")

    for ind in data_range:
        for moment in ['ED', 'ES']:

            filename = str(ind) + '_' + moment

            # load images
            image_path = join(path, 'images')
            us_image = io.imread(join(image_path, filename) + '.png')

            # load masks
            mask_path = join(path, 'masks')
            mask = io.imread(join(mask_path, filename) + '.png')

            # put in the right format
            if np.max(us_image) > 1:
                us_image = us_image / np.max(us_image) * 1.0

            if np.max(mask) > 3:
                mask = (mask / 255 * 3).astype('int')

            # resize to the right size
            us_image = np.reshape(us_image, size +(1,))
            mask.reshape(size)
            mask = to_categorical(mask)

            x.append(us_image)
            y.append(mask)

    x = np.array(x, dtype='float32')
    y = np.array(y, dtype='float32')

    print(" Done ! ")

    return x, y


