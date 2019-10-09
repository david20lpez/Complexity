# -*- coding: utf-8 -*-
import math

def fibonacci(numero):
    if(numero < 1):
        print("número no válido")
        return None
    elif(numero == 1):
        return 0
    elif(numero == 2):
        return 1
    else:
        serie = []
        serie.append(0)
        serie.append(1)
        i = 2
        while(i < numero):
            serie.append(serie[i-1]+serie[i-2])
            i = i + 1
    print(serie)
    return serie[numero-1]

def serieFib(numero):
    if(numero < 1):
        print("número no válido")
    elif(numero == 1):
        return 0
    elif(numero == 2):
        return 1
    elif(numero < 1):
        return 0
    else:
        return int((((1 + math.sqrt(5))/2)**(numero -1) - ((1 - math.sqrt(5))/2)**(numero - 1))/math.sqrt(5))

print(fibonacci(4))
print(serieFib(4))