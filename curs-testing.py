# 48. Primește o listă de stringuri și sorteaz-o crescător după numărul de vocale din fiecare string.
# Fara a folosi functia sort() sau sorted().
# # Exemplu: ['ana', 'mere', 'casa', 'masina'] -> ['ana', 'casa', 'mere', 'masina']

lista  = ['ana', 'mere', 'casa', 'masina']
vocale = 'aeiou'
flag = ''
for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        count_i = sum(1 for char in lista[i] if char in vocale)
        count_j = sum(1 for char in lista[j] if char in vocale)
        if count_i > count_j:
            flag = lista[i]
            lista[i] = lista[j]
            lista[j] = flag
print(lista)   