# Impartirea si unirea stringurilor
# var = "tata mama fratele sora"
# print(var.split()) # -------> ['tata', 'mama', 'fratele', 'sora'] taie spatiile
# print(var.split('f')) # -------> ['tata mama ', 'ratele sora'] taie litera f si imparte in 2
# var_old = var.split()   # -------> ['tata', 'mama', 'fratele', 'sora']
# new_var = '#'.join(var_old)
# print(new_var) # -------> tata#mama#fratele#sora


# Verificari pe string-uri : startswith, endswith, isalpha, isdigit, isalnum
# text = "Abesei Paul"
# print(text.startswith('A')) # -------> True
# # sau
# print('Abesei Paul'.startswith('A')) # -------> True
# print(text.endswith('l'))   # -------> True
# print(text.isalpha())      # -------> False (are spatiu intre cuvinte)
# print(text.isdigit())  # -------> False (nu toate caracterele sunt cifre)
# print(text.isalnum())  # -------> False (nu toate caracterele sunt alfanumerice, are spatiu)

# Caractere speciale in stringuri : \n \t \\ \' \"
# print("Acesta este un text cu un caracter special: \n new line")
# print("Acesta este un text cu un caracter special: \t tab")
# print('Acesta este un text cu un caracter special: \\ backslash')
# print("Acesta este un text cu un caracter special: \' apostrof")
# print('Acesta este un text cu un caracter special: \" ghilimele')

# Control flux
# Structura if ... elif ... else
# a = 10
# b = 12
# if a<b :
#     print("a este mai mic decat b")
# elif a==b :
#     print("a este egal cu b")
# else :
#     print("a este mai mare decat b")

# Structura for ... in ...
# ------------------------------------------------
# my_str = 'mama are 10 pere'
# for char in my_str : 
#     print(char)
# for cuvant in my_str.split() :
#     print(cuvant)
# ------------------------------------------------
# my_str = 'mama are 10 pere'
# text = ''
# for i in my_str : 
#     if i.isdigit() :
#         text = text + i # text += i <-- concatenare
# print("Cifrele din string sunt: " + text)

# for numar in range(2, 5, 2) :
#     print (numar) # -------> 2, 4

# Structura while ...
# -----------------------------------------------
# numar = 1
# limita = 5
# while numar <= limita :
#     print("Numarul curent este: " + str(numar))
#     numar = numar + 1
# -----------------------------------------------