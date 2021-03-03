# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 16:01:39 2021

@author: denis
"""
import numpy as np 
import random
import matplotlib.cm as cm
import matplotlib.pyplot as plt

dim = 100
semilla = 40
num = dim**2

semill = [x for x in range(1,semilla+1)]
valores = [0 for x in range(num)]
valores[:semilla] = semill
random.shuffle(valores)
actual = np.reshape(valores,(dim,dim))

actual_n = np.reshape(valores,(dim,dim))
no = []
m = actual.ravel()
fig = plt.figure()
plt.imshow(actual, interpolation='nearest', cmap=cm.jet)
fig.suptitle('Gráfica cristalización')
plt.savefig('Reto1_Practica2.png', dpi=300)
# plt.close()
plt.show()
p=0
while 0 in m:
    valor = []
    for pos in range(num):
        fila = pos // dim
        columna = pos % dim
        na = actual[fila,columna]
        
        if na > 0:
            while True:    
                for f in range(max(0, fila -1),min(dim, fila + 2)):
                    for c in range(max(0, columna -1),min(dim, columna +2)):

                       if actual_n[f,c] == 0:

                            actual_n[f,c] = na

                ac = actual_n[max(0, fila -1):min(dim, fila + 2),
                              max(0, columna -1):min(dim, columna +2)].ravel()
                acc = np.count_nonzero(ac == 0)
                if acc == 0:
                    break
 
    for i in range(num):
        f = i // dim
        c = i % dim
        valor.append(actual_n[f,c])
    p += 1
    actual = np.reshape(valor,(dim,dim))
    m = actual.ravel()
    fig = plt.figure()
    plt.imshow(actual, interpolation='nearest', cmap=cm.jet)
    fig.suptitle('Gráfica cristalización')
    plt.savefig('Reto1_Practica2_{:d}.png'.format(p), dpi=300)
    # plt.close()
    plt.show()

for i in actual[0,:]:
    no.append(i)
for i in actual[:,0]:
    no.append(i)
for i in actual[dim-1,:]:
    no.append(i)
for i in actual[:,dim-1]:
    no.append(i)

no = np.unique(no)

for i in range(len(no)):
    for x in range(len(valor)):
        a = no[i]
        b = valor[x]
        if a == b:
            valor[x] = 0

actual = np.reshape(valor,(dim,dim))
fig = plt.figure()
plt.imshow(actual, interpolation='nearest', cmap=cm.jet)
fig.suptitle('Gráfica cristalización')
plt.savefig('Reto1_Practica2_f.png',dpi=300)
plt.show()      
m = actual.ravel()
print(np.count_nonzero(m == 0) / num )
    