# -*- coding: utf-8 -*-
def sumatoria(numero):
    if(not isinstance(numero, int)):
        print("el número no es entero")
    else:
        num = 0
        suma = 0
        while(num < numero):
            num = num + 1
            #print(str(suma) + "+"  + str(num))
            suma = suma + num
    return suma

number = raw_input("Ingrese número: ")

def serieSumatoria(numero):
    if(not isinstance(numero, int)):
        print("el número no es entero")
    else:
        return (numero*(numero + 1))/2

#print("la sumatoria es: " + str(serieSumatoria(int(number))))
print(sumatoria(int(number)))