# nume = "Paul"
# nume = "Aura"
# print(nume) # Aura deoarece a suprascris peste Paul

# text = 'aici putem scrie un "text" simplu'
# text2 = "Paul's bike is blue."
# text3 = 
# """aici
# putem
# scrie
# pe'
# "mai"
# multe linii."""
# text4 = input("Introdu text aici : ") # se introduce de la tastatura

# print(text)
# print(text2)
# print(text3)
# print(text4)

# # Operatii
# ----------------------------------------
# Adunare -------------------------------
# print(5 + 2)

# text = 'IT School'
# text1 = '2025'
# text2 = text + ' ' + text1
# print (text2) # ------> IT School 2025
# # sau
# print (text + ' ' + text1) # ------> IT School 2025

# Scadere -------------------------------
# print(7 - 4)

# Inmultire ---------------------------
# print(5 * 2)

# text = '2025
# print (text * 100) # ------> printeaza 2025 de 100 ori

# Impartire ---------------------------
# print(5 /2 )

# Impartire intreaga ---------------------------
# print(5//2)

# Impartire cu rest ---------------------------
# print(5%2)

# Ridicare la putere ---------------------------
# print(5**2)

# Logici (True si False): ---------------------------
# and - ambele adevarate
# or - cel putin una adevarata
# not - negarea valorii
# a = 1
# b = 2
# c = 3
# print (a>b and b<c) # False

# Apartenenta in & not in ---------------------------
# print('a' in 'Ana') # True
# print('10' in '10222') # True
# print(10 in [2,56,5,'10']) # False
# print(10 not in [2,56,5,'10']) # True

# Identitate is & is not (catre ce locatie de memorie arata variabelele) ---------------------------
# a = None
# b = None
# print(a is b) # True
# print(a is not b) # False
# ----------------------------------------

# Afisare tip de date
# ----------------------------------------
# text = 'Python'
# numar_intreg = 10
# numar_zecimal = 14.7

# type afiseaza tipul de clasa al variabilei introduse
# print(type(text))
# print(type(numar_intreg))
# print(type(numar_zecimal))
# ----------------------------------------

# Conversii (casting)
# ----------------------------------------
# conversie int la str si concatenare
# text = input("Introdu numele")
# numar_intreg = input("Introdu varsta")
# print(text + ' are : ' + str(numar_intreg) + ' ani') # Ana are : 15 ani

# sau

# nume = input('Inroduce numele: ')
# varsta = input('Introdu varsta: ')
# var1 = 'Salut, {}! {} are {} ani.'.format(nume, nume, varsta)
# # var 1 si var 2 sunt echivalente doar ca e mai simplu de scris si citit cu f string
# var2 = f'Salut, {nume}! {nume} are {varsta} ani.'
# print(var1) # -------> Salut, Paul! Paul are 30 ani.

# rotunjire numar decimail la 4 zecimale
# print(round(3.151592,4)) # 3.1515

# # conversie de la str la int si adunare
# text = "30"
# text2 = input("Introdu un numar")
# print(int(text) + 10 + int(text)) # 30 + 10 + ....

# conversie la bool()
# x = 1
# x = bool(x)
# print(x) #true
# x = 0
# x = bool(x)
# print(x) #false

# conversie la float()
# x = 1
# x = float(x)
# print(x) # 1.0
# ----------------------------------------

# String - len(), slicesing
# ------------------------------------------------
# nume = "Paul"
#         01234
# print(nume[2]) # ------> litera u
# nume = "abracadabra"
# print(len(nume)) # --------> 11 caractere

# var = 'Marius are pere'
# #      012345 678 9.10.11.12
# #                 -4-3-2-1   
# print(var[0]) # ------> M
# print(var[1]) # ------> a
# print(var[-1]) # ------> e
# print(var[-2]) # ------> r
# print(var[-3]) # ------> e
# print(var[-4]) # ------> p

# prints slices from var string 
# print (var[-4::1]) # -------> pere
# print (var[0:5:1]) # -------> Marius

# var1 = var[7:10] # or var1 = var[7:10:1]
# print(var1) # -------> are

# Impartirea si unirea string-urilor
# ------------------------------------------------
# var = "tata mama fratele sora"
# print(var.split()) # -------> ['tata', 'mama', 'fratele', 'sora'] taie spatiile
# print(var.split('f')) # -------> ['tata mama ', 'ratele sora'] taie litera f si imparte in 2
# var_old = var.split()   # -------> ['tata', 'mama', 'fratele', 'sora']
# new_var = '#'.join(var_old)
# print(new_var) # -------> tata#mama#fratele#sora

# Verificari pe string-uri : startswith, endswith, isalpha, isdigit, isalnum
# ------------------------------------------------
# text = "Abesei Paul"
# print(text.startswith('A')) # -------> True
# # sau
# print('Abesei Paul'.startswith('A')) # -------> True
# print(text.endswith('l'))   # -------> True
# print(text.isalpha())      # -------> False (are spatiu intre cuvinte)
# print(text.isdigit())  # -------> False (nu toate caracterele sunt cifre)
# print(text.isalnum())  # -------> False (nu toate caracterele sunt alfanumerice, are spatiu)

# Caractere speciale in string-uri : \n \t \\ \' \"
# ------------------------------------------------
# print("Acesta este un text cu un caracter special: \n new line")
# print("Acesta este un text cu un caracter special: \t tab")
# print('Acesta este un text cu un caracter special: \\ backslash')
# print("Acesta este un text cu un caracter special: \' apostrof")
# print('Acesta este un text cu un caracter special: \" ghilimele')
# ------------------------------------------------

# Liste, subliste, index, bucla for
# ------------------------------------------------
# lista_cumparaturi = ["mere","oua","lapte"]
#       sau
# lista_cumparaturi = [
#     "mere",
#     "oua",
#     "lapte"
#     ]
# lista_preturi = [5,3,8]

# print(lista_cumparaturi[0])
# print(lista_preturi[0])
# print("Pretul pentru " + lista_cumparaturi[0] + " este " + str(lista_preturi[0]) + " RON ")
# print("Pretul pentru " + lista_cumparaturi[1] + " este " + str(lista_preturi[1]) + " RON ")
# print("Pretul pentru " + lista_cumparaturi[2] + " este " + str(lista_preturi[2]) + " RON ")

# lista_liste = [ ["Mere", 5], ["Oua", 3], ["Lapte", 8]]
# print(lista_liste[0]) # -------> []"Mere", 5]

# lista_mere = lista_liste[0] # -------> []"Mere", 5]
# lista_oua = lista_liste[1]
# lista_lapte = lista_liste[2]

# print(lista_mere) # -------> []"Mere", 5]
# print(lista_mere[0]) # -------> Mere
# #       sau
# print(lista_liste[0][0]) # -------> Mere

# print("pretul pentru " + lista_liste[0][0] + " este " + str(lista_liste[0][1]) + " RON.")
# print("pretul pentru " + lista_liste[1][0] + " este " + str(lista_liste[1][1]) + " RON.")
# print("pretul pentru " + lista_liste[2][0] + " este " + str(lista_liste[2][1]) + " RON.")

# lista_cumparaturi = ["oua", "paine", "lapte", "kiwi"]
# for i in lista_cumparaturi :
#     print(i)

# lista_cumparaturi = [ ["oua",1], ["paine",3], ["lapte",8], ["kiwi", 5] ]
# for i in lista_cumparaturi :
#     if i[0] == "paine":
#         print("am gasit")
#     else : 
#         print("produsul " + i[0] + " are pretul " + str(i[1]) + " RON.")
# ------------------------------------------------

# operatorul de comparatie ==
# ------------------------------------------------
# adevarat = True
# fals = False

# print(adevarat) # -------> True
# print(type(adevarat)) # -------> <class 'bool'>
# print(fals) # -------> False
# print(type(fals)) # -------> <class 'bool'>

# numar_1 = 5
# numar_2 = 10
# print(numar_1 == numar_2) # -------> False

# numar_1 = 5
# numar_2 = 5
# print(numar_1 == numar_2) # -------> True

# numar_1 = 5
# numar_2 = "5"
# print(numar_1 == numar_2) # -------> False
# ------------------------------------------------

# Control flux
# Structura if ... elif ... else
# ------------------------------------------------
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
# -----------------------------------------------

# Structura while ...
# -----------------------------------------------
# numar = 1
# limita = 5
# while numar <= limita :
#     print("Numarul curent este: " + str(numar))
#     numar = numar + 1
# -----------------------------------------------

# conditional statements
# ------------------------------------------------
# numar_1 = 5
# numar_2 = 5
# if numar_1 == numar_2 :
#     print("numarul 1 este egal cu numarul 2")

# numar_1 = 20
# numar_2 = 25
# if numar_1 == numar_2 :
#     print("numere egale")
# else :
#     print("numere diferite")

# if int(input("ce varsta ai ? ")) >= 20 :
#      print("ai voie in parc")
# else :
#      print("nu ai voie in parc")
# ------------------------------------------------

# Methods : upper, lower, camel, pascal, append, replace, count, find, strip, lstrip, rstrip
# ------------------------------------------------
# nume = "paul"
# print(nume.upper()) # -----> PAUL

# nume = "PAUL"
# print(nume.lower()) # -----> paul

# lista_fructe = ["banane", "capsuni"]
# print(lista_fructe)
# lista_fructe.append("kiwi")
# print(lista_fructe)
# print(lista_fructe[1])

# var = 'mama tata fratele sora sotia sotul copilul mama'
# print(var.replace('sotia', 'nevasta')) # -------> mama tata fratele sora nevasta sotul copilul mama
# print(var.count('mama')) # -------> 2 ori gasit
# print(var.find('fratele')) # -------> la indexul 10 din string

# nume = '      Abesei Paul      '
# print(nume.strip()) # -------> Abesei Paul (elimina spatiile de la inceput si sfarsit)
# print(nume.lstrip()) # -------> Abesei Paul      (elimina spatiile de la inceput)
# print(nume.rstrip()) # ------->      Abesei Paul (elimina spatiile de la sfarsit)
# ------------------------------------------------

# Modules : import
# ------------------------------------------------
# import random
# lista = [1,2,3,4,5,6,7]
# print(lista)
# random.shuffle(lista) # -------> 5627341
# print(lista)
# ------------------------------------------------

##Quiz2 : len - lungime
# ------------------------------------------------
# import random
# name = input("Care este numele tau ? ")
# print("Multumesc," + " " + name)
# print("Regulile sunt urmatoarele :")
# print("1. Set de intrebari cu punctaj si raspuns cu T sau F")
# print("2. La final se afiseaza scorul")
# scor = 0

# varianta 1 --------------
# lista = ["Suntem pe Terra?", "Suntem in Romania?", "Stai in apartament?", "Ai laptop?", "Ai tricou alb"]
# random.shuffle(lista)
# print("3. O sa avem " + str(len(lista)) + " intrebari")
# for i in lista :
#     print(i)
#     if input() == "t" :
#         print("Raspuns corect")
#         scor = scor + 1
#     else :
#         print("Raspuns gresit")
# -------------

# varianta 2 ---------------
# lista = [] # ------> aici este initializata o lista goala la care se adauga cu .append() elemente in aceasta
# lista.append(["Suntem pe Terra?","t"])
# lista.append(["suntem in Italia", "f"])
# lista.append(["Stai la curte", "f"])
# lista.append(["Ai laptop", "t"])
# lista.append(["Ai tricou alb", "t"])
# print("3. Vei avea " + str(len(lista)) + " intrebari.")
# for i in lista :
#     print(i[0])
#     raspuns = input()
#     if raspuns.lower() == i[1] : #------------> evitam ca utilizatorul sa introduca litera mare chiar daca e raspunsul corect
#         print("Raspuns corect")
#         scor = scor + 1
#     else :
#         print("Raspuns gresit")
# ---------------
# print("Scorul tau este : " + str(scor))
#        #sau 
# if scor == 0 :
#     print("scorul tau este 0 , mai incearca")
# elif scor <=4 :
#     print("scorul tau este " + str(scor) + " , felicitari")
# else :
#     print("Felicitari ai atins scorul maxim de 5 puncte")