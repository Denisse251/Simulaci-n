# -*- coding: utf-8 -*-
"""
Created on Wed May 19 10:11:44 2021

@author: denis
"""

from random import randint
from math import floor, log
import pandas as pd
import numpy as np
from pyDOE import  fullfact
import seaborn as sns
import matplotlib.pyplot as plt

f = [1, 1, 0]
repeticion = 10
FS = []

for p in range(0,11, 1):
    pr = p/10
    for replica in range(repeticion):
        modelos = pd.read_csv('digits.txt', sep=' ', header = None)
        modelos = modelos.replace({'n': f[0], 'g': f[1], 'b': f[2]})
        r, c = 5, 3
        dim = r * c
         
        tasa = 0.15
        tranqui = 0.99
        tope = 9
        k = tope + 1 # incl. cero
        contadores = np.zeros((k, k + 1), dtype = int)
        n = floor(log(k-1, 2)) + 1
        neuronas = np.random.rand(n, dim) # perceptrones
          
        for t in range(5000): # entrenamiento
            d = randint(0, tope)
            pixeles = abs(1 * (np.random.rand(dim) < modelos.iloc[d]) - (np.random.uniform(size = dim)<pr))
            correcto = '{0:04b}'.format(d)
            for i in range(n):
                w = neuronas[i, :]
                deseada = int(correcto[i]) # 0 o 1
                resultado = sum(w * pixeles) >= 0
                if deseada != resultado: 
                    ajuste = tasa * (1 * deseada - 1 * resultado)
                    tasa = tranqui * tasa 
                    neuronas[i, :] = w + ajuste * pixeles
         
        for t in range(300): # prueba
            d = randint(0, tope)
            pixeles = abs(1 * (np.random.rand(dim) < modelos.iloc[d]) - (np.random.uniform(size = dim)<pr))
            correcto = '{0:04b}'.format(d)
            salida = ''
            for i in range(n):
                salida += '1' if sum(neuronas[i, :] * pixeles) >= 0 else '0'
            r = min(int(salida, 2), k)
            contadores[d, r] += 1
        c = pd.DataFrame(contadores)
        # print(c)
        c.columns = [str(i) for i in range(k)] + ['NA']
        c.index = [str(i) for i in range(k)]
        cm = np.array(c)
        
        TP = np.diag(cm)
        
        FP = np.sum(cm[:,:-1], axis=0) - TP
        
        FN = np.sum(cm, axis=1) - TP
        
        num_classes = k
        TN = []
        for i in range(num_classes):
            temp = np.delete(cm, i, 0)    # delete ith row
            temp = np.delete(temp, i, 1)  # delete ith column
            TN.append(sum(sum(temp)))
        # print(TN)
        
        l = 300
        for i in range(num_classes):
            print(TP[i] + FP[i] + FN[i] + TN[i] == l)
            
        precision = TP/(TP+FP)
        recall = TP/(TP+FN)    
        specificity = TN/(TN+FP)
        
        F_score = 2/ ((1/precision)+(1/recall))
        F_score2 = TP / (TP+((FP+FN)/2))    
        F_score3 = (2 * precision * recall)
        
        for x in F_score:
            FS.append(x)

rep = repeticion * 10
df = pd.DataFrame(
    {"Porcentaje sal y pimienta": ["0.0"] * rep + ["0.1"] * rep + ["0.2"] * rep + ["0.3"] * rep +
                 ["0.4"] * rep + ["0.5"] * rep + ["0.6"] * rep + ["0.7"] * rep +
                 ["0.8"] * rep + ["0.9"] * rep + ["1"] * rep ,
     "F-Score": FS}
     )



pd.set_option("display.max_rows", None, "display.max_columns", None)
ax = sns.violinplot(x='Porcentaje sal y pimienta', y='F-Score', data=df, scale='count', inner="box"  ,cut = 0)
plt.savefig('p11p_r2_1.png', dpi=300)
plt.show()
plt.close()


