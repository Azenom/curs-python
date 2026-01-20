# ------------------------------------------------------ Afisare date ----------------------------------------------------------------------

# text = 'Python'
# nume = "Paul"
# nume = "Aura"
# text1 = 'textul este un "text" simplu'
# text2 = "Paul's bike is blue."
# text3 = """chiar 
# daca scriem
# text la 'olalta
# pe "mai"
# multe linii."""
# text4 = input("Introdu text aici : ") # se introduce de la tastatura

# print(nume) # ------> Aura deoarece a suprascris peste Paul
# print(text1) # ------> textul este un "text" simplu
# print(text2) # ------> Paul's bike is blue.
# print(text3) # afiseaza :     chiar 
#                               daca scriem
#                               text la 'olalta
#                               pe "mai"
#                               multe linii.
# print(text4) # afiseaza textul introdus de la tastatura

# ----------------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------ Operatii ---------------------------------------------------------------------
# Adunare ------------------------------------------------

# print(5 + 2)
# text = 'IT School'
# text1 = '2025'
# text2 = text + ' ' + text1
# print (text2) # ------> IT School 2025
# print (text + ' ' + text1) # ------> IT School 2025

# Scadere ------------------------------------------------

# print(7 - 4) # ------> 3

# Inmultire ------------------------------------------------

# print(5 * 2) # ------> 10
# text = '2025'
# print (text * 100) # ------> printeaza 2025 de 100 ori

# Impartire ------------------------------------------------

# print(5 /2 ) # ------> 2.5

# Impartire intreaga ------------------------------------------------

# print(5//2) # ------> 2

# Impartire cu rest ------------------------------------------------

# print(5%2) # ------> 1

# Ridicare la putere ------------------------------------------------

# print(5**2) # ------> 25

# Comparatie == ------------------------------------------------

# numar_1 = 5
# numar_2 = 10
# print(numar_1 == numar_2) # -------> False

# numar_1 = 5
# numar_2 = 5
# print(numar_1 == numar_2) # -------> True

# numar_1 = 5
# numar_2 = "5"
# print(numar_1 == numar_2) # -------> False

#-----------------------------------------------------------------------------------------------------------------------------------------

# ----------------------------- Operatori Logici (True si False), Apartenta in / not in, Identitate is & is not --------------------------

# and - ambele adevarate
# or - cel putin una adevarata
# not - negarea valorii
# a = 1
# b = 2
# c = 3
# print (a>b and b<c) # False

# print('a' in 'Ana') # ------> True
# print('10' in '10222') # ------> True
# print(10 in [2,56,5,'10']) # ------> False
# print(10 not in [2,56,5,'10']) # ------> True

# a = None
# b = None
# print(a is b) # True
# print(a is not b) # False

# ------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------ Control flux ------------------------------------------------
# Structura if ... elif ... else ------------------------------------------------

# a = 10
# b = 12
# if a<b :
#     print("a este mai mic decat b")
# elif a==b :
#     print("a este egal cu b")
# else :        # ------- > daca a nu este mai mic si nici egal cu b
#     print("a este mai mare decat b")

# -----------------------------------------------

# Structura for ... in ... ------------------------------------------------

# my_str = "python"
# for char in my_str : 
#     print(char) # --------> afiseaza fiecare caracter pe linie noua : p
#                                                                       y
#                                                                       t
#                                                                       h
#                                                                       o
#                                                                       n

# -----------------------------------------------

# Structura while ... -----------------------------------------------

# numar = 1
# limita = 5
# while numar <= limita :
#     print("Numarul curent este: " + str(numar))
#     numar = numar + 1

# -----------------------------------------------

# Structura if ... else ... ------------------------------------------------

# numar_1 = 5
# numar_2 = 5

# if numar_1 == numar_2 :
#     print("numarul 1 este egal cu numarul 2")

# if int(input("ce varsta ai ? ")) >= 20 :
#      print("ai voie in parc")
# else :
#      print("nu ai voie in parc")

# -------------------------------------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------Conversii ---------------------------------------------------------------------
# Conversie int(), str(), bool(), float(), list(), rotunjire  ----------------------------------------

# text = input("Introdu numele")
# numar_intreg = input("Introdu varsta")
# print(text + ' are : ' + str(numar_intreg) + ' ani') # Ana are : 15 ani

# text = "30"
# text2 = input("Introdu un numar")
# print(int(text) + 10 + int(text)) # -------> 30 + 10 + ....

# sau 

# nume = input('Inroduce numele: ')
# varsta = input('Introdu varsta: ')
# var1 = 'Salut, {}! {} are {} ani.'.format(nume, nume, varsta)
# # var 1 si var 2 sunt echivalente doar ca e mai simplu de scris si citit cu f string
# var2 = f'Salut, {nume}! {nume} are {varsta} ani.'
# print(var1) # -------> Salut, Paul! Paul are 30 ani.

# x = 1
# x = bool(x)
# print(x) # --------> true
# x = 0
# x = bool(x)
# print(x) # --------> false

# x = 1
# x = float(x)
# print(x) # -------> 1.0

# text = "Python"
# lista = list(text)
# print(lista) # -------> ['P', 'y', 't', 'h', 'o', 'n']

# sau 

# numar = 12345
# lista_cifre = list(str(numar)) # -------> int is not iterable, convertim la str si apoi la lista
# print(lista_cifre) # -------> ['1', '2', '3', '4', '5']

# Rotunjire numar decimail la 4 zecimale
# print(round(3.151592,4)) # --------> 3.1515

# lista = [7,5,3,2,0]
# print(lista) # -------> [7, 5, 3, 2, 0]
# print(lista.sort()) # -------> [0, 2, 3, 5, 7] # sorteaza lista, nu o modifica

# ----------------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------- Modificari pe string/liste ----------------------------------------------------------------- 
# Slicesing, split(), join(), zip(), sort() ------------------------------------------------

# nume = "Paul"
#         01234
# print(nume[2]) # ------> litera u

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

# var1 = var[7:10] 
# # sau
# var1 = var[7:10:1]
# print(var1) # -------> are

# var = "tata mama fratele sora"
# print(type(var)) # -------> <class 'str'>
# print(var.split()) # -------> ['tata', 'mama', 'fratele', 'sora'] taie spatiile
# print(var.split('f')) # -------> ['tata mama ', 'ratele sora'] taie litera f si imparte in 2
# var_old = var.split()   # -------> ['tata', 'mama', 'fratele', 'sora']
# print(type(var_old)) # -------> <class 'list'>
# new_var = '#'.join(var_old)
# print(type(new_var)) # -------> <class 'str'>
# print(new_var) # -------> tata#mama#fratele#sora

# my_str = 'mama are 10 pere'
# for cuvant in my_str.split() :
#     print(cuvant) # afiseaza fiecare cuvant pe linie noua

# x = [1,2,3]
# y = [4,5,6]
# for a,b in zip(x,y) :
#     print("element zipuite sunt : ", a, "-", b)

# nume =["ana", "maria", "marcel"]
# varsta = [32,54,18]
# for elem_nume, elem_varsta in zip(nume,varsta) :
#     print(elem_nume, " are ", elem_varsta, " ani")

# lista = [7,5,3,2,0]
# print(lista)
# lista.sort()
# print(lista)

# ------------------------------------

# Stergerea spatiilor strip(), lstrip(), rstrip() ------------------------------------------------

# nume = '      Abesei Paul      '
# print(nume.strip()) # -------> Abesei Paul (elimina spatiile de la inceput si sfarsit)
# print(nume.lstrip()) # -------> Abesei Paul      (elimina spatiile de la inceput)
# print(nume.rstrip()) # ------->      Abesei Paul (elimina spatiile de la sfarsit)

# ------------------------------------

# Inlocuire/stergere remove(), replace(), pop(), clear() ------------------------------------------------

# var = 'mama tata fratele sora sotia sotul copilul mama'
# print(var.replace('sotia', 'nevasta')) # -------> mama tata fratele sora nevasta sotul copilul mama

# lista = ['mere', 'pere', 'banane', 'kiwi', 'struguri']
# lista.remove('kiwi')
# print(lista) # -------> ['mere', 'pere', 'banane', 'struguri']

# lista = ['mere', 'pere', 'banane', 'kiwi', 'struguri']
# lista.replace('kiwi')
# print(lista) # -------> ['mere', 'pere', 'banane', 'struguri']

# lista = ['mere', 'pere', 'banane', 'kiwi', 'struguri']
# lista.pop(2) # sterge elementul de la indexul 2
# element_sters = lista.pop(2) # sterge elementul de la indexul 2 si il salveaza in variabila element_sters
# print(lista) # -------> ['mere', 'pere', 'kiwi', 'struguri']
# print("Elementul sters este : " + element_sters) # -------> Elementul sters este : banane

# lista = ['mere', 'pere', 'banane', 'kiwi', 'struguri']
# lista.clear() # sterge toate elementele din lista
# print(lista) # -------> []

# ------------------------------------

# Liste, subliste, string ------------------------------------------------

# lista_cumparaturi = ["mere","oua","lapte"]

#       sau

# lista_cumparaturi = [
#     "mere",
#     "oua",
#     "lapte"]
# lista_preturi = [5,3,8]

# print(lista_cumparaturi[0])
# print(lista_preturi[0])
# print("Pretul pentru " + lista_cumparaturi[0] + " este " + str(lista_preturi[0]) + " RON ")
# print("Pretul pentru " + lista_cumparaturi[1] + " este " + str(lista_preturi[1]) + " RON ")
# print("Pretul pentru " + lista_cumparaturi[2] + " este " + str(lista_preturi[2]) + " RON ")

# sau 

# lista_cumparaturi = ["oua", "paine", "lapte", "kiwi"]
# for i in lista_cumparaturi :
#     print(i) # -------> oua paine lapte kiwi (fiecare pe linie noua)

# lista_liste = [ ["Mere", 5], ["Oua", 3], ["Lapte", 8]]
# print(lista_liste[0]) # -------> ["Mere", 5]

# lista_mere = lista_liste[0] # -------> ["Mere", 5]
# lista_oua = lista_liste[1]
# lista_lapte = lista_liste[2]

# print(lista_mere) # -------> ["Mere", 5]
# print(lista_mere[0]) # -------> Mere
# #       sau
# print(lista_liste[0][0]) # -------> Mere

# print("pretul pentru " + lista_liste[0][0] + " este " + str(lista_liste[0][1]) + " RON.")
# print("pretul pentru " + lista_liste[1][0] + " este " + str(lista_liste[1][1]) + " RON.")
# print("pretul pentru " + lista_liste[2][0] + " este " + str(lista_liste[2][1]) + " RON.")

# lista_cumparaturi = [ ["oua",1], ["paine",3], ["lapte",8], ["kiwi", 5] ]
# for i in lista_cumparaturi :
#     if i[0] == "paine":
#         print("am gasit")
#     else : 
#         print("produsul " + i[0] + " are pretul " + str(i[1]) + " RON.")

# ---------------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------- Verificari pe string/liste -----------------------------------------------------------------
# ------------- len(), index(), startswith(), endswith(), isalpha(), isdigit(), isalnum(), type(), any(), all(), count(), find(), sorted()  --------------

# nume = "abracadabra"
# print(len(nume)) # --------> 11 caractere

# nume = "abracadabra"
# print(nume.index('c')) # -------> 4 (indexul la care se gaseste litera c)

# text = "Abesei Paul"
# print(text.startswith('A')) # -------> True

# sau

# print('Abesei Paul'.startswith('A')) # -------> True
# print(text.endswith('l'))   # -------> True
# print(text.isalpha())      # -------> False (are spatiu intre cuvinte)
# print(text.isdigit())  # -------> False (nu toate caracterele sunt cifre)
# print(text.isalnum())  # -------> False (nu toate caracterele sunt alfanumerice, are spatiu)

# numar_intreg = 10
# numar_zecimal = 14.7
# print(type(text)) # -------> <class 'str'>
# print(type(numar_intreg)) # -------> <class 'int'>
# print(type(numar_zecimal)) # -------> <class 'float'>

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

# lista_pare = []
# for x in range(1,11) :
#     if x % 2 == 0 :
#         lista_pare.append(x)
# print(lista_pare) # ------> 2,4,6,8,10

# var = 'mama tata fratele sora sotia sotul copilul mama'
# print(var.count('mama')) # -------> 2 ori gasit
# print(var.find('fratele')) # -------> la indexul 10 din string

# lista = [5,3,8,1,2]
# print(sorted(lista)) # -------> [1, 2, 3, 5, 8] sorteaza si suprascrie lista

# ------------------------------------------------------ Caractere speciale ------------------------------------------------------------------
# Caractere speciale in string-uri : \n \t \\ \' \" ----------------------------------------------------

# print("Acesta este un text cu un caracter special: \n new line")
# print("Acesta este un text cu un caracter special: \t tab")
# print('Acesta este un text cu un caracter special: \\ backslash')
# print("Acesta este un text cu un caracter special: \' apostrof")
# print('Acesta este un text cu un caracter special: \" ghilimele')

# --------------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------ Metode string/liste ---------------------------------------------------------------
# ----------------- upper(), capitalize(), lower(), camel(), pascalcase(), append(), extend() ----------------

# nume = "paul"
# print(nume.upper()) # -----> PAUL

# nume = "abesei paul"
# print(nume.capitalize()) # -----> Abesei paul # prima litera mare

# nume = "abesei paul andrei"
# print(nume.title()) # -----> Abesei Paul Andrei # fiecare cuvant cu litera mare

# sau

# nume = "abesei paul"
# print(nume.pascalcase()) # -----> Abesei Paul # fiecare cuvant cu litera mare

# nume = "PAUL"
# print(nume.lower()) # -----> paul

# lista_fructe = ["banane", "capsuni"]
# print(lista_fructe)
# lista_fructe.append("kiwi")
# print(lista_fructe)
# print(lista_fructe[1])

# lista_vegetale = ["morcovi", "cartofi"]
# lista_fructe = ["banane", "capsuni"]
# lista_fructe.extend(lista_vegetale)
# print(lista_fructe) # -------> ['banane', 'capsuni', 'morcovi', 'cartofi']

# ------------------------------------------------

# --------------------------------------------------------------Modules : import------------------------------------------------------------------------------------------------
# import random ------------------------------------------------

# lista = [1,2,3,4,5,6,7]
# print(lista)
# random.shuffle(lista) # -------> 5627341
# print(lista)

# numar = random.randint(1, 100)
# print(numar) # -------> 57 (numar random intre 1 si 100)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------