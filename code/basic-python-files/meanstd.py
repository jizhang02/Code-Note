import numpy as np
from PIL import Image,ImageChops
import os, sys
import numpy as np
import cv2
loss=[15.453547089543175,
      8.882177379263107,
      9.188037982538118,
      9.135677316080985,
       ]
acc = [407.1783247904562,153.60155003993356,
       181.016714393194,142.3610346041732,]
#iou = [0.784,0.822,0.833]
print('%.3f'%np.mean(loss),'%.2f'%np.std(loss))
print('%.3f'%np.mean(acc),'%.2f'%np.std(acc))
#('%.3f'%np.mean(iou),'%.2f'%np.std(iou))

def normalization(path):
    img = Image.open(path)#.convert('RGB')
    img_mean = np.mean(img)
    img_std = np.std(img)
    img = Image.open(path)#.convert('RGB')
    img = np.array(img)
    print(np.max(img))
    print(np.min(img))

    img_norm = (1 / img_std) * (img - img_mean)#first method
    #img_norm = (img-np.min(img))/(np.max(img)-np.min(img))# second method
    print(np.max(img_norm))
    print(np.min(img_norm))

    #imResize = Image.fromarray(img_norm.astype('uint8'),'RGB') # normalization, u=0, std=1, labels don't need to do this
    #imResize.save("%d.png", quality=90)
    #return img_norm
path='data/training_set999_800_540/label/000_HC_Annotation.png'

def count(path):
    img = Image.open(path)  # .convert('RGB')
    img = np.array(img)
    print(np.shape(img))
    print (np.max(img))
    print(len(img[img==255]))
    #whiteixel_count = len(img[g])
    #print(whiteixel_count)
count(path)
#normalization(path)