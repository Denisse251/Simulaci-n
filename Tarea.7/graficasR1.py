# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 03:00:12 2021

@author: denis
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import floor, log

def g(x, y):
    return (np.cos(4.5*x + 0.3) - x * (x + 0.2) - 1.01 + np.sin(y+2))

low = -3
high = 3
step = 0.2
p = np.arange(low, high, step)
n = len(p)
z = np.zeros((n, n), dtype=float)
valores=[]
paso = 0.5

digitos = floor(log(100, 10)) + 1
guardar = 0
for i in range(n):
    x = p[i]
    for j in range(n): 
        y = p[n - j - 1] # voltear
        z[i, j] = g(x, y)
        valores.append(g(x, y))
maximo=max(valores)
ts = [10, 50, 100]
xis = [0.99, 0.66, 0.33]
v = [99, 66, 33]
for t in ts:
    va = 0
    vi = va+1
    
    for xi in xis: 
        valor=v[va]
        df1 = pd.read_csv('resultados_15_T{0:}_xi{1:}.csv'.format(t, vi))
        df2 = pd.read_csv('resultados_30_T{0:}_xi{1:}.csv'.format(t, vi))
        df3 = pd.read_csv('resultados_45_T{0:}_xi{1:}.csv'.format(t, vi))
        
        p1 = df1['T '+str(t)+' xi '+str(xi)+ ' '+'15 con 100'],df2['T '+str(t)+' xi '+str(xi)+ ' '+'30 con 100'],df3['T '+str(t)+' xi '+str(xi)+ ' '+'45 con 100']
        p2 = df1['T '+str(t)+' xi '+str(xi)+ ' '+'15 con 1000'],df2['T '+str(t)+' xi '+str(xi)+ ' '+'30 con 1000'],df3['T '+str(t)+' xi '+str(xi)+ ' '+'45 con 1000']
        p3 = df1['T '+str(t)+' xi '+str(xi)+ ' '+'15 con 10000'],df2['T '+str(t)+' xi '+str(xi)+ ' '+'30 con 10000'],df3['T '+str(t)+' xi '+str(xi)+ ' '+'45 con 10000']
        medianprops = dict(linestyle='solid', linewidth=2.5, color='red')
        
        xticks=[15*x for x in range(1,4)]
        p=[x for x in range(1,4)] 
        
        
        plt.boxplot(p1,medianprops=medianprops)
        plt.ylabel('Maximos')
        plt.xticks(p, xticks)
        plt.xlabel('replicas')
        plt.axhline(maximo, color = 'green',label='Maximo estimado') 
        # plt.legend()
        plt.savefig('p7_p100_T'+str(t)+'_xi'+str(valor)+'.png', dpi=300)
        plt.show()
        plt.close()
        
        plt.boxplot(p2,medianprops=medianprops)
        plt.ylabel('Maximos')
        plt.xticks(p, xticks)
        plt.xlabel('replicas')
        plt.axhline(maximo, color = 'green',label='Maximo estimado') 
        # plt.legend() 
        plt.savefig('p7_p1000_T'+str(t)+'_xi'+str(valor)+'.png', dpi=300)
        plt.show()
        plt.close()
        
        plt.boxplot(p3,medianprops=medianprops)
        plt.ylabel('Maximos')
        plt.xticks(p, xticks)
        plt.xlabel('replicas')
        plt.axhline(maximo, color = 'green',label='Maximo estimado') 
        # plt.legend() 
        plt.savefig('p7_p10000_T'+str(t)+'_xi'+str(valor)+'.png', dpi=300)
        plt.show()
        plt.close()
        va += 1
        vi= va+1
        