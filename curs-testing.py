# zip, any, all, list comprehension
# x = [1,2,3]
# y = [4,5,6]

# for a,b in zip(x,y) :
#     print("element zipuite sunt : ", a, "-", b)

# nume =["ana", "maria", "marcel"]
# varsta = [32,54,18]

# for elem_nume, elem_varsta in zip(nume,varsta) :
#     print(elem_nume, " are ", elem_varsta, " ani")

# lista1 = [1,2,3,4,5]
# lista2 = [False, False]
# lista3 = [0,1,2,3,4]
# print(any(lista1)) # -------> true
# print(any(lista2)) # -------> false
# print(any(lista3)) # -------> true
# print(all(lista1)) # -------> true
# print(all(lista3)) # -------> false
# print(all(lista3)) # -------> false

# lista_mea = [x for x in range (1,11) if x % 2 == 0]
# print(lista_mea) # ------> 2,4,6,8,10

# sau

lista_pare = []
for x in range(1,11) :
    if x % 2 == 0 :
        lista_pare.append(x)
print(lista_pare)

# lista_mea = [x**2 for x in range (1,11) if x % 2 == 0]
# print(lista_mea) # ------> 4,16,36,64,100

