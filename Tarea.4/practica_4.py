# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 21:33:57 2021

@author: denis
"""

import matplotlib.pyplot as plt
import seaborn as sns
from math import sqrt
from PIL import Image, ImageColor
from random import randint, choice
import pandas as pd


 
def celda(pos):
    if pos in semillas:
        return semillas.index(pos)
    x, y = pos % n, pos // n
    cercano = None
    menor = n * sqrt(2)
    for i in range(k):
        (xs, ys) = semillas[i]
        dx, dy = x - xs, y - ys
        dist = sqrt(dx**2 + dy**2)
        if dist < menor:
            cercano, menor = i, dist
    return cercano
 
def inicio():
    direccion = randint(0, 3)
    if direccion == 0: # vertical abajo -> arriba
        return (0, randint(0, n - 1))
    elif direccion == 1: # izq. -> der
        return (randint(0, n - 1), 0)
    elif direccion == 2: # der. -> izq.
        return (randint(0, n - 1), n - 1)
    else:
        return (n - 1, randint(0, n - 1))

def propaga(replica):
    prob, dificil = 0.9, 0.8
    grieta = voronoi.copy()
    g = grieta.load()
    (x, y) = inicio()
    largo = 0
    negro = (0, 0, 0)
    prof = []
    minimo = []
    while True:
        g[x, y] = negro
        largo += 1
        frontera, interior = [], []
        for v in vecinos:
            (dx, dy) = v
            vx, vy = x + dx, y + dy
            if vx >= 0 and vx < n and vy >= 0 and vy < n: # existe
               if g[vx, vy] != negro: # no tiene grieta por el momento
                   if vor[vx, vy] == vor[x, y]: # misma celda
                       interior.append(v)
                   else:
                       frontera.append(v)
        a = []
        b = y - 0
        a.append(b)
        b= n-1 - y
        a.append(b)
        b = x - 0
        a.append(b)
        b= n-1 - x
        a.append(b)
        minimo.append(min(a))
        elegido = None
        if len(frontera) > 0:
            elegido = choice(frontera)
            prob = 1
        elif len(interior) > 0:
            elegido = choice(interior)
            prob *= dificil
        if elegido is not None:
            (dx, dy) = elegido
            x, y = x + dx, y + dy
        else:
            break # ya no se propaga
       
        
    if largo >= limite:

        prof = max(minimo)
        visual = grieta.resize((10 * n,10 * n),resample=Image.BOX)
        visual.save("p4pg_{1:d}_{2:d}_{0:d}.png".format(replica, n, k))
        return prof
    else:
        return 0 

if __name__ == "__main__":
    replicas = 20
    for n in range(20, 101, 20):
        p_t = []
        porcentaje = []
        dimension = []
        for por in range(50, 151,25):
    
            profundidad = []
            k = int((por*n)/100) 
            semillas =  []
            # semillas = []
            for s in range(k):
                while True:
                    x, y = randint(0, n - 1), randint(0, n - 1)
                    if (x, y) not in semillas:
                        semillas.append((x, y))
                        break
             
            celdas = [celda(i) for i in range(n * n)]
            voronoi = Image.new('RGB', (n, n))
            vor = voronoi.load()
            c = sns.color_palette("Set3", k).as_hex()
            for i in range(n * n):
                vor[i % n, i // n] = ImageColor.getrgb(c[celdas.pop(0)])
            limite, vecinos = n, []
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx != 0 or dy != 0:
                        vecinos.append((dx, dy))
        
            for r in range(replicas): 
                p = propaga(r)
                if p > 0:
                    profundidad.append(p)
                    
            for t in range(0,int(len(profundidad))):
                p_t.append(profundidad[t])
                porcentaje.append(k)
                dimension.append(n)
                
        data = {'distancia':p_t,
                'semillas':porcentaje} 
        df = pd.DataFrame(data)
        ax = sns.boxplot(x='semillas', y="distancia", data=df);
        plt.savefig('Grafica_dimensión_{:d}'.format(n), dpi=300) 
        plt.show()    