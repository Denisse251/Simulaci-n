# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 23:01:10 2021

@author: denis
"""

from math import pi
import numpy as np
import matplotlib.pyplot as plt

runs = 10
cantidad = 1000
er_p = []
d = 0
eti = []
de = []
while runs <= 1000000:
    pi_p = []

    radio = 0.5
    for a in range(cantidad):
        X = np.random.uniform(-radio, radio, runs)
        Y = np.random.uniform(-radio, radio, runs) 
        
        circulo = X**2 + Y**2 <= radio**2
        pi_c = circulo.sum()/ runs * 4
        pi_p.append(pi_c)
    pi_ce = sum(pi_p) / cantidad
    error = abs((pi_ce - pi) / pi_ce) * 100   
    er_p.append(error)
    # print(pi_ce)
    d += 1
    de.append(d)
    etiqueta = r'$10^{'+str(d)+'}$'
    eti.append(etiqueta)
    runs *= 10
    extra = np.invert(circulo)
    plt.figure(figsize=(10,10))    
    plt.plot(X[circulo], Y[circulo], 'r.')
    plt.plot(X[extra], Y[extra], 'g.')
    plt.title('Aproximación de pi = {0:.8f} \n Con la cantidad de {1:d}'.format(pi_ce, runs))
    plt.savefig('p5r1f{:d}.png'.format(d), dpi=300)
    plt.show()
    
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.plot(de, er_p, '.-')
plt.xlabel(r'$cantidad$')
plt.ylabel(r'$Porcentaje de error$')
plt.xticks(de, eti)
plt.savefig('p5r1.png', dpi=300)
plt.show() # opcional
plt.close()
    
