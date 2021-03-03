# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 13:14:32 2021

@author: denis
"""

import pandas as pd
import re
import random

lines = []
primo = []
primos = []
nprimos = []
pares = []
primos_nprimos = []
nprimos_primos = []
aleatorio = []

#Abrir el archivo txt y convertirlo a un unico vector
with open('primes3.txt', 'r') as in_file:
        for line in in_file:
            if line != '\n':
                txt = re.split(r'\D',line)
                lines.append(txt)
print(len(lines[1]))

#Del vector lines, se eliminan las celdas vacias dejando solo los numeros primos
for x in range(1, len(lines)):
    for y in range(len(lines[x])):
        if lines[x][y] != '':
            primo.append(int(lines[x][y]))
            
cantidad = 10000

#Con la variable cantidad, se seleccionan los primeros numeros del vector primo
for x in range(cantidad):
    primos.append(primo[x])

#Obtengo los numeros no primos que no sean pares, calculando la mitad entre cada numero primo
for x in range(len(primos)):
    if x < len(primos)-1:
        num =((primos[x]-primos[x+1])/2)+primos[x]
        if num % 2 == 0:
            num += 1
        nprimos.append(int(num))
        
    else:
        num = primos[x] + 2
        nprimos.append(int(num))
        break

#obtengo los puros numeros pares, sumando un uno a los numeros primos
for x in range(len(primos)):
    num = primos[x]+1
    pares.append(num)

#obtengo la mitad de numeros primos y la otra midad de numeros no primos
for x in range(int(len(primos)/2)):
    primos_nprimos.append(primos[x])

for x in range(int(len(nprimos)/2)):
    primos_nprimos.append(nprimos[x])
print(len(primos_nprimos))

#obtengo la inversa del vector de numeros primos y no primos
nprimos_primos = primos_nprimos[::-1]

#obtengo una distribucion aleatoria de numeros primos y no primos
aleatorio = primos_nprimos
random.shuffle(aleatorio)

#guardo todos los numeros en una tala o matriz 
data = {'Primos':primos, 
                'No_Primos':nprimos, 
                'Pares':pares,
                'Primos_NoPrimos': primos_nprimos,
                'NoPrimos_Primos': nprimos_primos,
                'Aleatorio': aleatorio} 
df = pd.DataFrame(data)
print(df)

#paso la tabla o matriz a un csv para su uso
df.to_csv('C:/Users/denis/OneDrive/Documentos/maestria/Segundo Semestre/Simulación computacional de nanomateriales/practicas/Practica3/numeros.csv')
