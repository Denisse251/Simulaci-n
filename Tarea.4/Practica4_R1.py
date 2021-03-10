# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 23:35:52 2021

@author: denis
"""

import seaborn as sns # instalar con pip3
from random import randint, choice
from PIL import Image, ImageColor # instalar con pip3
from math import sqrt
import pandas as pd
import matplotlib.pyplot as plt



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
    grieta = zona.copy()
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
                   if celda[vx, vy] == celda[x, y]: # misma celda
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


replicas = 10
for n in range(20, 101, 20):
    p_t = []
    porcentaje = []
    dimension = []
    for por in range(50, 151,25):
        profundidad = []
        k = int((por*n)/100) 
        semillas =  []
        fondo = (255, 0, 0) # rojo
        zona = Image.new('RGB', (n, n), color = fondo)
        celda = zona.load()
        radio = [1]*k
        color = sns.color_palette("Set3", k).as_hex()
        semillas = []
        sc = []
        ciclo = 0
        semilla = 0
        while True:
            
            ac = []
            for s in range(len(semillas)):
                for pos in range(n*n):
                    fil = pos // n
                    col = pos % n
                    if celda[fil, col] == fondo:
                        ac.append(1)
                    else:
                        ac.append(0)
                    (xs, ys) = semillas[s]
                    dx, dy = fil - xs, col - ys
                    dist = sqrt(dx**2 + dy**2)
                    if dist <= radio[s]:
                        if celda[fil, col] == fondo:
                            celda[fil, col] = ImageColor.getrgb(color[sc[s]])
                radio[s] += 1
        
            if semilla <= k-1:
                conteo = 0
                while True:
                    if ac == []:
                        ac.append(1)
                    if len(sc) == k:
                        break
                    columna = randint(0, n - 1)
                    fila = randint(0, n - 1)
                    if celda[columna, fila] == fondo:
                        celda[columna, fila] =  ImageColor.getrgb(color[semilla])
                        sc.append(semilla)
                        semillas.append((columna,fila))
                        break
                    if conteo == 10:
                        break
                    conteo += 1
            visual = zona.resize((10 * n,  10 * n), resample=Image.BOX)
            # visual.save("p4p_{:d}.png".format(ciclo))
            visual.save("p4p_{1:d}_{2:d}_{0:d}.png".format(ciclo, n, k))

            ciclo += 1
            semilla += 1
            acc = max(ac)
            if acc == 0:
                print('no hay fondo')
                break
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
    print(data)
    df = pd.DataFrame(data)
    ax = sns.boxplot(x='semillas', y="distancia", data=df);
    plt.savefig('Grafica_dimensión_{:d}'.format(n), dpi=300) 
    plt.show()    