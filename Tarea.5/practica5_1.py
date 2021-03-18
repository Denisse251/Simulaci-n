# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 20:30:07 2021

@author: denis
"""

from math import exp, pi
import numpy as np
import matplotlib.pyplot as plt
from GeneralRandom import GeneralRandom
def g(x):
    return (2  / (pi * (exp(x) + exp(-x))))
 
vg = np.vectorize(g)
X = np.arange(-8, 8, 0.002) # ampliar y refinar
Y = vg(X) # mayor eficiencia
 

generador = GeneralRandom(np.asarray(X), np.asarray(Y))
desde = 3
hasta = 7
    
def parte(pedazo, replica):
    V = generador.random(pedazo)[0]
    return ((V >= desde) & (V <= hasta)).sum() 

def porcentaje(por, dec):
    r = str(0.048834)
    p = 0
    for y in range(len(por)):
        f = 0
        v = por[y]
        for x in range(3,len(r)):
            if v[x] == r[x]:

                f += 1
            else:
                break
        print(f)
        if f >= dec:
            p += 1
    porc = (p / len(por))*100
    print(porc)
    return porc
 
import multiprocessing
if __name__ == "__main__":
    cuantos = 50000
    pedazo = 10
    dec = 1
    ped = []
    ped_e = []
    deci = []
    pedazo_1 = 2
    while pedazo <= 100000:
        print(pedazo)
        por = []
        for a in range(10):
            with multiprocessing.Pool(2) as pool:
                montecarlo = pool.starmap(parte, zip([pedazo]*cuantos, range(cuantos)))
                integral = sum(montecarlo) / (cuantos * pedazo)
                f=(pi / 2) * integral
                # print(f)
                por.append(str(f))
                print(f)
        porc = porcentaje(por, dec)
        if porc >= 90:
            deci.append(dec+1)
            ped.append(pedazo_1)
            dec += 1
            etiqueta = r'$10^{'+str(pedazo_1)+'}$'
            ped_e.append(etiqueta)
            print('es mayor que 90')
        pedazo *= 10
        pedazo_1 += 1
        
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.plot(deci, ped, 'o-')
    plt.xlabel(r'$Decimales$')
    plt.ylabel(r'$Pedazo$')
    plt.xticks(deci)
    plt.yticks(ped, ped_e)
    plt.savefig('p5p1m.png', dpi=300)
    plt.show() # opcional
    plt.close()
