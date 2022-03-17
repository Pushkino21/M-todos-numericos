#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 20:15:17 2022

@author: pushkino
"""
import matplotlib.pyplot as plt
import numpy as np
global subplot
subplot = 1
#funcion
def h(x):
    a = ((np.exp(x-1))-(1.5*x))
    return a

def plot(pos):
    ax = plt.subplot(5,5,pos)
    
    plt.xlim(limit_1,limit_2)
    plt.ylim(-2,2)
    
    plt.plot(x, h(x),label='función')

    lim_1 = plt.axvline(x=x_1, ymin=-5, ymax=5, color="blue", linestyle='dashed',label='lim-x1')
    lim_2 = plt.axvline(x=x_2, ymin=-5, ymax=5, color="green", linestyle='dashed',label='lim-x2')
    pm = plt.axvline(x=mitteldot, ymin=-5, ymax=5, color="red", linestyle='dashdot',label='punto medio')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Ploteo función')
    plt.legend(loc='best')

    plt.grid()
    return 

#Valores en los que evaluamos f(x)
x = np.linspace(-500, 500, 10000)


fig = plt.figure(figsize=(30,30))
fig.tight_layout()

plt.subplot(5,5,subplot)
#plt.plot(x, h(x))
plt.xlim(-10,10)
plt.ylim(-5,5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Ploteo función')
plt.legend(loc='best')

plt.grid()


plt.plot(x, h(x),label='función')
#plt.show()
#print(fx)
#lim_1 = plt.axvline(x=x_1, ymin=-5, ymax=5, color="blue", linestyle='dashed',label='lim-x1')
#lim_2 = plt.axvline(x=x_2, ymin=-5, ymax=5, color="green", linestyle='dashed',label='lim-x2')
#pm = plt.axvline(x=mitteldot, ymin=-5, ymax=5, color="red", linestyle='dashdot',label='punto medio')



#Valores para el intervalo captura
limit_1 = float(input("Introduzca el primer limite del intervalo que desea probar\n"))
limit_2 = float(input("Introduzca el segundo limite del intervalo que desea probar\n "))

x_1 = limit_1
x_2 = limit_2
    
error_esp = 0.00001

error = 1
   
while error > error_esp:
    
    mitteldot = (x_1+x_2)/2
    #Evaluación de los valores limites para hallar la raiz
    fa=h(x_1)
    print("Función evaluada en el limite uno: ",fa)
    fb=h(x_2)
    print("Función evaluada en el limite dos: ",fb)
    fc=h(mitteldot)
    print("Función evaluada en el punto medio: ",fc)
        
    if fa < 0 and fb > 0 and fc < 0:
    
            print('Ambos, limite uno: ',x_1,' y punto medio: ',mitteldot,' son negativos\n punto medio será el siguiente limite negativo')
    
            x_1 = mitteldot
    
            print(mitteldot)
            subplot=subplot+1
            
            plot(subplot)
            error = (x_2-x_1)/2
            #plot()
            #fc=h(mitteldot)
            #if fc == 0:
             #   print('Raiz encontrada',fc)
            #else:
             #       pass

    elif fa < 0 and fb > 0 and fc > 0:    

            print('Ambos\n limite dos: ',x_2,' y punto medio: ',mitteldot,' son positivos\n punto medio será el siguiente limite positivo')
    
            x_2 = mitteldot
    
            #mittel = x_2+x_1
            #print(mittel)
            subplot=subplot+1
    
            plot(subplot)
            error = (x_2-x_1)/2
            #plot()
            #fc=h(mittel)
            #if fc == 0:
             #   print('Raiz encontrada',fc)
            #else:
             #   pass

    elif fa > 0 and fb < 0 and fc < 0:
    
            print('Ambos\n limite dos: ',x_2,' y punto medio: ',mitteldot,' son negativos\n punto medio será el siguiente limite negativo')
    
            x_2 = mitteldot
    
            #mittel = x_2+x_1
    
            subplot=subplot+1
            plot(subplot)
            error = (x_2-x_1)/2
            #plot()
            #fc=h(mittel)
            #if fc == 0:
             #   print('Raiz encontrada = ',mittel,'F(c) = ',fc)
            #else:
             #   pass
    
    elif fa > 0 and fb < 0 and fc > 0:
    
            print('Ambos\n limite uno: ',x_1,' y punto medio: ',mitteldot,' son positivos\n punto medio será el siguiente limite positivo')
    
            x_1 = mitteldot
    
            #mittel = (x_1+x_2)/2
    
            subplot=subplot+1
            plot(subplot)
            error = (x_2-x_1)/2
            #plot()
            #fc=h(mittel)
            #if fc == 0:
             #   print('Raiz encontrada',fc)
            #else:
             #   pass
            
    print('Error de calculo del: ',error*100)
    print('Raiz aproximada: ',mitteldot, '\n F(x)= ',h(mitteldot))
    #mitteldot = mitteldot
    #error = (x_2-x_1)/2