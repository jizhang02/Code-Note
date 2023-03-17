# python 2
#coding=utf-8
import datetime
import os
import h5py
import numpy as np

f = h5py.File('data/brats_data.h5','r')
f.keys() #可以查看所有的主键
print([key for key in f.keys()])
print('first, we get values of x:', f['affine'][:])
print('then, we get values of y:', f['data'][:])
print(f['affine'][:].shape)
print(f['data'][:].shape)



