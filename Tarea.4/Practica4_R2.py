# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 21:11:59 2021

@author: denis
"""

import seaborn as sns # instalar con pip3
from random import randint,random
from PIL import Image, ImageColor # instalar con pip3
from math import sqrt
import pandas as pd
import matplotlib.pyplot as plt

pvr=[0.1, 0.25, 0.50]
pmr=[1 , 0.5, 0.25]
pvc=[]
pmc=[]
cont=[]
# for replica in range(10):
for pm in (pmr):
    pvc=[]
    pmc=[]
    cont=[]
    for replica in range(10):
        for pv in (pvr):
            # pv = 0.1
            # pm = 1
            n = 50
            k= 15
            p_t = []
            porcentaje = []
            dimension = []  
            profundidad = []
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
            vida = [1]*k
            vecinos = [1]*k
            cic = [0]*k
            cic[0] = -1
            
            
            while True:
                ac = []
                for s in range(len(semillas)):
            
                    for pos in range(n*n):
            
                        fil = pos //  n
                        col = pos % n
                        if celda[fil, col] == fondo:
                            ac.append(1)
                        else:
                            ac.append(0)
                        if vida[s] == 1:
                            cic[s] = 1
                            (xs, ys) = semillas[s]
                            dx, dy = fil - xs, col - ys
                            dist = sqrt(dx**2 + dy**2)
                
                            if dist <= radio[s]:
                                if celda[fil, col] == fondo:
                                    if (random() < pv):
                                        vecinos[s] += 1
                                        celda[fil, col] = ImageColor.getrgb(color[sc[s]])
            
                    v = (vecinos[s])
                    radio[s] += 1
                    vc = cic[s]
                    # print(cic)
                    if v <= 1 and cic[s] == 1 and random() < pm:        
                        vida[s] = 0
                        cic[s] = 2
                if not (0 in cic or 1 in cic):
                    print(replica,'no hay vivos', pm, pv)
                    break
                        
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
                # visual.save("p4p_{1:}_{2:}_{0:d}.png".format(ciclo, pm, pv))
            
                ciclo += 1
                semilla += 1
                acc = max(ac)
                if acc == 0:
                    print(replica,'no hay fondo',pm,pv)
                    break
            print('final pv')
            pvc.append(pv)
            pmc.append(pm)
            cont.append(ciclo)
        print('final pm')

    data = {'Probabilidad':pvc,
            'Ciclo final':cont}
    # print(data) 
    df = pd.DataFrame(data)
    ax = sns.boxplot(x='Probabilidad', y="Ciclo final", data=df);
    plt.savefig('Grafica_probabilidad_{:d}'.format(int(pm*100)), dpi=300) 
    plt.show()    