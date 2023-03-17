from numpy import *
import numpy
import maxflow
from PIL import Image
from matplotlib import pyplot as plt
from pylab import *
import cv2

#The function implements graph cut by partitioning a directed graph into two disjoint sets, foreground and background...
def graph(file, # input image
k, # kappa value --> similar pixels have weight close to kappa
s, # Sigma value --> determines how fast the values decay towards zero with increasing dissimilarity.
fore, # foreground area ---> should be input by the user manually.
back): # background area ---> should be input by the user manually.
    I = (Image.open(file).convert('L')) # read image
    If = I.crop(fore) # take a part of the foreground
    Ib = I.crop(back) # take a part of the background
    I,If,Ib = array(I),array(If),array(Ib) # convert all the images to arrays to calculation
    Ifmean,Ibmean = mean(cv2.calcHist([If],[0],None,[256],[0,256])),mean(cv2.calcHist([Ib],[0],None,[256],[0,256])) #Taking the mean of the histogram
    F,B =  ones(shape = I.shape),ones(shape = I.shape) #initalizing the foreground/background probability vector
    Im = I.reshape(-1,1) #Coverting the image array to a vector for ease.
    m,n = I.shape[0],I.shape[1]# copy the size
    g,pic = maxflow.Graph[int](m,n),maxflow.Graph[int]() # define the graph
    structure = np.array([[inf, 0, 0],
                          [inf, 0, 0],
                          [inf, 0, 0]
                         ]) # initializing the structure....
    source,sink,J = m*n,m*n+1,I # Defining the Source and Sink (terminal)nodes.
    nodes,nodeids = g.add_nodes(m*n),pic.add_grid_nodes(J.shape) # Adding non-nodes
    pic.add_grid_edges(nodeids,0),pic.add_grid_tedges(nodeids, J, 255-J)
    gr = pic.maxflow()
    IOut = pic.get_grid_segments(nodeids)
    for i in range(I.shape[0]): # Defining the Probability function....
        for j in range(I.shape[1]):
            F[i,j] = -log(abs(I[i,j] - Ifmean)/(abs(I[i,j] - Ifmean)+abs(I[i,j] - Ibmean))) # Probability of a pixel being foreground
            B[i,j] = -log(abs(I[i,j] - Ibmean)/(abs(I[i,j] - Ibmean)+abs(I[i,j] - Ifmean))) # Probability of a pixel being background
    F,B = F.reshape(-1,1),B.reshape(-1,1) # convertingb  to column vector for ease
    for i in range(Im.shape[0]):
        Im[i] = Im[i] / linalg.norm(Im[i]) # normalizing the input image vector
    w = structure # defining the weight
    for i in range(m*n):#checking the 4-neighborhood pixels
        ws=(F[i]/(F[i]+B[i])) # source weight
        wt=(B[i]/(F[i]+B[i])) # sink weight
        g.add_tedge(i,ws[0],wt) # edges between pixels and terminal
        if i%n != 0: # for left pixels
            w = k*exp(-(abs(Im[i]-Im[i-1])**2)/s) # the cost function for two pixels
            g.add_edge(i,i-1,w[0],k-w[0]) # edges between two pixels
            '''Explaination of the likelihood function: * used Bayes’ theorem for conditional probabilities
            * The function is constructed by multiplying the individual conditional probabilities of a pixel being either 
            foreground or background in order to get the total probability. Then the class with highest probability is selected.
            * for a pixel i in the image:
                               * weight from sink to i:
                               probabilty of i being background/sum of probabilities
                               * weight from source to i:
                               probabilty of i being foreground/sum of probabilities
                               * weight from i to a 4-neighbourhood pixel:
                                K * e−|Ii−Ij |2 / s
                                 where k and s are parameters that determine hwo close the neighboring pixels are how fast the values
                                 decay towards zero with increasing dissimilarity
            '''
        if (i+1)%n != 0: # for right pixels
            w = k*exp(-(abs(Im[i]-Im[i+1])**2)/s)
            g.add_edge(i,i+1,w[0],k-w[0]) # edges between two pixels
        if i//n != 0: # for top pixels
            w = k*exp(-(abs(Im[i]-Im[i-n])**2)/s)
            g.add_edge(i,i-n,w[0],k-w[0]) # edges between two pixels
        if i//n != m-1: # for bottom pixels
            w = k*exp(-(abs(Im[i]-Im[i+n])**2)/s)
            g.add_edge(i,i+n,w[0],k-w[0]) # edges between two pixels
    I = array(Image.open(file)) # calling the input image again to ensure proper pixel intensities....
    print ("The maximum flow for %s is %d"%(file,gr) )# find and print the maxflow
    Iout = ones(shape = nodes.shape)
    for i in range(len(nodes)):
        Iout[i] = g.get_segment(nodes[i]) # calssifying each pixel as either forground or background
    out = 255*ones((I.shape[0],I.shape[1],3)) # initialization for 3d input
    for i in range(I.shape[0]):
        for j in range(I.shape[1]): # converting the True/False to Pixel intensity
            if IOut[i,j]==False:
                if len(I.shape) == 2:
                    out[i,j,0],out[i,j,1],out[i,j,2] = I[i,j],I[i,j],I[i,j] # foreground for 2d image
                if len(I.shape) == 3:
                    out[i,j,0],out[i,j,1],out[i,j,2] = I[i,j,0],I[i,j,1],I[i,j,2] # foreground for 3d image
            else:
                out[i,j,0],out[i,j,1],out[i,j,2] = 1,255,255 # red background
    figure()
    plt.imshow(out,vmin=0,vmax=255) # plot the output image
    plt.show()

graph('input1.jpg',2,100,(225,142,279,185),(7,120,61,163)) #calling the maxflow funtion for input1
graph('input2.jpg',2,120,(148,105,201,165),(11,12,80,52)) #calling the maxflow funtion for input2
