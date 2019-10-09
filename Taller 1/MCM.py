# -*- coding: utf-8 -*-

def mcm(numero1, numero2):
    if(numero1 < 1 or numero2 < 1):
        print("Números no válidos")
    elif(numero1 == numero2):
        return numero1
    else:
        i=numero1*numero2
        multiplosComunes = []
        while(i > numero1 and i > numero2):
            if(i%numero1 == 0 and i%numero2 == 0):
                multiplosComunes.append(i)
            i = i - 1
        print(multiplosComunes)
        return multiplosComunes[len(multiplosComunes)-1]
            
    

print(mcm(44,63))