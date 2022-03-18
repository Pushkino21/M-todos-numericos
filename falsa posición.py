#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 02:06:07 2022

@author: pushkino
"""

import matplotlib.pyplot as plt
import numpy as np

lim = 1

def f(x):
    a = ((np.exp(x-1))-(1.5*x))
    return a

def xr(x_1,x_2,fx_1,fx_2):
    dot = x_2 - ((fx_2 * (x_1-x_2))/(fx_1-fx_2))
    return dot

def plot(pos):
    ax = plt.subplot(10,10,pos)
    #ax.text(3, 8, 'Raiz', style='italic',
     #   bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
    
    plt.xlim(.30,lim)
    plt.ylim(-2,2)
    
    plt.plot(z, f(z),label="e^x-1 - 1.5x")

    #lim_1 = plt.axvline(x=limit_1, ymin=-5, ymax=5, color="blue", linestyle='dashed',label='lim-x1')
    #lim_2 = plt.axvline(x=limit_2, ymin=-5, ymax=5, color="green", linestyle='dashed',label='lim-x2')
    pm = plt.axvline(x=punto, ymin=-5, ymax=5, color="red", linestyle='dashdot',label=str(punto))

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Ploteo función')
    plt.legend(loc='best')

    plt.grid()
    return 
subplot = 1
z = np.linspace(-500, 500, 10000)

fig = plt.figure(figsize=(50,50))
fig.tight_layout()

plt.subplot(10,10,subplot)
#plt.plot(x, h(x))
plt.xlim(-10,10)
plt.ylim(-5,5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Ploteo función')
plt.legend(loc='best')

plt.grid()


plt.plot(z, f(z),label='función')

limit_1 = float(input('Introduzca el primer limite\n'))
limit_2 = float(input('Introduzca el segundo limite\n'))

Q = f(limit_1)
W = f(limit_2)

proof = Q*W

error = 0.001
errorspe = 1

punto = xr(limit_1,limit_2,f(limit_1),f(limit_2))

i=0
limm = .10

if proof < 0:
    
    print("Existe una raiz en el intervalo [",limit_1,",",limit_2,"]")
    errorspe = (punto - f(limit_1))/punto
    print("primer error: ",errorspe)
    
    while errorspe > error:
        
        punto = xr(limit_1,limit_2,f(limit_1),f(limit_2))
        print("Solucion calculada: ",punto)
        errorspe = (punto - f(limit_1))/punto
        proof_2 = f(punto) * f(limit_1)
        print( "El valor de la segunda prueba",proof_2)
        
        if (f(punto) * f(limit_1)) < 0:
            
            limit_1 = punto
            print("limite 1 remplazado: ",limit_1)
            i=i+1
            subplot = subplot+1
            plot(subplot)
            lim = abs(punto +.005)
            limm = limm + .005
            
        elif (f(punto) * f(limit_1)) > 0:
            
            limit_2 = punto
            print("limite 2 remplazado: ", limit_2)
            i=i+1
            subplot = subplot+1
            plot(subplot)
            lim = abs(punto +.005)
            limm = limm + .005
            
        elif (f(punto) * f(limit_1)) == 0 or (f(punto) * f(limit_1)) == 0.0:
            print("Raiz encontrada",punto)
            i=i+1
            subplot = subplot+1
            plot(subplot)
            lim = abs(punto +.005)
            limm = limm + .005
            break
else:
    
    print("Intervalo no valido")
    
print("Valor de raiz aproximada es: ",punto, "\n F(c)= ",f(punto))
print("Iteraciones requeridas: ",i)