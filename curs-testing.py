# 8) Elimină toate elementele pare dintr-o listă de numere.
# Exemplu: [1,2,3,4,5,6] -> [1,3,5]
lista = [1,2,3,4,5,6]
for i in lista :
    if i % 2 == 0 :
        lista.remove(i)
print(lista)