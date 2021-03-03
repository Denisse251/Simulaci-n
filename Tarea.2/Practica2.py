# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 23:45:33 2021

@author: denis
"""
import numpy as np 
from random import random
import matplotlib.cm as cm
import matplotlib.pyplot as plt


dim = 12
num = dim**2
p = 0.5
valores = [1*(random() < p) for i in range(num)]
print(valores)
actual = np.reshape(valores,(dim,dim))
print("El actual es: ", actual)
valor_a = []

def mapeo(pos):
    fila = pos // dim
    columna = pos % dim
    return actual[fila, columna]

assert all([mapeo(x) == valores[x] for x in range(num)])


def paso(pos, reglas):
    fila = pos // dim
    columna = pos % dim
    actual_o = actual
    if fila == 0:
        actualn = actual_o[[dim-1],:]
        actualm = actual_o[[i for i in range(dim-1)],:]
        actual_o = np.append(actualn,actualm, axis=0)
        fila += 1

    elif fila == dim-1:
        actualn= actual_o[[0],:]
        actualm= actual_o[[i for i in range(1,dim)],:]
        actual_o = np.append(actualm,actualn, axis=0)
        fila -= 1

    if columna == 0:
        actualn= actual_o[:,[dim-1]]
        actualm= actual_o[:,[i for i in range(dim-1)]]
        actual_o = np.append(actualn,actualm, axis=1)
        columna += 1

    elif columna == dim-1:
        actualn= actual_o[:,[0]]
        actualm= actual_o[:,[i for i in range(1,dim)]]
        actual_o = np.append(actualm,actualn, axis=1)
        columna -= 1

        
    vecindad = actual_o[max(0, fila -1):min(dim, fila + 2),
              max(0, columna -1):min(dim, columna +2)]
    actual_f=actual_o
    actual_o=actual
    vecinos = (np.sum(vecindad) - actual_f[fila, columna])

    if reglas == 1:
        return 1 * (vecinos == 3)
    
    elif reglas == 2:
        if vecinos == 3:
            regla = True
            
        elif vecinos == 2:
            regla = 1 * (random() < 0.5)
        elif vecinos == 4:
            regla = 1 * (random() < 0.5)
        else:
            regla = False
           
        return 1 * (regla)
    
    elif reglas == 3:
        valor_a.append(valores[pos])
        
        if vecinos == 3:
            regla = True
            
        elif vecinos == 2:
            
            if valor_a[pos] == 1:
                regla = True
            else:
                regla = 1 * (random() < 0.5)

        elif vecinos == 4:
 
            if valor_a[pos] == 1:
                regla = True

            else:
                regla = 1 * (random() < 0.5)

        else:
            regla = False

        return 1 * (regla)
        
    elif reglas == 4:
        if vecinos == 1:
            regla = 1 * (random() < 0.2)
            
        elif vecinos == 2:
            regla = 1 * (random() < 0.3)
        
        elif vecinos == 3:
            regla = 1 * (random() < 0.5)
        
        elif vecinos == 4:
            regla = 1 * (random() < 0.35)
        
        elif vecinos == 5:
            regla = 1 * (random() < 0.6)
        
        elif vecinos == 6:
            regla = 1 * (random() < 0.05)
        
        elif vecinos == 7:
            regla = 1 * (random() < 0.85)
        
        elif vecinos == 8:
            regla = 1 * (random() < 0.02)
        
        else:
            regla = 1 * (random() < 0.01)
        
        return 1 * (regla)
    
    
    elif reglas == 5:
        if vecinos % 2 == 0:
            regla = 1 * (random() < 0.5) 
        else:
            regla = 1 * (random() < 0.01)
        
        return 1 * regla
    else:
        print("El numero de regla no existe")
        return 1 * False
        
if __name__ == "__main__":
    vi_t = []
    for reglas in range(1,6):
        fig = plt.figure()
        plt.imshow(actual, interpolation='nearest', cmap=cm.Greys)
        fig.suptitle('Estado inicial')
        
        va, vi =  [], []
        plt.savefig('p2_r{:d}_t0_p.png'.format(reglas))
        plt.close()
        plt.show()
        actual_i = actual
        # print(actual_i)
        valores_i = valores
        vivos = sum(valores)
        vi.append(vivos)
        for iteracion in range(30):
            
            valores = [paso(x,reglas) for x in range(num)]
            va.append(valores)
            
            vivos = sum(valores)
            vi.append(vivos)
            # print(vi)
            if vivos == 0:
                print('# Ya no queda nadie vivo.')
                break;
            actual = np.reshape(valores, (dim, dim))
            fig = plt.figure()
            plt.imshow(actual, interpolation='nearest', cmap=cm.Greys)
            fig.suptitle('Paso {:d}'.format(iteracion + 1))
            plt.savefig('p2_r{1:d}_t{0:d}_p.png'.format((iteracion + 1),reglas))
            plt.close()
            plt.show()
        actual = actual_i
        valores = valores_i
        vi_t.append(vi)
    print(vi_t)
    
    # fig = plt.figure()
    # gs = fig.add_gridspec(5,1, hspace=1.5)
    # ax1 = fig.add_subplot(gs[0])
    # ax1.plot(vi_t[0])
    # ax1.set_title('Regla 1')
    # ax1.set(ylabel='Vivos')
    # ax2 = fig.add_subplot(gs[1])
    # ax2.plot(vi_t[1])
    # ax2.set_title('Regla 2')
    # ax2.set(ylabel='Vivos')
    # ax3 = fig.add_subplot(gs[2])
    # ax3.plot(vi_t[2])
    # ax3.set_title('Regla 3')
    # ax3.set(ylabel='Vivos')
    # ax4 = fig.add_subplot(gs[3])
    # ax4.plot(vi_t[3])
    # ax4.set_title('Regla 4')
    # ax4.set(ylabel='Vivos')
    # ax5 = fig.add_subplot(gs[4])
    # ax5.plot(vi_t[4])
    # ax5.set_title('Regla 5')
    # ax5.set(ylabel='Vivos')
    fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, sharex= True, sharey = True)
    fig.suptitle('Gráficas de vida durante las iteraciones, de la regla 1 a la 5')
    ax1.plot(vi_t[0])
    ax1.set(ylabel='Vivos')
    ax2.plot(vi_t[1])
    ax2.set(ylabel='Vivos')
    ax3.plot(vi_t[2])
    ax3.set(ylabel='Vivos')
    ax4.plot(vi_t[3])
    ax4.set(ylabel='Vivos')
    ax5.plot(vi_t[4])
    ax5.set(xlabel='Iteraciones',ylabel='Vivos')
    
    plt.savefig('Grafica de vida', dpi=300)
# print(va)

