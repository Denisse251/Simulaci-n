# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:45:26 2021

@author: denis
"""
from random import random, randint
import matplotlib.pyplot as plt 
import pandas as pd


for e in range(6):
    exponencial = e + 4
    exp = 2 ** exponencial
    print('Con numero de pasos de ', exp)
    rf=[],[],[],[],[]
    minimo, maximo, promedio, porcentaje = [],[],[],[]
    for d in range(5):
        dimension = d+1
        p_inicial = [0] * dimension
        resultados = []
        resultados1 = []
        repeticiones = 30
    
        for nr in range(repeticiones):
            nunca = True
    
            for paso in range(exp):
                dim = randint(0, dimension-1)
                p_inicial[dim] = p_inicial[dim] + 1 if random() < 0.5 else p_inicial[dim] -1
                
                if all([p == 0 for p in p_inicial]):
                    resultados.append(paso+1)
                    resultados1.append(paso+1)
                    nunca = False
                    break
            if nunca:
                resultados.append(None)
                # resultados1.append(exp+1)
        
        cuantos = sum([r is None for r in resultados])
        # print((cuantos / repeticiones)*100, 'no regresaron nunca en la dimension ', d+1)
        porcentaje.append((cuantos / repeticiones)*100)
        if cuantos < repeticiones:
            regresaron = sum([r if r is not None else 0 for r in resultados])
            # print(regresaron / (repeticiones - cuantos), 'fue la tardanza en promedio en la dimension ', d+1)
        for r in resultados1:
            rf[d].append(r) 
        # print(rf[d])
        if rf[d] > []:
            mi = min(rf[d])
            prom = sum(rf[d])/len(rf[d])
            ma = max(rf[d])
            minimo.append(mi)
            promedio.append(prom)
            maximo.append(ma)
        else:
            # print("se anula")
            minimo.append('Anulado')
            promedio.append('Anulado')
            maximo.append('Anulado')
        
            
    data = {'Dimension':[1,2,3,4,5], 
            'Minimo':minimo, 
            'Promedio':promedio, 
            'Maximo':maximo,
            'Porcentaje':porcentaje} 
    # print(data)
    df = pd.DataFrame(data)
    print(df)
        
    fig, ax = plt.subplots()
    ax.boxplot(rf)
    ax.set_xlabel('Dimensión')
    ax.set_ylabel('Pasos')
    ax.set_title('Total de Pasos: ' + str(exp))
    # ax.set_title('')
    plt.savefig('p1_pasos_de_'+ str(exp) + '.png')
    # plt.close()