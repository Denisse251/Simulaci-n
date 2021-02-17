# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 19:01:43 2021

@author: denis
"""
from random import random,randint
import matplotlib.pyplot as plt
import multiprocessing

def practica1(dimension):

    for e in range (6):
        exponencial = e + 4
        exp= 2**exponencial
        print ('con numero de paso de', exp)
     
        
        pinicial = [0] * dimension
        res = []
        rep = 30
        
        
        for nr in range (rep) :
            nunca = True 
            
            
            for paso in range (exp):
                dim = randint(0,dimension-1)
                pinicial[dim]=pinicial[dim]+ 1 if random() < 0.5 else pinicial[dim] - 1
                
                if all ([p==0 for p in pinicial]):
                    res.append(paso)
                    nunca = False
                    
                    break
            if nunca:
                res.append(None)
        cuantos = sum([r is None for r in res])
        print ( cuantos/rep,'no regresaron nunca en la dimension', dimension)
        
        if cuantos < rep:
            regresaron = sum([r if r is not None else 0 for r in res])
            print (regresaron/(rep- cuantos), 'fue la tardanza en promedio en la dimensión', dimension)
            
if __name__ == "__main__":
     # practica1(2)
    # dimension = [d for d in range(1, 2)]
    # p = [(d) for d in dimension]
    # print(p, dimension)
    job=[]
    for i in range(1,6):
        p1 = multiprocessing.Process(target=practica1, args=(i,))
        job.append(p1)
        p1.start()
    # with multiprocessing.Pool() as pool:
    #     inicio = pool.map(practica1, p)
    # print(inicio)
   
   
        
    