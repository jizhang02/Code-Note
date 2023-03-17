#Auther:ZHANG Jing
#Email address:jing.zhang@insa-rouen.fr
#Date:2018-11-23
#Title:performing GraphCut method to segmentate a image
#Usage:right clicked the mouse to run the code
#url:https://github.com/erichardin/graph-cut-segmentation

import os
from PIL import Image
import maxflow
from numpy import array,asarray,median,exp,zeros,ones
import matplotlib.pyplot as plt
from numpy import mean,std


plt.ion()

do_plots = True

# image is an image as a numpy array
# mask is a single band logical array that is the same size as image
# mean and standard deviation will be calculated from the image according to the non-zero areas in the mask
def GetMeanAndStd(image,mask):
    image_masked = image[mask]
    mu = array([ mean(band) for band in image_masked.T ])
    sigma = array([ std(band) for band in image_masked.T ])
    return [mu,sigma]

im_original = Image.open('data/original2_v1.jpg')
im_marked = Image.open('data/marked2_v2.jpg')

# reduce image sizes
p = 0.5
new_size = (int(p*im_original.size[0]),int(p*im_original.size[1]))
im_original = im_original.resize(new_size, Image.ANTIALIAS)
im_marked = im_marked.resize(new_size, Image.ANTIALIAS)
# 

arr_original = asarray(im_original)
arr_marked = asarray(im_marked) # supposedly asarray is read only, whereas array(im) will make a copy

# fg indicates foreground and bg indicates background
fg_color = (255,0,255)
bg_color = (0,255,0)
eps = 3 # just a little buffer to help extract the markup/annotation
fg_mask = (arr_marked[:,:,0] > fg_color[0]-eps)*(arr_marked[:,:,1] < fg_color[1]+eps)*(arr_marked[:,:,2] > fg_color[2]-eps)
bg_mask = (arr_marked[:,:,0] < bg_color[0]-eps)*(arr_marked[:,:,1] > bg_color[0]+eps)*(arr_marked[:,:,2] < bg_color[0]-eps)

R = arr_original[:,:,0]
G = arr_original[:,:,1]
B = arr_original[:,:,2]

# compute energies, which are simple gaussian wells, could be more complicated though. 
[mu_fg, sigma_fg] = GetMeanAndStd(arr_original,fg_mask)
E_data_fg = 1-exp(-((R-mu_fg[0])**2/(2*sigma_fg[0]**2)+(G-mu_fg[1])**2/(2*sigma_fg[1]**2)+(B-mu_fg[2])**2/(2*sigma_fg[2]**2)))

if do_plots:
    plt.figure()
    plt.imshow(E_data_fg)
    #plt.colorbar()
    plt.axis('off')
    plt.savefig('graphcub_fb_energy.jpg')

[mu_bg, sigma_bg] = GetMeanAndStd(arr_original,bg_mask)
E_data_bg = 1-exp(-((R-mu_bg[0])**2/(2*sigma_bg[0]**2)+(G-mu_bg[1])**2/(2*sigma_bg[1]**2)+(B-mu_bg[2])**2/(2*sigma_bg[2]**2)))
if do_plots:
    plt.figure()
    plt.imshow(E_data_bg)
    #plt.colorbar()
    plt.axis('off')
    plt.savefig('graph_bg_energy.jpg')

# Segment the image by minimizing the energy via graph cut
# http://pmneila.github.io/PyMaxflow/tutorial.html#a-first-example
image_shape = arr_original[:,:,1].shape
g = maxflow.Graph[float]() 
nodeids = g.add_grid_nodes(image_shape)
# structure specifies second order clique
structure = array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
alpha = 1 # controls the strength of feature coherence
weights = alpha/float(sum(structure.flatten()))*ones(image_shape)
g.add_grid_edges(nodeids, weights, structure=structure, symmetric=False)
g.add_grid_tedges(nodeids, E_data_fg, E_data_bg)

g.maxflow()
sgm = g.get_grid_segments(nodeids)

########
if do_plots:
    greyscale = mean(arr_original,2)
    plt.figure()
    plt.imshow(greyscale, cmap=plt.get_cmap('gray'))
    plt.imshow(sgm, alpha=0.5)
    plt.axis('off')
    plt.savefig('graphcut.jpg')