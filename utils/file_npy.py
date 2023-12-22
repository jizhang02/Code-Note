'''
-----------------------------------------------
File Name: file_npy.py
Description: npy file reading and writing.
Author: Jing (zhangjingnm@hotmail.com)
Date: 7/5/2021
-----------------------------------------------
'''

import numpy as np
import random
import math

def randomNums(a, b, n):
    all = list(range(a, b))
    res = []

    while n:
        index = math.floor(random.random() * len(all))
        res.append(all[index])
        del all[index]
        n -= 1
    return res


# t1 = sorted(randomNums(0,120,120))
# t2 = sorted(randomNums(20,140,120))
# t3 = sorted(randomNums(40,160,120))
# t4 = sorted(randomNums(60,180,120))
# t5 = sorted(randomNums(80,200,120))
v1 = sorted(randomNums(121,170,40))
v2 = sorted(randomNums(141,190,40))
v3 = sorted(randomNums(161,200,30))
v3s = sorted(randomNums(0,20,10))
vs = np.append(v3s,v3)
print(vs)
v4 = sorted(randomNums(181,200,10))
v4s = sorted(randomNums(0,59,30))
vs4 = np.concatenate((v4s,v4))
print(vs4)
v5 = sorted(randomNums(0,80,40))
print(v1)
print(v2)
print(v3)
print(v4)
print(v5)
np.save('valid1.npy',v1)
np.save('valid2.npy',v2)
np.save('valid3.npy',vs)
np.save('valid4.npy',vs4)
np.save('valid5.npy',v5)

#a=np.arange(5,15)
#print(a)
#np.save('test.npy',a)
a=np.load('valid3.npy')

print(len(a))