# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 22:13:25 2021

@author: denis
"""

import matplotlib.pyplot as plt
import pandas as pd
from math import ceil, sqrt
def divisores(n):
    if n % 2 == 0:
        for i in range(1, int(ceil(sqrt(n)))):
            if n % i == 0:
                p = True
                if i < 4:
                    p = True
                    
                if i % 2 == 0:
                    p = False
                for x in range(3, int(ceil(sqrt(i))), 2):
                    if i % x == 0:
                        p = False
                if p == True:
                    print(i)
                    for x in range(1, n):
                        if i == 1:
                            break
                        elif i**x > n:
                            break
                        elif i**x == n:
                            print(i , x)
                            break
        return True
    else:           
        for i in range(1, int(ceil(sqrt(n))), 2):
            if n % i == 0:
                p = True
                if i < 4:
                    p = True
                if i % 2 == 0:
                    p = False
                for i in range(3, int(ceil(sqrt(i))), 2):
                    if n % i == 0:
                        p = False
    
                if p == True:
                    print(i)
                    for x in range(1, n):
                        if i == 1:
                            break
                        elif i**x > n:
                            break
                        elif i**x == n:
                            print(i , x)
                            break
        return True

from scipy.stats import describe # instalar con pip3
import multiprocessing
cores = multiprocessing.cpu_count()
from time import time
if __name__ == "__main__":
    df = pd.read_csv('C:/Users/denis/OneDrive/Documentos/maestria/Segundo Semestre/Simulación computacional de nanomateriales/practicas/Practica3/numeros.csv')
    primos = df['Primos']
    nprimos = df['No_Primos']
    pares = df['Pares']
    p_np = df['Primos_NoPrimos']
    np_p = df['NoPrimos_Primos']
    aleatorio = df['Aleatorio']
    empezar = df['Pares'][:10]

    replicas = 40
    tiempo=[]
    tt = []
    tiempos = {"pt": [], "pnpt": [], "nppt": [],  "at": [], "npt": [], "part": []}
    for x in range(1, cores-1):
        with multiprocessing.Pool(processes = x) as pool:
            for r in range(replicas):
                pool.map(divisores, empezar)
                t = time()
                pool.map(divisores, primos)
                tiempos["pt"].append(time() - t)
                t = time()
                pool.map(divisores, nprimos)
                tiempos["npt"].append(time() - t)
                t = time()
                pool.map(divisores, pares)
                tiempos["part"].append(time() - t)
                t = time()
                pool.map(divisores, p_np)
                tiempos["pnpt"].append(time() - t)
                t = time()
                pool.map(divisores, np_p)
                tiempos["nppt"].append(time() - t)
                t = time()
                pool.map(divisores, aleatorio)
                tiempos["at"].append(time() - t)
        for tipo in tiempos:
            print('Con la cantidad de núcleos de: ', x)
            print(describe(tiempos[tipo]),tipo)
            print('')
            tiempo.append(tiempos[tipo])
        tt.append(tiempo)
        tiempos = {"pt": [], "pnpt": [], "nppt": [],  "at": [], "npt": [], "part": []}
    fig1 = plt.figure()
    ax1 = fig1.add_subplot()
    ax1.boxplot(tt[0][:6])
    ax1.set_title('1 Núcleo')
    ax1.set(xlabel='Variantes', ylabel='Tiempo')
    plt.savefig('Gráfica_tiempo_1.png', dpi=300)

    fig2 = plt.figure()
    ax2 = fig2.add_subplot()
    ax2.boxplot(tt[0][6:12])
    ax2.set_title('2 Núcleos')
    ax2.set(xlabel='Variantes', ylabel='Tiempo')
    plt.savefig('Gráfica_tiempo_2.png', dpi=300)
                          
    fig3 = plt.figure()
    ax3 = fig3.add_subplot()
    ax3.boxplot(tt[0][12:18])
    ax3.set_title('3 Núcleos')
    ax3.set(xlabel='Variantes', ylabel='Tiempo')
    plt.savefig('Gráfica_tiempo_3.png', dpi=300)
    
    fig4 = plt.figure()
    ax4 = fig4.add_subplot()
    ax4.boxplot(tt[0][18:24])
    ax4.set_title('4 Núcleos')
    ax4.set(xlabel='Variantes', ylabel='Tiempo')
    plt.savefig('Gráfica_tiempo_4.png', dpi=300)  
    
    fig5 = plt.figure()
    ax5 = fig5.add_subplot()
    ax5.boxplot(tt[0][24:30])
    ax5.set_title('5 Núcleos')
    ax5.set(xlabel='Variantes', ylabel='Tiempo')
    plt.savefig('Gráfica_tiempo_5.png', dpi=300) 

    fig6 = plt.figure()    
    ax6 = fig6.add_subplot()
    ax6.boxplot(tt[0][30:36])
    ax6.set_title('6 Núcleos')
    ax6.set(xlabel='Variantes', ylabel='Tiempo')
    plt.savefig('Gráfica_tiempo_6.png', dpi=300)