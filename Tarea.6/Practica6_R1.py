# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 18:17:54 2021

@author: denis
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from math import floor, log, sqrt
from random import random, uniform
 
l = 1.5
n = 50
pi = 0.05
pr = 0.02 # prob. de recuperar
v = 15
r = 0.1
tmax = 100
digitos = floor(log(tmax, 10)) + 1
c = {'I': 'r', 'S': 'g', 'R': 'orange'}
m = {'I': 'o', 'S': 's', 'R': '2'}
tt_t, im_t = [], []
for va in range(0, 10):
    tt, im = [], []
    pv = va/10
    prim = 0
    for iteraciones in range(15):
        agentes =  pd.DataFrame()
        agentes['x'] = [uniform(0, l) for i in range(n)]
        agentes['y'] = [uniform(0, l) for i in range(n)]
        agentes['xi'] = agentes['x']
        agentes['yi'] = agentes['y']
        agentes['px'] = [uniform(0, l) for i in range(n)]
        agentes['py'] = [uniform(0, l) for i in range(n)]
        agentes['vpx'] = agentes['x'] < agentes['px']
        agentes['vpy'] = agentes['y'] < agentes['py']
        agentes['estado'] = ['R' if random() <= pv else 'S' if random() > pi else 'I' for i in range(n)]
        vx, vy = False, False
        epidemia = []
        for tiempo in range(tmax):
            conteos = agentes.estado.value_counts()
            infectados = conteos.get('I', 0)
            epidemia.append(infectados)
            if infectados == 0:
                break
            contagios = [False for i in range(n)]
            for i in range(n): # contagios
                a1 = agentes.iloc[i]
                if a1.estado == 'I':
                    for j in range(n):
                        a2 = agentes.iloc[j]
                        if a2.estado == 'S':
                            d = sqrt((a1.x - a2.x)**2 + (a1.y - a2.y)**2)
                            if d < r:
                                if random() < (r - d) / r:
                                    contagios[j] = True
            for i in range(n): # movimientos
                a = agentes.iloc[i]
                if contagios[i]:
                    agentes.at[i, 'estado'] = 'I'
                elif a.estado == 'I': # ya infectado
                    if random() < pr:
                        agentes.at[i, 'estado'] = 'R'
                
                velx = (a.px-a.xi)/v
                vely = (a.py-a.yi)/v
                x = a.x + velx
                y = a.y + vely
                
                if a.vpx:
                    if x >= a.px:
                        vx = True
                else:
                    if x <= a.px:
                        vx = True
        
                if a.vpy:
                    if y >= a.py:
                        vy = True      
                else:
                    if y <= a.py:
                        vy = True
                    
                x = x if x < l else x - l
                y = y if y < l else y - l
                x = x if x > 0 else x + l
                y = y if y > 0 else y + l
                agentes.at[i, 'x'] = x
                agentes.at[i, 'y'] = y
                if vx and vy:
                    agentes.at[i, 'xi'] = a.x
                    agentes.at[i, 'yi'] = a.y
                    agentes.at[i, 'px'] = uniform(0, l)
                    agentes.at[i, 'py'] = uniform(0, l)
                    agentes.at[i, 'vpx'] = a.x < a.px
                    agentes.at[i, 'vpy'] = a.y < a.py
                vx, vy = False, False
            if prim == 0:
                fig = plt.figure()
                ax = plt.subplot(1, 1, 1)
                plt.xlim(0, l)
                plt.ylim(0, l)
                for e, d in agentes.groupby('estado'):
                    if len(d) > 0:
                        ax.scatter(d.x, d.y, c = c[e], marker = m[e])
                plt.xlabel('x')
                plt.xlabel('y')
                plt.title('Paso {:d}'.format(tiempo + 1))
                fig.savefig('p6p_v{:d}_t'.format(va) + format(tiempo, '0{:d}'.format(digitos)) + '.png')
                plt.close()

        if prim == 0:
            plt.figure(figsize=(8, 3), dpi=300)
            plt.plot(range(len(epidemia)), [100 * e / n for e in epidemia], 'bo')
            plt.xlabel('Tiempo')
            plt.ylabel('Porcentaje de infectados')
            plt.savefig('p6pe_v{:d}.png'.format(va), bbox_inches='tight')
            plt.close()
            
        prim = 1
        ite = (np.where(epidemia == max(epidemia))[0])
        for x in ite:
            tt.append(x)
        maximo = [max(epidemia)] * len(ite)
        for x in maximo:
            im.append(x)

    im_t.append(im)
    tt_t.append(tt)
    
tm = []
im = []
for x in tt_t:
    tm.append(np.median(x))    
for x in im_t:
    im.append(np.median(x))    
xticks=[x/10 for x in range(0,10)]
p=[x for x in range(1,11)]     
medianprops = dict(linestyle='solid', linewidth=2.5, color='red')
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.boxplot(tt_t, showfliers=False, medianprops=medianprops)
ax1.set_ylabel('Momento del pico')
ax2.boxplot(im_t, showfliers=False, medianprops=medianprops)
ax2.set_ylabel('Altura del pico')
plt.xticks(p, xticks)
plt.xlabel('Prob. de vacunación')
plt.savefig('p6pg.png', dpi=300)
