# -*- coding: utf-8 -*-

def esPrimo(numero):
    if(not isinstance(numero, int) and not numero > 1):
        return False
    num = 1
    primo = 0
    while(num <= numero):
        if(numero%num == 0):
            primo = primo + 1
            print(num)
        num = num + 1
    if(primo > 2):
        return False
    else:
        return True


number = raw_input('Ingrese un número: ')

print(esPrimo(int(number)))
        
    
    