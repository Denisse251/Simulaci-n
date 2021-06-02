# -*- coding: utf-8 -*-
"""
Created on Tue May 31 20:51:53 2021

@author: denis
"""

import pandas as pd 
import matplotlib.pyplot as plt
from math import floor, log
from random import random, uniform
 
l = 10
nc = 10
rc = (10*0.05)/2
na = 50
ra = (10*0.03)/2
nt = 2
rt = (10*0.5)/2
v = l / 30
pc = 0.25

tmax = 100
digitos = floor(log(tmax, 10)) + 1
c = {'C1': 'firebrick', 'C2': 'r', 'CA': 'g', 'CB': 'orange', 'T': 'b'}
m = {'C1': 'o', 'C2': 'o', 'CA': 'o', 'CB': 'o', 'T': 'o'}
capsula =  pd.DataFrame()
capsula['x'] = [uniform((0+rc), (l-rc)) for i in range(nc)]
capsula['y'] = [uniform((9+rc), (l-rc)) for i in range(nc)]
capsula['dx'] = [uniform(-v, v) for i in range(nc)]
capsula['dy'] = [uniform(-v, v) for i in range(nc)]
capsula['estado'] = ['C1' for i in range(nc)]
epidemia = []

cel = pd.DataFrame()
cel['x'] = [uniform((0+ra), (l-ra)) for i in range(na)]
cel['y'] = [uniform((0+ra), (9-ra)) for i in range(na)]
cel['dx'] = [uniform(-v, v) for i in range(na)]
cel['dy'] = [uniform(-v, v) for i in range(na)]
cel['estado'] = ['CB' if random() <= pc else 'CA' for i in range(na)]

# temp = pd.DataFrame()
# temp['x'] = [uniform((0+rt), (l-rt)) for i in range(nt)]
# temp['y'] = [uniform((0+rt), (9-rt)) for i in range(nt)]
# temp['estado'] = ['T' for i in range(nt)]

for i in range(na):
    celula = cel.iloc[i]
    
# print(temp['x'])
# print(temp['x'][0])
# print(temp['x'][1])
ph = pd.DataFrame()

at = 300000
a = at*0.5
l1 = [x-0.5 for x in range(1,11)]
l2 = [9.5]*10
fig = plt.figure(figsize=(9.9,10.15), dpi = 300)
ax = plt.subplot(1, 1, 1)
plt.xlim(0, l)
plt.ylim(0, l)
ax.plot([0,10],[9.5,9.5],linewidth=(550*0.1), c='orange', alpha = 0.5)
for e, d in capsula.groupby('estado'):
    if len(d) > 0:
        ax.scatter(d.x, d.y, c = c[e], marker = m[e], s = ((550*0.05))**2, alpha = 0.8)

for e, d in cel.groupby('estado'):
    if len(d) > 0:
        ax.scatter(d.x, d.y, c = c[e], marker = m[e], s = ((550*0.03))**2, alpha = 0.8)
        
# for e, d in temp.groupby('estado'):
#     if len(d) > 0:
#         ax.scatter(d.x, d.y, c = c[e], marker = m[e], s = ((550*0.5))**2, alpha = 0.3)
        
plt.show()
plt.close()


