# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:58:28 2021

@author: denis
"""
import numpy as np
from random import randint, random
from numpy.random import shuffle
import matplotlib.pyplot as plt
from math import exp, floor, log
import pandas as pd



def rotura(x, c, d):
    return 1 / (1 + exp((c - x) / d))
 
def union(x, c):
    return exp(-x / c)
 

 
def romperse(tam, cuantos):
    if tam == 1: # no se puede romper
        return [tam] * cuantos
    res = []
    for cumulo in range(cuantos):
        if random() < rotura(tam, c, d):
            primera = randint(1, tam - 1)
            segunda = tam - primera
            assert primera > 0
            assert segunda > 0
            assert primera + segunda == tam
            res += [primera, segunda]
        else:
            res.append(tam) # no rompió
    assert sum(res) == tam * cuantos
    return res
 
def unirse(tam, cuantos):
    res = []
    for cumulo in range(cuantos):
        if random() < union(tam, c):
            res.append(-tam) # marcamos con negativo los que quieren unirse
        else:
            res.append(tam)
    return res

def filtro(cumulos, c, n):
    cum = []
    for valor in cumulos:
        if valor >= c:
            cum.append(valor)
    porcentaje = (sum(cum)*100)/n
    return porcentaje

eps = 0.5
k = 1000
ns = [16000,32000,64000,128000]
# porc = []

replica = 50
repeticion = 25
post = []
pm = []
vm = []
for n in ns: 
    porct = []
    pos = []
    for repet in range(repeticion):
        for r in range(replica):
            porc = []
            orig = np.random.normal(size = k)
            cumulos = orig - min(orig)
            cumulos += eps # ahora el menor vale epsilon
            cumulos = cumulos / sum(cumulos) # ahora suman a uno
            cumulos *= n # ahora suman a n, pero son valores decimales
            cumulos = np.round(cumulos).astype(int) # ahora son enteros
            diferencia = n - sum(cumulos) # por cuanto le hemos fallado
            cambio = 1 if diferencia > 0 else -1
            while diferencia != 0:
                p = randint(0, k - 1)
                if cambio > 0 or (cambio < 0 and cumulos[p] > 0): # sin vaciar
                    cumulos[p] += cambio
                    diferencia -= cambio
            assert (all([c != 0 for c in cumulos])) 
            assert sum(cumulos) == n
             
            c = np.median(cumulos) # tamaño crítico de cúmulos
            d = np.std(cumulos) / 4 # factor arbitrario para suavizar la curva
             
            duracion = 50
            digitos = floor(log(duracion, 10)) + 1
    
            for paso in range(duracion):
                if n == 0:
                    porc.append(0)
                else:
                    assert sum(cumulos) == n
                    assert (all([c > 0 for c in cumulos])) 
                    (tams, freqs) = np.unique(cumulos, return_counts = True)
                    cumulos = []
                    assert len(tams) == len(freqs)
                    for i in range(len(tams)):
                        cumulos += romperse(tams[i], freqs[i]) 
                    assert sum(cumulos) == n
                    assert (all([c > 0 for c in cumulos])) 
                    (tams, freqs) = np.unique(cumulos, return_counts = True)
                    cumulos = []
                    assert len(tams) == len(freqs)
                    for i in range(len(tams)):
                        cumulos += unirse(tams[i], freqs[i])
                    cumulos = np.asarray(cumulos)
                    neg = cumulos < 0
                    a = len(cumulos)
                    juntarse = -1 * np.extract(neg, cumulos) # sacarlos y hacerlos positivos
                    cumulos = np.extract(~neg, cumulos).tolist() # los demás van en una lista
                    assert a == len(juntarse) + len(cumulos)
                    nt = len(juntarse)
                    if nt > 1:
                        shuffle(juntarse) # orden aleatorio
                    j = juntarse.tolist()
                    while len(j) > 1: # agregamos los pares formados
                        cumulos.append(j.pop(0) + j.pop(0))
                    if len(j) > 0: # impar
                        cumulos.append(j.pop(0)) # el ultimo no alcanzó pareja
                    assert len(j) == 0
                    assert sum(cumulos) == n
                    assert (all([c != 0 for c in cumulos]))
    
                    porc.append(filtro(cumulos, c, n))
    
            porct.append(porc)
    
        PT = []
        for m in range(duracion):
            P = []
            for row in range(len(porct)):
                P.append(porct[row][m])
            PT.append(P)
        medianas = [np.median(PT[x]) for x in range(duracion)]  
        maximo  = max(medianas)
        posicion = medianas.index(max(medianas))+1
        pos.append(posicion)
    post.append(pos)
    mejor = 0
    for p in pos:
        valor = pos.count(p)
        if valor > mejor:
            mejor = valor
            mejorv = p
            
    vm.append(mejorv)
    pm.append((mejor*100)/repeticion)

    plt.plot(pos)
    plt.ylabel('Iteración ideal')
    plt.xlabel('Repetición')
    plt.savefig('p8_r1_n'+str(n)+'.png', dpi=300)
    plt.show()
    plt.close()
    
plt.boxplot(post)
plt.ylabel('Iteración ideal')
plt.xlabel('Particulas')
plt.xticks([1,2,3,4],ns)
plt.savefig('p8_01_r1_n'+str(n)+'.png', dpi=300)
plt.show()
plt.close()

df = pd.DataFrame()
df['particulas']=ns
df['mejor valor']=vm
df['porcentaje']=pm
df.to_csv('tabla_de_mejor.csv')