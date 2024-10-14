import numpy as np
import tqdm
from tqdm import tnrange
import medpy
from medpy.metric.binary import dc, hd, assd
import keras
from keras.utils import to_categorical
from os.path import join
import PIL
from PIL import Image
from scipy.ndimage import binary_fill_holes
from skimage.measure import regionprops, label
import matplotlib.pyplot as plt
from scipy.misc import imresize


def post_process(seg):
    """Keep only the largest predicted structure of seg"""

    # fill holes
    seg = binary_fill_holes(seg)

    ## keep largest structure to remove false positive
    region_properties = regionprops(label(seg.astype('uint8')))

    # Find the area of largest region
    max_area = 0
    for region in region_properties:
        if region.area > max_area:
            max_area = region.area

    # Remove any regions not belonging to max region
    for region in region_properties:
        if region.area < max_area:
            for point in region.coords:
                seg[point[0], point[1]] = False

    return seg


def get_geometrical_results(model, data, groundtruths, path, inds, use_pp):
    """Compute Dices, Hausdorff distances and ASSDs between the model predictions on the inds indices of data and the groundtruths
       use_pp enables to use post-processing on the predictions. The original image sizes are stored in inds"""

    # Get predictions from the input data
    segmentations = model.predict(data, verbose=1)
    predictions = np.argmax(segmentations, axis=-1)

    voxel_spacing = [0.154, 0.308]

    nb_im = predictions.shape[0]
    nb_struct = groundtruths.shape[-1] - 1
    results = np.zeros((nb_im, nb_struct, 3), dtype=np.float)

    size_file = open(join(path, 'ori_sizes.txt'), 'r')
    sizes = size_file.readlines()

    # get image indices
    indices = []
    for ind in inds:
        indices.append(ind*2)
        indices.append(ind*2+1)

    for im in tnrange(nb_im, desc="Evaluation on each image"):

        # Reshape the prediction as a binary class matrix
        pred_cat = keras.utils.to_categorical(predictions[im, :, :], num_classes=4)

        # get original size from the relative indexing
        line = sizes[indices[im] - 600]
        ori_size = [int(line.split()[2][1:-1]), int(line.split()[3][0:-1])]

        for struct in range(1, nb_struct+1):

            # Extract the structure channel
            pred = pred_cat[:, :, struct]
            gt = groundtruths[im, :, :, struct]

            # Resize to the original size
            pred = np.array(Image.fromarray(pred).resize((ori_size[1], ori_size[0]), PIL.Image.NEAREST)).astype('uint8') #Image.resize inverts dimensions
            gt = np.array(Image.fromarray(gt).resize((ori_size[1], ori_size[0]), PIL.Image.NEAREST)).astype('uint8')

            # Transform into boolean array
            pred = (pred == 1)
            gt = (gt == 1)

            # Apply postprocessing
            if use_pp:
                pred = post_process(pred)

            #  Compute geometrical metrics using the medpy library
            dice = dc(pred, gt)
            if np.sum(pred) > 0:  # If the structure is predicted on at least one pixel
                hausdorff = hd(pred, gt, voxelspacing=[voxel_spacing[0], voxel_spacing[1]])
                asd = assd(pred, gt, voxelspacing=[voxel_spacing[0], voxel_spacing[1]])
            else:
                print("on image ", nb_im, "the structure ", struct, " was not associated to any pixel")
                hausdorff = 'nan'
                asd = 'nan'

            results[im, struct-1, :] = [dice, hausdorff, asd]

    return results, segmentations


def display_mean_values_of_metrics(res, metrics, structs):
    """Displays the average values of the metrics with results in res for the structures structs"""

    # Display average results
    mean_perf = np.nanmean(res, axis=0)
    print('Metric', metrics)
    for ind, struct in enumerate(structs):
        print(struct, ': ', np.around(mean_perf[ind, :], 2))


def display_histogram_of_metrics(res, metrics, structs):
    """Displays the histograms of the metrics with results in res for the structures structs"""

    plt.figure(figsize=(10, 3), dpi=200)
    for i, metric in enumerate(metrics):
        plt.subplot(1, 3, i + 1)
        plt.title(metric)
        plt.hist(res[:, :, i], label=structs, range=[0, np.nanmax(res[:, :, i])])
        plt.legend()
    plt.show()
