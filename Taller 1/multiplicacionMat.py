# -*- coding: utf-8 -*-
import random

def mult(mat1, mat2):
    mat = []
    if(not len(mat1[0]) == len(mat2)):
        print("matrices no multiplicables entre sí")
    else:
        i = 0
        j = 0
        k = 0
        acumulado = 0
        while(i < len(mat1)):
            fila =  []
            while(j < len(mat2[0])):
                while(k < len(mat1[0])):
                    acumulado = acumulado + mat1[i][k]*mat2[k][j]
                    k = k + 1
                fila.append(acumulado)
                acumulado = 0
                k = 0
                j = j + 1
            j = 0
            mat.append(fila)
            i = i + 1
    return mat


def llenar(mat):
    i = 0
    j = 0
    while(i < len(mat)):
        col = []
        while(j < len(mat[i])):
            col.append(random.randint(0,9))
            j = j + 1
        mat[i] = col
        j = 0 
        i = i + 1

matriz1 = [[0]*3]*4
matriz2 = [[0]*4]*3

llenar(matriz1)
llenar(matriz2)

print(matriz1)
print(matriz2)

print(mult(matriz1, matriz2))
