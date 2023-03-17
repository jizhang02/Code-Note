#Auther:ZHANG Jing
#Email address:jing.zhang@insa-rouen.fr
#Date:2018-11-21
#Title:performing Laplacian-gauss operator algorithm to segmentate a image
#Usage:right clicked the mouse to run the code

import scipy.ndimage as nd
import scipy.misc
from scipy.misc import pilutil

a = pilutil.Image.open('data/verbe_axial.png').convert('L')
a = scipy.misc.fromimage(a)
LoG = nd.gaussian_laplace(a, 2)
b = scipy.misc.toimage(LoG)
b.save('LoG.png')
b.show()