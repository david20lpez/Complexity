# -*- coding: utf-8 -*-

def factorial(numero):
    if(not isinstance(numero, int) or numero < 0):
        print("Número no válido")
    elif(numero == 0):
        return 0
    else:
        i = 1
        acumulado = 1
        while(i <= numero):
            acumulado = acumulado * i
            i = i + 1
        return acumulado

def combinacion(n,k):
    if(k >= n or not isinstance(k, int) or not isinstance(n, int) or k < 1 or n < 1):
        print("Número no válido")
    else:
        return factorial(n)/(factorial(k)*factorial(n - k))

print(combinacion(400,270))