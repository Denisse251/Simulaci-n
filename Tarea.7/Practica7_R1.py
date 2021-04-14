# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 23:11:30 2021

@author: denis
"""

from random import uniform, random
import matplotlib.pyplot as plt
import numpy as np
from math import exp, floor, log
import pandas as pd

def g(x, y):
    return np.cos(4.5*x + 0.3) - x * (x + 0.2) - 1.01 + np.sin(y+2)


low = -3
high = 3
step = 0.1
paso = 0.5

p = np.arange(low, high, step)
n = len(p)
z = np.zeros((n, n), dtype=float)
valores=[]
for i in range(n):
    x = p[i]
    for j in range(n): 
        y = p[n - j - 1] # voltear
        z[i, j] = g(x, y)
        valores.append(g(x, y))
digitos = floor(log(100, 10)) + 1


tmax=10
temperaturas = [10, 50, 100]
xis = [0.99, 0.66, 0.33]
for temperatura in temperaturas:
    valor=1
    guardar = 0
    for xi in xis:
        for a in range(15, 46, 15):
        
            resultados = pd.DataFrame()
            for tiem in range(2, 5):
                agentes =  pd.DataFrame()
                agentes['x'] = [uniform(low, high) for i in range(a)]
                agentes['y'] = [uniform(low, high) for i in range(a)]
                agentes['t'] = [temperatura for i in range(a)]
                agentes['best'] = [min(valores) for i in range(a)]
                
                
                bestx = agentes['x'][0]
                besty = agentes['x'][0]
                best = g(bestx,besty)
                
                
        
                for tiempo in range(tmax**tiem):
                    agentes['dx'] = [uniform(-paso, paso) for i in range(a)]
                    agentes['dy'] = [uniform(-paso, paso) for i in range(a)]
                    for i in range(a):
                        r = agentes.iloc[i]
                        xp = r.x + r.dx
                        yp = r.y + r.dy
                        
                        if  xp < low+step:
                            xp = r.x
                        elif xp > high-step:
                            xp = r.x
                        if  yp < low+step:
                            yp = r.y
                        elif yp > high-step:
                            yp = r.y
                        
                        delta = g(xp, yp) - g(r.x, r.y)
                        prob = exp(delta/r.t)
                        if delta > 0:
                            agentes.at[i, 'x'] = xp
                            agentes.at[i, 'y'] = yp
                        else:
                            if random() < (prob):
                                agentes.at[i, 'x'] = xp
                                agentes.at[i, 'y'] = yp
                                agentes.at[i, 't'] = r.t * xi
                        mejor = g(r.x, r.y)
                        if mejor > best:
                            best = g(r.x, r.y)
                            bestx = r.x
                            besty = r.y
                        if mejor > r.best:
                            agentes.at[i, 'best'] = mejor
                            
                    xb = ((n-1)/2)+(bestx/step)
                    yb= ((n-1)/2)-(besty/step)
                    
                    if guardar == 0:
                        t = range(0, n, 5)
                        l = ['{:.1f}'.format(low + i * step) for i in t]
                        fig, ax = plt.subplots(figsize=(6, 5), ncols=1)
                        pos = ax.imshow(z) 
                        for k in range(a):
                            r = agentes.iloc[k]
                            x= ((n-1)/2)+(r.x/step)
                            y= ((n-1)/2)-(r.y/step)     
                            ax.plot(y, x, 'ro')
                        ax.plot(yb,xb, 'go')
                        plt.xticks(t, l)
                        plt.yticks(t, l[::-1]) # arriba-abajo
                        fig.colorbar(pos, ax=ax)
                        plt.savefig('p7_T{0:d}_xi_{1:d}v_t'.format(temperatura, (valor)) + format(tiempo, '0{:d}'.format(digitos)) + '.png')
            
                guardar = 1
                resultados['T ' + str(temperatura)+' xi '+ str(xi)+ ' '+ (str(a)+' con ' +str(tmax**tiem))] = agentes['best']
                print(tmax**tiem)
                
            resultados.to_csv('resultados_{0:d}_T{1:d}_xi{2:d}.csv'.format(a, temperatura, valor))
        valor +=1
                      