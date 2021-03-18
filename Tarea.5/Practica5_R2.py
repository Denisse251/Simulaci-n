# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:20:58 2021

@author: denis
"""

from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

im = Image.open('pera.png')
a = np.asarray(im,dtype=np.float32)/255
plt.figure(figsize=(12,12))
plt.imshow(a)
plt.axis('off')
plt.show()
w, h = im.size
colors = im.getcolors(w * h)
num_colores = len(colors) 
num_pixels = w*h
x, y, z = a.shape
a1 = a.reshape(x*y, z)
n = 10
k_means = KMeans(n_clusters=n)
k_means.fit(a1)
centroides = k_means.cluster_centers_
etiquetas = k_means.labels_
a2 = centroides[etiquetas]
a3 = a2.reshape(x,y,z)
plt.figure(figsize=(12,12))
plt.imshow(a3)
plt.axis('off')
plt.savefig('p5_r2.png', dpi=300)
plt.show()

runs = 10
while runs <= 100000:
    if runs >= w*h:
        print('El valor de muestras es mas grande que la imagen')
        break
    cantidad_c = len(centroides)
    porcentajes = [[]]* cantidad_c
    litros = [[]] * cantidad_c
    colores = [[]] * cantidad_c
    for cant in range(cantidad_c):
        X = np.random.uniform(0, h, runs)
        Y = np.random.uniform(0, w, runs) 
        valores = []
        for a in range(runs):
            x = int(X[a])
            y = int(Y[a])
            valores.append(a3[x,y])
            porcentaje = []
    
        for a in range(cantidad_c):
            color = valores == centroides[a]
            suma = color.sum()
            porcentaje.append(((suma-runs)/3)/runs)
            
        porcentajes[cant] = porcentaje
        
        #usando la formula para pintura de calidad dada por https://disnapin.com/como-calcular-la-cantidad-de-pintura-a-utilizar-en-paredes/
        metros = 25
        rendimiento = 10
        manos = 2
        pintura_t = (metros/rendimiento) * manos
        # litros por colores
        litros[cant] = [pintura_t*p for p in(porcentajes[cant])] 
        colores[cant] = [c for c in range(1, cantidad_c+1)]
        
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.boxplot(litros, colores)
    # plt.title('Cantidad de litros de pintura por color')
    plt.xlabel('colores')
    plt.ylabel('Litros de pintura')
    plt.savefig('p5_r2_{:d}.png'.format(runs), dpi=300)
    plt.show() # opcional
    plt.close()
    runs *= 10

    