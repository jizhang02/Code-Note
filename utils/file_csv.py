'''
-----------------------------------------------
File Name: file_csv.py
Description: 
Author: Jing (zhangjingnm@hotmail.com)
Date: 7/5/2021
-----------------------------------------------
'''

from tqdm import tqdm # progress bar
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageChops
import pandas as pd
import math
import glob
import os

def angle(a, b, c):
  """
  Return angle between lines ab, bc
  """
  ab = a - b
  cb = c - b
  return math.acos(np.dot(ab,cb) / (np.linalg.norm(ab) * np.linalg.norm(cb)))

df = pd.read_csv('data/training_set3996_256_256/train_annotation3996_256.csv')
df = df.assign(center_x = 0.000000000, center_y = 0.000000000, semi_axe_a = 0.000000000, semi_axe_b = 0.0000000000, angle = 0.0)

labels_path = 'data/training_set3996_256_256/label/'
dirs = os.listdir(labels_path)
print(len(dirs))
for k in range(len(dirs)):
    #img = plt.imread(labels_path+dirs[k])
    img = Image.open(labels_path+dirs[k]).convert("L")
    img = np.array(img)
    print(np.max(img))
    xs, ys = np.where(img >= 1)
    center = [np.mean(xs), np.mean(ys)]
    df['filename'][k] = (dirs[k])
    df['center_x'][k] = center[1]
    df['center_y'][k] = center[0]
    points = np.hstack((xs.reshape(-1, 1), ys.reshape(-1, 1)))
    maximum = points[np.argmax(np.linalg.norm(center - points, axis=1))]
    df['semi_axe_a'][k] = np.max(np.linalg.norm(center - points, axis=1))
    minimum = points[np.argmin(np.linalg.norm(center - points, axis=1))]
    df['semi_axe_b'][k] = np.min(np.linalg.norm(center - points, axis=1))
    df['angle'][k] = angle([df['center_x'][k], 0], df['semi_axe_b'][k], [df['center_x'][k], df['center_y'][k]])
    print(k)

df.to_csv('data/training_set3996_256_256/train_annotation3996_256.csv', columns=['filename','center_x','center_y','semi_axe_a','semi_axe_b','angle'],index=0)
