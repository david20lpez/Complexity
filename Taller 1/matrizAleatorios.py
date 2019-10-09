# -*- coding: utf-8 -*-
import random

def llenar(matriz):
    i = 0 #posición fila
    j = 0 #posición columna
    while(i < len(matriz)):
        fila = []
        while(j < len(matriz[i])):
            fila.append(random.randint(0,9999))
            j = j + 1
        print(fila)
        matriz[i] = fila
        j = 0 
        i = i + 1

matrizriz = [[0]*5]*3
llenar(matrizriz)
print(matrizriz)