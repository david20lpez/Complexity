# -*- coding: utf-8 -*-
import random

def llenar(vec):
    posicion = 0
    while(posicion < len(vec)):
        vec[posicion] = random.randint(0,9999)
        posicion = posicion + 1
    return vec

vector = [0]*30
llenar(vector)

print(vector)