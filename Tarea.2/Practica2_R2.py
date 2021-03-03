# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 23:08:38 2021

@author: denis
"""
from random import random
import pandas as pd
import numpy as np

input = "star.csv"
m = pd.read_csv(input, names=('normal1','normal2','normal3',
                                              'primera1','primera2','primera3',
                                              'segunda1','segunda2','segunda3',
                                              'tercera1','tercera2','tercera3')) # modelo 3D
num = len(m)
print(num)
valores = [1*(random() < 0.5) for i in range(num)]
print(valores)

for v in range(len(valores)):
    # print(valores[v])
    if valores[v] == 1:
        valores[v] = 'TRUE'
    elif valores[v] == 0:
        valores[v] = 'FALSE'
print(valores)

m['estado']=valores
m.to_csv('star_0.csv', index = False, header = False)

esquina1_c = m[['primera1','primera2','primera3']]
esquina2_c = m[['segunda1','segunda2','segunda3']]
esquina3_c = m[['tercera1','tercera2','tercera3']]
estado_a = m['estado']
pasos = 5

for p in range(pasos):
    estado_c = []
    for x in range(num):
        esquina1 = esquina1_c.values[x]
        esquina2 = esquina2_c.values[x]
        esquina3 = esquina3_c.values[x]
        estado = estado_a.values[x]
        estados = []
        cambio = 0
        for y in range(num):
            contador = 0
            esquina1_2 = esquina1_c.values[y]
            esquina2_2 = esquina2_c.values[y]
            esquina3_2 = esquina3_c.values[y]
            estadoy = estado_a.values[y]
            if list(esquina1) == list(esquina1_2) or list(esquina1) == list(esquina2_2) or list(esquina1) == list(esquina3_2):
                contador += 1
            if list(esquina2) == list(esquina1_2) or list(esquina2) == list(esquina2_2) or list(esquina2) == list(esquina3_2):
                contador += 1
            if list(esquina3) == list(esquina1_2) or list(esquina3) == list(esquina2_2) or list(esquina3) == list(esquina3_2):
                contador += 1
            if contador == 2:
                estados.append(estadoy)
                if estadoy == 'TRUE':
                    cambio += 1
    
        if cambio > 1:
            estado_c.append('TRUE')
        else:
            estado_c.append('FALSE')
    print(estado_c)
    print('')
    print(valores)
    m['estado'] = estado_c 
    m.to_csv('star_{:d}.csv'.format(p+1), index = False, header = False)
