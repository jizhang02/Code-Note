'''
-----------------------------------------------
File Name: t-SNE-cardiac$
Description: t-SNE example for cardiac classes
Author: Jing$
Date: 11/30/2021$
-----------------------------------------------
'''

print(__doc__)
from time import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import offsetbox
from sklearn import datasets, manifold
from data_volume import *
root = 'C:/Users/Jing/Desktop/PycharmProjects/CardiacVGG/'
img_aug = root +'ACDC_3D_multi_slice/dataset9_aug/img_aug/'
img_ori = root +'ACDC_3D_multi_slice/dataset9_aug/img_ori/'
csv_aug = root +'ACDC_3D_multi_slice/dataset9_aug/ACDC_aug.csv'
csv_ori = root +'ACDC_3D_multi_slice/dataset9_aug/ACDC_ori.csv'
H = 100
W = 100
slice = 9

X_aug,Y_aug,psxy_aug,psz_aug, \
X_ori,Y_ori,psxy_ori,psz_ori  = load_data_multislice(img_aug,img_ori,csv_aug,csv_ori,H,W,slice)
X = Y_ori#X_ori # Y_ori load cardiac image or cardiac volume value
Y = np.full((182,3), [1,2,3])# RV, MYO, LV

#n_samples, n_features = X.shape
print('shape of X, Y', np.asarray(X.shape), len(Y)) #shape of X, Y [182 100 100   9] 3

def plot_embedding(X, title=None):
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    X = (X - x_min) / (x_max - x_min)

    plt.figure()
    ax = plt.subplot(111)
    for i in range(X.shape[0]):
        plt.text(X[i, 0], X[i, 1], str(Y[i][0]), color=plt.cm.Set1(Y[i][0] / 6), fontdict={'weight':'bold', 'size':9})
        plt.text(X[i, 0], X[i, 1], str(Y[i][1]), color=plt.cm.Set1(Y[i][1] / 6), fontdict={'weight':'bold', 'size':9})
        plt.text(X[i, 0], X[i, 1], str(Y[i][2]), color=plt.cm.Set1(Y[i][2] / 6), fontdict={'weight':'bold', 'size':9})

    if hasattr(offsetbox, 'AnnotationBbox'): # if offsetbox has property 'Anno...'
        shown_images = np.array([[1., 1.]])
        for i in range(X.shape[0]):
            dist = np.sum((X[i] - shown_images) ** 2, 1) #axis=1
            if np.min(dist) < 4e-3:
                continue
            shown_images = np.r_[shown_images, [X[i]]] # row-wise merging
            #imagebox = offsetbox.AnnotationBbox(offsetbox.OffsetImage(digits.images[i], cmap=plt.cm.gray_r), X[i])
            #ax.add_artist(imagebox)
    plt.xticks([])
    plt.yticks([])
    if title is not None:
        plt.title(title)
    plt.show()

# plot images of the cardiac slice
def plot_images(X):
    n_img_per_row = 3
    img = np.zeros((100 * n_img_per_row, 100 * n_img_per_row))
    for i in range(n_img_per_row):
        ix = 10 * i + 1
        for j in range(n_img_per_row):
            iy = 10 * j + 1
            img[ix:ix + 100, iy:iy + 100] = X[i * n_img_per_row + j,:,:,0].reshape((100, 100))

    plt.imshow(img, cmap=plt.cm.binary)
    plt.xticks([])
    plt.yticks([])
    plt.title('A selection from the cardiac slice')
    plt.show()

#plot_images(X)

def plot_label(X):
    n_img_per_row = 10
    img = np.zeros((10 * n_img_per_row, 10 * n_img_per_row))
    for i in range(n_img_per_row):
        ix = 10 * i + 1
        for j in range(n_img_per_row):
            iy = 10 * j + 1
            plt.text(ix + 10, iy + 10, str(X[i][0]), color='green', fontdict={'weight':'bold', 'size':9})
            plt.text(ix + 10, iy + 10, str(X[i][1]), color='red', fontdict={'weight':'bold', 'size':9})
            plt.text(ix + 10, iy + 10, str(X[i][2]), color='blue', fontdict={'weight':'bold', 'size':9})

    plt.imshow(img, cmap=plt.cm.binary)
    plt.xticks([])
    plt.yticks([])
    plt.title('A selection from the cardiac label')
    plt.show()
plot_label(X)

def tsne(X):
    # t-SNE embedding of the digits dataset
    print("Computing t-SNE enbedding")
    tsne = manifold.TSNE(n_components=2, perplexity=10.0,
                     early_exaggeration=12.0, learning_rate=200.0, n_iter=1000,
                     n_iter_without_progress=300, min_grad_norm=1e-7,
                     metric="euclidean", init="random", verbose=0,
                     random_state=None, method='barnes_hut', angle=0.5)
    t0 = time()
    #X = X.reshape(182,90000)# cardiac slice for image
    X_tsne = tsne.fit_transform(X)#  182,3
    plot_embedding(X_tsne, "t-SNE embedding of the cardiac (time %.2fs)" % (time() - t0))

tsne(X)