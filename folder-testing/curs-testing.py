# [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]

def mijloc(lista):
    if len(lista) == 0 :
        return None
    if len(lista) % 2 == 0 :
        return [ ( ( len(lista) // 2 ) -1 , lista[(len(lista) // 2 ) -1] ) , ( len(lista)//2 , lista[len(lista)//2] ) ]
    return (len(lista)//2,lista[len(lista)//2])
    
lista1 = [23,45,29,49,89,93]
lista2 = [14,25,36,47,58]

print(mijloc(lista1))
print(mijloc(lista2))