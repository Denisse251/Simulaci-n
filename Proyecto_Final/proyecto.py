# -*- coding: utf-8 -*-
"""
Created on Tue May 31 20:51:53 2021

@author: denis
"""

import pandas as pd 
import matplotlib.pyplot as plt
from math import floor, log, sqrt
from random import random, uniform
from os import popen, system
import seaborn as sns

 
l = 10
nc = 10
rc = (10*0.05)/2
na = 50
ra = (10*0.2)/2
nt = 2
rt = (10*0.5)/2
nf = 25
rf = (10*0.005)/2
v = 0.2
vc = 0.75
pc = 0.15
# print(v)

tmax = 30
rcp = ((550*0.05))**2
rap = ((550*0.03))**2
rtp1 = ((550*0.2))**2
rtp2 = ((550*0.03))**2
rfp = ((550*0.005))**2

digitos = floor(log(tmax, 10)) + 1

c = {'C1': 'b', 'C2': 'r', 'CA': 'g', 'CB': 'orange', 'TA': 'g', 'TB': 'r', 'F' : 'k'}
m = {'C1': 'o', 'C2': 'o', 'CA': 'o', 'CB': 'o', 'TA': 'o', 'TB': 'o', 'F' : 'o'}
s = {'C1': rcp, 'C2': rcp, 'CA': rap, 'CB': rap, 'TA': rtp2, 'TB': rtp1, 'F' : rfp}

porcentaje1 = []
porcentaje2 = []
itera = 15
for iteracion in range(itera):
    system('DEL -f p_t*.png') # borramos anteriores en el caso que lo hayamos corrido
    system('DEL -f p.gif')
    
    capsula =  pd.DataFrame()
    capsula['x'] = [uniform((0+rc), (l-rc)) for i in range(nc)]
    capsula['y'] = [uniform((9+rc), (l-rc)) for i in range(nc)]
    capsula['dx'] = [uniform(-vc, vc) for i in range(nc)]
    capsula['dy'] = [uniform(-vc, 0) for i in range(nc)]
    capsula['estado'] = ['C1' for i in range(nc)]
    capsula['carga'] = [True for i in range(nc)]
    
    farmaco = pd.DataFrame()
    farmaco['x'] = []
    farmaco['y'] = []
    farmaco['dx'] = []
    farmaco['dy'] = []
    farmaco['estado'] = []
    farmaco['iden'] = []
    
    for j in range(nc):
        
        cap = capsula.iloc[j]
        x = cap.x
        y = cap.y
        farm = pd.DataFrame()
        farm['x'] = [uniform((x-(rc*0.65)), (x+(rc*0.7))) for i in range(nf)]
        farm['y'] = [uniform((y-(rc*0.65)), (y+(rc*0.7))) for i in range(nf)]
        farm['dx'] = [cap.dx for i in range(nf)]
        farm['dy'] = [cap.dy for i in range(nf)]
        farm['estado'] = ['F' for i in range(nf)]
        farm['iden'] = [j for i in range(nf)]
        farmaco = farmaco.append(farm,ignore_index=True)
    
    cel = pd.DataFrame()
    cel['x'] = [uniform((0+(10*0.03)/2), (l-(10*0.03)/2)) for i in range(na)]
    cel['y'] = [uniform((0+(10*0.03)/2), (9-ra)) for i in range(na)]
    cel['dx'] = [uniform(-v, v) for i in range(na)]
    cel['dy'] = [uniform(-v, v) for i in range(na)]
    cel['estado'] = ['CB' if random() <= pc else 'CA' for i in range(na)]
    cel['med'] = [0 for i in range(na)]
    cel['PH'] = [0.3 if i == 'CB' else 0 for i in (cel['estado'])]
    
    
    
    temp = pd.DataFrame()
    temp['x'] = cel['x']
    temp['y'] = cel['y']
    temp['estado'] = ['TA' if i == 'CA' else 'TB' for i in (cel['estado']) ]
    
    l1 = [x-0.5 for x in range(1,11)]
    l2 = [9.5]*10
    fig = plt.figure(figsize=(9.9,10.15), dpi = 300)
    ax = plt.subplot(1, 1, 1)
    plt.xlim(0, l)
    plt.ylim(0, l)
    ax.plot([0,10],[9.5,9.5],linewidth=(550*0.1), c='orange', alpha = 0.5)
    for e, d in capsula.groupby('estado'):
        if len(d) > 0:
            ax.scatter(d.x, d.y, c = c[e], marker = m[e], s = s[e], alpha = 0.8)
    
    for e, d in cel.groupby('estado'):
        if len(d) > 0:
            ax.scatter(d.x, d.y, c = c[e], marker = m[e], s = s[e], alpha = 0.8)
            
    for e, d in temp.groupby('estado'):
        if len(d) > 0:
            ax.scatter(d.x, d.y, c = c[e], marker = m[e], s = s[e], alpha = 0.25)
    
    for e, d in farmaco.groupby('estado'):
        if len(d) > 0:
            ax.scatter(d.x, d.y, c = c[e], marker = m[e], s = s[e], alpha = 0.8)
    
    fig.savefig('p_t0.png')
    # plt.show()
    plt.close()
    cont_t = temp.estado.value_counts()
    cont_c = capsula.carga.value_counts()
    # print(t_i)
    # print(c_i)
    
    for tiempo in range(tmax):
        
        #movimiento celula
        for a in range(na):
            celula = cel.iloc[a]
            cx = celula.x
            cy = celula.y
            cdx = celula.dx
            cdy = celula.dy
            
            cdx = cdx if cx < (l-(10*0.03)/2) else -(cdx)    
            cdy = cdy if cy < (9-ra) else -(cdy)    
            cdx = cdx if cx > (0+(10*0.03)/2) else -(cdx)
            cdy = cdy if cy > (0+(10*0.03)/2) else -(cdy)
            
            x = cx + cdx
            y = cy + cdy
            
            
            cel.at[a, 'x'] = x
            cel.at[a, 'y'] = y
            temp.at[a, 'x'] = x
            temp.at[a, 'y'] = y
            cel.at[a, 'dx'] = cdx
            cel.at[a, 'dy'] = cdy
        
        #movimieto nanotubos
        for a in range(nc):
            cap = capsula.iloc[a]
            cx = cap.x
            cy = cap.y
            cdx = cap.dx
            cdy = cap.dy
            
            cdx = cdx if cx < (l-(10*0.1)/2) else -(cdx)       
            cdx = cdx if cx > (0+(10*0.1)/2) else -(cdx)
            
            x = cx + cdx
            y = cy + cdy
    
            capsula.at[a, 'x'] = x
            capsula.at[a, 'y'] = y
            capsula.at[a, 'dx'] = uniform(-vc, vc)
            capsula.at[a, 'dy'] = uniform(-vc, 0)
            
    
                
            if cap.carga == True:
                for b in range(a*nf, ((a*nf)+nf)):
                    far = farmaco.iloc[b]
                    iden = (far.iden)
        
                    if a == iden:
                        fx = far.x
                        fy = far.y
                             
                        fx = fx + cdx
                        fy = fy + cdy
                
                        farmaco.at[b, 'x'] = fx
                        farmaco.at[b, 'y'] = fy
                        
                for aa in range(na):
                    tem = temp.iloc[aa]
                    tex = tem.x
                    tey = tem.y
                    
                    if tem.estado == 'TB':
                        d = sqrt((x - tex)**2 + (y - tey)**2)
                                
                        if d < ((rc/2)+(rt/2)):
                            capsula.at[a, 'carga'] = False
            
            else:
                for b in range(a*nf, ((a*nf)+nf)):
                    far = farmaco.iloc[b]
                    iden = (far.iden)
        
                    if a == iden:
                        fx = far.x
                        fy = far.y
                        fdx = far.dx
                        fdy = far.dy

                        fdx = fdx/2
                        fdy = fdy/2

                        fuerzax = []
                        fuerzay = []
                        fuerzax.append(fdx)
                        fuerzay.append(fdy)
                        for j in range(na):
                            celula = cel.iloc[j]
                            tem = temp.iloc[j]
                            cx = celula.x
                            cy = celula.y
                            conteo = celula.med
                            if tem.estado == 'TB':
    
                                d = sqrt((cx - fx)**2 + (cy - fy)**2)
                                f = celula.PH / d
                
                                fuerzax.append(((cx - fx)*f)/d)
                                fuerzay.append(((cy - fy)*f)/d)
                                dt = (10*0.04)/2+rf
    
                                if d <= dt:
                                    
                                    cel.at[j, 'med'] = conteo + 1
                                
                                if celula.med > 3:
                                    temp.at[j, 'estado'] = 'TA'
                                    cel.at[j, 'estado'] = 'CA'
                                    cel.at[j, 'PH'] = 0
    
                        fdx = sum(fuerzax)
                        fdy = sum(fuerzay)
                        fdx = fdx if fx < (l-(10*0.005)/2) else -(fdx)       
                        fdx = fdx if fx > (0+(10*0.005)/2) else -(fdx)
                        
                        fdy = fdy if fy < (9-(10*0.005)/2) else -(fdy)       
                        fdy = fdy if fy > (0+(10*0.005)/2) else -(fdy)
                        
                        fx = fx + fdx
                        fy = fy + fdy
                        
                        fy = fy if fy < (9-(10*0.005)/2) else (9-(10*0.005)/2)
                        
                        farmaco.at[b, 'x'] = fx
                        farmaco.at[b, 'y'] = fy
                        farmaco.at[b, 'dx'] = uniform(-vc, vc)
                        farmaco.at[b, 'dy'] = uniform(-vc, vc)
    
    
        fig = plt.figure(figsize=(9.9,10.15), dpi = 300)
        ax = plt.subplot(1, 1, 1)
        plt.xlim(0, l)
        plt.ylim(0, l)
        ax.plot([0,10],[9.5,9.5],linewidth=(550*0.1), c='orange', alpha = 0.5)
        for e, d in capsula.groupby('estado'):
            if len(d) > 0:
                ax.scatter(d.x, d.y, c = c[e], marker = m[e], s = s[e], alpha = 0.8)
        
        for e, d in cel.groupby('estado'):
            if len(d) > 0:
                ax.scatter(d.x, d.y, c = c[e], marker = m[e], s = s[e], alpha = 0.8)
                
        for e, d in temp.groupby('estado'):
            if len(d) > 0:
                ax.scatter(d.x, d.y, c = c[e], marker = m[e], s = s[e], alpha = 0.25)
        
        for e, d in farmaco.groupby('estado'):
            if len(d) > 0:
                ax.scatter(d.x, d.y, c = c[e], marker = m[e], s = s[e], alpha = 0.8)
        
        fig.savefig('p_t' + format(tiempo + 1, '0{:d}'.format(digitos)) + '.png')
        plt.close()
    cont2_t = temp.estado.value_counts()
    cont2_c = capsula.carga.value_counts()
    c_i = cont_c
    c_f = cont2_c
    t_i = cont_t
    t_f = cont2_t
    ti = 50 - t_i['TA']
    tf = 50 - t_f['TA']
    por1 = ((ti - tf) / ti) * 100
    ci = c_i[True]
    cf = 10 - c_f[False]
    por2 = ((ci - cf) / ci) * 100
    porcentaje1.append(por1)
    porcentaje2.append(por2)
    popen('magick convert -delay 35 -size 300x300 p_t*.png -loop 0 p.gif') # requiere ImageMagick

df = pd.DataFrame(
    {"Variables": ["Cel"] * itera + ["Cap"] * itera,
     "Porcentaje": porcentaje1 + porcentaje2}
     )
print(df)
pd.set_option("display.max_rows", None, "display.max_columns", None)
ax = sns.violinplot(x='Variables', y='Porcentaje', data=df, scale='count', inner="box"  ,cut = 0)
plt.savefig('p.png', dpi=300)
plt.show()
plt.close()