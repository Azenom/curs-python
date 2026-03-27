'''# 133. Sa se scrie un program care citeste un fisier text numit "date.txt" si afiseaza numarul de linii, cuvinte si caractere din fisier. '''

# spatii = 1 # numarul de spatii este mai mic cu 1 decat numarul de cuvinte dintr-o propozitie
# count_spatii = 0
# caracter = 0
# count_caracter = 0
# with open("date.txt", 'r') as my_file :
#    linii_fisier = my_file.readlines()

# print(f'Fisierul are : {len(linii_fisier)} linii') # numarul de linii
# for index in linii_fisier : # parcurgi index-urile din lista
#    for litera in index : # parcurgi propozitia din index din lista
#       if litera == " ":
#          spatii += 1
#       elif litera != "\n":
#          caracter += 1
#    count_spatii += spatii
#    count_caracter += caracter
#    spatii = 1 # resetez numarul de spatii memorate inainte sa treaca la urmatoarea linie
#    caracter = 0 # resetez numarul de caractere memorate inainte sa treaca la urmatoarea linie
# print("Numarul de cuvinte este : ",count_spatii)
# print("Numarul de caractere este : ",count_caracter)

# sau

# with open("date.txt", 'r', encoding='utf-8') as fisier:
#     continut = fisier.read()
# nr_linii = len(continut.splitlines())
# nr_cuvinte = len(continut.split())
# caractere = 0
# for i in continut:
#     if i != " " and i != "\n":
#         caractere = caractere +1
# print(f"Rezultate\n Numar linii: {nr_linii} \n Numar cuvinte: {nr_cuvinte} \n Numar caractere: {caractere}")