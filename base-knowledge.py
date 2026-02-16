'''# ------------------------------------------------------ Afisare date ----------------------------------------------------------------------'''

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

'''# ------------------------------------------------------------ Operatii ---------------------------------------------------------------------'''
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

'''# ----------------------------- Operatori Logici (True si False), Apartenta in / not in, Identitate is & is not --------------------------'''

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

'''# ------------------------------------------------------------------------ Control flux ------------------------------------------------------------'''
'''# Structura if ... elif ... else ------------------------------------------------'''

# a = 10
# b = 12
# if a<b :
#     print("a este mai mic decat b")
# elif a==b :
#     print("a este egal cu b")
# else :        # ------- > daca a nu este mai mic si nici egal cu b
#     print("a este mai mare decat b")

# sau

# numar_1 = 5
# numar_2 = 5

# if numar_1 == numar_2 :
#     print("numarul 1 este egal cu numarul 2")
# if int(input("ce varsta ai ? ")) >= 20 :
#      print("ai voie in parc")
# else :
#      print("nu ai voie in parc")

# -----------------------------------------------

'''# Structura for ... in ... ------------------------------------------------'''

# my_str = "python"
# for char in my_str : 
#     print(char) # --------> afiseaza fiecare caracter pe linie noua : p
#                                                                       y
#                                                                       t
#                                                                       h
#                                                                       o
#                                                                       n

# -----------------------------------------------

'''# Structura while ... -----------------------------------------------'''

# numar = 1
# limita = 5
# while numar <= limita :
#     print("Numarul curent este: " + str(numar))
#     numar = numar + 1

# -------------------------------------------------------------------------------------------------------------------------------------------

'''# -----------------------------------------------------------Conversii ---------------------------------------------------------------------'''
'''# Conversie int(), str(), bool(), float(), list(), rotunjire  ----------------------------------------'''

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

'''# ------------------------------------------------- Modificari pe string/liste/tuple -----------------------------------------------------------------''' 
'''# Slicesing, split(), join(), zip(), sort() ------------------------------------------------'''

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

'''# Stergerea spatiilor strip(), lstrip(), rstrip() ------------------------------------------------'''

# nume = '      Abesei Paul      '
# print(nume.strip()) # -------> Abesei Paul (elimina spatiile de la inceput si sfarsit)
# print(nume.lstrip()) # -------> Abesei Paul      (elimina spatiile de la inceput)
# print(nume.rstrip()) # ------->      Abesei Paul (elimina spatiile de la sfarsit)

# ------------------------------------

'''# Inlocuire/stergere remove(), replace(), pop(), clear() ------------------------------------------------'''

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

'''# Liste, subliste, string ------------------------------------------------'''

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

# ------------------------------------

'''# Tuple-uri (value, value, value) - modificari si operatii ------------------------------------------------'''

# tuple_exemplu = (1, 2, 3, "patru", "cinci")
# print("Tuple exemplu:", tuple_exemplu)
# Unpacking - cate variabile definesti, atatea elemente in tuplu le ia
# a, b, c, d, e = tuple_exemplu
# print("Unpacked values:", a, b, c, d, e) # -------> 1 2 3 patru cinci

# Accesare element din tuplu
# tuple_exemplu = (1, 2, 3, "patru", "cinci")
# print(tuple_exemplu[3]) # -------> patru

# Lungimea tuplului 
# tuple_exemplu = (1, 2, 3, "patru", "cinci")
# print(len(tuple_exemplu)) # -------> 5

# Numarul de aparitii ale unui element in tuplu
# tuple_exemplu = (1, 2, 3, "patru", "cinci")
# print(tuple_exemplu.count(2))   # -----> 1

# Slicing
# sub_tuple = tuple_exemplu[1:4] # Elemente de la index 1 la 3
# print("Sub-tuple:", sub_tuple) # -----> (2, 3, 'patru')

# Generare tuplu folosind comprehension
# tuple_exemplu = ('a', 'b', 'c', 'd', 'e', 'i', 'f', 'g', 'h', 'i')
# tuple1 = tuple(zi for zi in tuple_exemplu if zi == 'i')  
# print(tuple1) # -----> ('i', 'i')

# Modificarea unui tuple prin conversie la lista si inapoi la tuplu, deoarece tuplele sunt imutabile(nu pot fi modificate direct)
# tuple_numere = (1,2,3,4)
# tuple_numere = list(tuple_numere)
# tuple_numere.append(5)
# tuple_numere = tuple(tuple_numere)
# print(tuple_numere)

# -----------------------------------------------

'''# Set-uri {value, value, value} - modificari si operatii ----------------------------------------------- '''

# set_exemplu = {1, 2, 3, "patru", "cinci"}
# print("Set exemplu:", set_exemplu)

# Accesare elemente din set (nu se poate accesa un element specific)
#print(set_exemplu[0]) # eroare

# Creare set folosind comprehansion
# set_nou = {x**2 for x in range(5)}
# print("Set creat prin comprehensiune:", set_nou) # -----> {0, 1, 4, 9, 16}

# Afisarea unui element din set
# for element in set_exemplu:
#     print("Element din set:", element)

# Adaugare element in set
# set_exemplu = {1, 2, 3, "patru", "cinci"}
# set_exemplu.add("sase")
# print("Set dupa adaugare:", set_exemplu)

# Stergere element din set
# set_exemplu = {1, 2, 3, "patru", "cinci"}
# set_exemplu.remove("patru")
# print("Set dupa stergere:", set_exemplu)

# Verificare existenta element in set
# set_exemplu = {1, 2, 3, "patru", "cinci"}
# print("Exista 'cinci' in set?", "cinci" in set_exemplu)

# Operatii cu seturi
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print("Intersectie:", set1 & set2) # sau set1.intersection(set2)
# print("Reuniune:", set1 | set2) # sau set1.union(set2)
# print("Diferenta:", set1 - set2) # sau set1.difference(set2)

# Unire seturi
# set_unire = set1.union(set2)
# print("Set unire:", set_unire)

# Intersection - returneaza intersectia dintre doua seturi
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# print("Intersectie set1 si set2:", set1.intersection(set2)) # -----> {3, 4}

# Difference - diferenta intre doua seturi
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# print("Diferenta set1 si set2:", set1.difference(set2)) # -----> {1, 2}

# Issubset - verificare submultime intre doua seturi si returneaza True/False
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = {1, 2, 3, 4, 7, 8}
# print("set1 este submultime a set2:", set1.issubset(set2)) # -----> False
# print("set1 este submultime a set3:", set1.issubset(set3)) # -----> True

# Conversie lista in set
# lista = [1, 2, 2, 3, 4]
# lista_modificata = set(lista)

# Conversie set in lista
# lista_noua = {1, 2, 3, 4}
# lista_noua = list(set_exemplu)

# Update set cu elemente din alta colectie fara a lua duplicatele
# set_1 = {1, 2, 3, 4}
# set_2 = {4, 5, 6}
# set_1.update(set_2)
# print("Set 1 dupa update:", set_1) # -----> {1, 2, 3, 4, 5, 6}

# Functia pop() pentru seturi
# my_set = {10, 20, 30, 40}
# print("Element scos din set:", my_set.pop())  # Scoate si returneaza un element arbitrar din set

# Frozen set - set imuabil, nu poate fi modificat dupa creare, nu se pot adauga sau sterge elemente, dar se pot face operatii de intersectie, reuniune, diferenta

# frozen_set_exemplu = frozenset([1, 2, 3, 4])
# print("Frozen set exemplu:", frozen_set_exemplu)
# frozen_set_exemplu.add(5) # eroare deoarece frozen set este imuabil

'''# Dictionar {key:value} - modificari si operatii ------------------------------- '''

# dictionarul = {'Ana':19, 'Maria':20, 'Marian':45}

# persoane = {} # dicționar gol
# n = int(input("Câte persoane vrei să adaugi? ")) # citim câte persoane vrem să adăugăm
# for i in range(n):
#     nume = input("Introdu numele persoanei: ")
#     varsta = int(input("Introdu vârsta: "))
#     persoane[nume] = varsta  # adăugăm în dicționar
# print("Dictionar : ", persoane)

# Afisare valori folosind : Ana, Maria, Marian - keys si 19, 29, 45 - values

# print(dictionarul['Maria']) # -----> 20

# print(dictionarul.get('masina', 'Cheia nu exista in dictionar')) # -----> Cheia nu exista in dictionar
# print(dictionarul.get('Ana', 'Cheia nu exista in dictionar')) # -----> 19

# Modificare valoare folosind cheia:
# dictionarul['Marian'] = 40
# print(dictionarul['Marian']) # -----> 40

# Afisare keys si values -------------------------------

# for key in dictionarul.keys():
#    print(key)  # ------> Ana
                #        Maria
                #        Marian 

# for value in dictionarul.values():
#    print(value) # ------> 19
                 #         20
                 #         40

# for key, value in dictionarul.items():
#     print(f'Key: {key}  Value: {value}') 
    # ------> Key: Ana  Value: 19
    #         Key: Maria  Value: 20
    #         Key: Marian  Value: 40

# -------------------------------

# Adaugare pereche noua in dictionar -------------------------------
# dictionarul = {'Ana':19, 'Maria':20, 'Marian':45}
# dictionarul['Ion'] = 25
# print(dictionarul) # -----> {'Ana': 19, 'Maria': 20, 'Marian': 40, 'Ion': 25}

#-------------------------------
# Metodele pop(), popitem(), clear() si update() -------------------------------

# dictionarul = {'Ana':19, 'Maria':20, 'Marian':45}
# print(dictionarul)
# dictionarul.pop('Ana') # Sterge perechea cu cheia 'Ana'
# print(dictionarul) # -----> {'Maria': 20, 'Marian': 40, 'Ion': 25}

# dictionarul.popitem() # Sterge ultima pereche adaugata
# print(dictionarul) # -----> {'Maria': 20, 'Marian': 40}

# dictionarul.clear() # Sterge toate perechile din dictionar
# print(dictionarul) # -----> {}

# dictionarul = {'Ana':19, 'Maria':20, 'Marian':45}
# dictionarul.update({'Elena':30, 'George':50}) # Adauga perechi noi in dictionar la final
# dictionarul.update({'Maria':22}) # Modifica valoarea cheii 'Maria' din 20 in 22
# print(dictionarul) # -----> {'Ana': 19, 'Maria': 22, 'Marian': 45, 'Elena': 30, 'George': 50}

# -------------------------------

# Setdefault() - adauga o pereche noua doar daca cheia nu exista deja in dictionar -------------------------------

# dictionarul = {'Ana':19, 'Maria':20, 'Marian':45}
# dictionarul.setdefault('Ion', 25) # Adauga perechea 'Ion':25
# dictionarul.setdefault('Maria', 22) # Nu modifica perechea 'Maria':20 deoarece cheia 'Maria' exista deja
# print(dictionarul) # -----> {'Ana': 19, 'Maria': 20, 'Marian': 45, 'Ion': 25}

# -------------------------------

# Dictionar cu valori complexe (dictionare in interiorul dictionarului) -------------------------------
# persoane = {
#     1234 : {
#             'nume':'Popescu',
#             'prenume':'Ion',
#             'varsta':30,
#             'masina':{
#                 'marca':'Dacia',
#                 'model':'Logan',
#                 'tip_combustibil':'benzina'
#                     }
#             },
#     5678 : {
#             'nume':'Ionescu',
#             'prenume':'Maria',
#             'varsta':25,
#             'masina':{
#                 'marca':'Ford',
#                 'model':'Focus',
#                 'tip_combustibil':'motorina'
#                     }
#             }
#             }
# Accesare model masina persoanei cu CNP 1234
# print(persoane['1234']['masina']['model']) # -----> Logan

# Modificare tip_combustibil masina persoanei cu CNP 5678
# persoane['5678']['masina']['tip_combustibil'] = 'electric'
# sau cu update():
# persoane['5678']['masina'].update({'tip_combustibil':'electric'})

# Afisare folosind get() la tip_combustibil masina persoanei cu CNP 5678
# print(persoane.get('5678').get('masina').get('tip_combustibil')) # -----> electric
# print(persoane.get('1234').get('nume')) # -----> Popescu

# --------------------------------------------

"""# Functii : def si return ------------------------------- """
''' Se foloseste return cand vrei sa stochezi ceea ce transmite functia'''

# def func_basic() :
#     print("Hello from func_basic")
#     return "Orice tip de data sau nimic"

# func_basic() # apelarea functiei si executarea codului din interiorul ei : Hello from func_basic
# var = func_basic()
# print(var) # None : deoarece functia nu are return

# def persoana (nume="Popescu", varsta=30) : # functia are doi parametrii cu valori implicite
#     print("Numele persoanei este:", nume)
#     print("Varsta persoanei este:", varsta)

# persoana() # apelarea functiei fara parametrii : se folosesc valorile implicite
# persoana("Ionescu") # apelarea functiei cu un singur parametru : varsta va avea valoarea implicita 
# persoana(25) # apelarea functiei cu un singur parametru : numele va avea valoarea implicita

# def persona (nume, prenume = "Anonim") : # functia are un parametru obligatoriu si unul cu valoare implicita
#     print("Numele complet al persoanei este:", nume, prenume)

# persona("Vasilescu", "Andrei") # apelarea functiei cu ambii parametrii
# persona("Marinescu") # apelarea functiei cu un singur parametru : prenumele va avea valoarea implicita
# persona(nume="Georgescu", prenume="Mihai") # apelarea functiei cu ambii parametrii folosind nume

# def func_with_params(param1, param2) :
#     print("Hello from func_with_params")
#     print(f"Parametrul 1 este {param1}")
#     print(f"Parametrul 2 este {param2}")
#     return param1 + param2, param1 * param2, param1 - param2

# x, y, z = func_with_params(10,7)
# print(x,y,z) # (17, 70, 3)

# Variabile locale si globale

# def functie_extra (param1, param2) :
#     rezultat = param1 + param2 
#     return rezultat

# print(functie_extra(10, 20)) 

# def functie_nou (param1, param2) :
#     global var # fiind definita ca si global, variabila poate sa sufere modificari atat in functie cat si inafara ei
#     var = param1 + param2
#     print(var)

# print(var)
# functie_nou (100,200)
# var = var + 10
# print(var)

# Functie recursiva atentie la oprire pentru a evita : # eroare de stack overflow

# lista = [1,2,3, [1,3,5], 6, [1, [1,2,3,1], 6,7],8]
# def frecv_nr (lista_in_care_caut, nr_cautat) :
#     counter = 0
#     for nr in lista_in_care_caut :
#         if type(nr) == list : 
#             counter += frecv_nr(nr , nr_cautat)
#         elif nr == nr_cautat :
#             counter += 1
#     return counter
# print(frecv_nr(lista,1))

# Functie care are ca parametru alta functie

# def aduna (lista_elemente):
#     suma = 0
#     for elem in lista_elemente :
#         suma += elem
#     return suma

# def produs (lista_elemente):
#     produsul = 1
#     for elem in lista_elemente:
#         produsul *=elem
#     return produsul

# def suma_liste (func, lista_cu_liste):
#     suma_totala = 0
#     for lista in lista_cu_liste :
#         suma_totala += func(lista)
#     return suma_totala

# lista = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] # variabila globala
# print ("suma sumelor elementelor din liste este :", suma_liste(aduna, lista))
# print ("suma produselor elementelor din liste este :", suma_liste(produs, lista))


# Functie care are ca parametru *args pentru a transmite nr variabil de argumente pozitionale - tuples

# def suma(*args):
#     return sum(args)
# print (suma(10,11,12,13))

# Functie care are ca parametru **kwargs pentru a transmite nr variabil de argumente numite - dictionare

# def suma(**kwargs):
#     total = 0
#     for valoare in kwargs.values():
#         total += valoare
#     return total

# rezultat = suma(a=10, b=5, c=3, d=2) # primeste a,b,c,d - key si 10,5,3,2 - values
# print(rezultat)  # 20

# Functie care are ca paramatrii *args si **kwargs

#[DEBUG] - mesajul pe care vreau sa il afisez
#[INFO]
# def logare(*mesaje, **optiuni):
#     nivel = optiuni.get('nivel', 'INFO')
#     separator = optiuni.get('separator', ' ')
#     log_final = separator.join(str(mesaj) for mesaj in mesaje)
#     print(f'[{nivel}] {log_final}')

# action = "Start Program"
# user = "Ana"

# logare(action, user)
# logare(f'Action: {action}', f'User : {user}', nivel="Debug", separator= ' \ ')

# Functie speciala pentru interpretare string din python

# x = "2 + 3 * 4"
# rezultat = eval(x)
# print(rezultat) # 14
# # Atenție: eval() este periculos dacă stringul vine de la utilizator (poate executa cod malițios).

# import ast
# x = "[1, 2, 3]"
# rezultat = ast.literal_eval(x)
# print(rezultat)  # [1, 2, 3]
# # Interpretează doar literali Python (numere, liste, dicționare etc.)

# import operator
# ops = {
#     '+' : operator.add,
#     '-' : operator.sub,
#     '*' : operator.mul,
#     '/' : operator.truediv,  # use operator.div for Python 2
#     '%' : operator.mod,
#     '^' : operator.xor,
# }

# def eval_binary_expr(op1, oper, op2):
#     op1, op2 = int(op1), int(op2)
#     return ops[oper](op1, op2)

# print(eval_binary_expr(("1 + 3".split())))
# print(eval_binary_expr(("1 * 3".split())))
# print(eval_binary_expr(("1 % 3".split())))
# print(eval_binary_expr(("1 ^ 3".split())))

# ----------------------------------------------------------------------------------------

'''# ------------------------------------------------- Verificari pe string/liste -----------------------------------------------------------------'''
'''# ------------- len(), index(), startswith(), endswith(), isalpha(), isdigit(), isalnum(), type(), any(), all(), count(), find(), sorted()  --------------'''

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

# --------------------------------------------------------------------------------------------------------------------------------------------

'''# ------------------------------------------------------ Caractere si metode speciale ------------------------------------------------------------------'''
'''# Caractere speciale in string-uri : \n \t \\ \' \" ----------------------------------------------------'''

# print("Acesta este un text cu un caracter special: \n new line")
# print("Acesta este un text cu un caracter special: \t tab")
# print('Acesta este un text cu un caracter special: \\ backslash')
# print("Acesta este un text cu un caracter special: \' apostrof")
# print('Acesta este un text cu un caracter special: \" ghilimele')

'''# Docstrings ----------------------------------------------------'''

# def suma(nuamr1 , numar2):
#     '''
#     Calculeaza suma a doua numere prmite ca parametru
    
#     :param nuamr1 tip int : primul numar de adunat
#     :param numar2 tip int : al doilea numar de adunat
#     return tip int : suma celor 2 numere
#     '''
#     total = nuamr1 + numar2
#     return total

# print(suma(10,20))
# help(suma) # afiseaza ce este pus intre ''' ''' din functia apelata si printeaza functia cu multe detalii
# print(suma.__doc__) # afiseaza ce este pus intre ''' ''' din functia apelata fara a o apela

'''# Type hinting ----------------------------------------------------'''

# def suma(nuamr1: int , numar2 : int)  -> int :
#     '''
#     Calculeaza suma a doua numere prmite ca parametru.

#     Args:
#         nuamr1 (int) : primul numar de adunat
#         numar2 (int) : al doilea numar de adunat

#     Returns:
#         int : suma celor 2 numere
#     '''
#     return nuamr1 + numar2

# from typing import List
# def suma_lista(lista : list[int]) -> int :
#     '''
#     Calculeaza suma tuturor elem dintr-o lista primita ca parametru

#     Args :
#         lista (list[int]) : lista de numere intregi
    
#     Returns :
#         int : suma nr din lista
#     '''
#     return sum(lista)

# --------------------------------------------------------------------------------------------------------------------------------------------

'''# ------------------------------------------------------ Metode string/liste ---------------------------------------------------------------'''
'''# ----------------- id(), copy(), copy.deepcopy(), upper(), capitalize(), lower(), camel(), pascalcase(), append(), extend() ----------------'''

# Locatie in memorie id()

# str1 = "ceva"
# str2 = str1

# print(id(str1)) # returneaza adresa de memorie a obiectului str1
# print(id(str2))

# list1 = [1, 2, 3, 4]
# list2 = list1

# print(id(list1)) # returneaza adresa de memorie a obiectului list1
# print(id(list2))

# Copierea obiectelor copy() pentru a crea o copie separata cu adresa de memorie diferita

# list1 = [1, 2, 3, 4]
# list2 = list1.copy()

# print(id(list1)) # returneaza adresa de memorie a obiectului list1
# print(id(list2))

# Copierea obiectelor in adancime deepcopy() pentru a crea o copie separata cu adresa de memorie diferita
# import copy
# list1 = [[1, 2], [3, 4]]
# list2 = copy.deepcopy(list1)
# print(id(list1)) # returneaza adresa de memorie a obiectului list1
# print(id(list2)) # returneaza adresa de memorie a obiectului list2

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
# print("noul nume este :",nume.lower()) # -----> paul

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

'''# --------------------------------------------------------------Modules : import------------------------------------------------------------------------'''
''' Module si pachete ------------------------------------------------'''
# Import de module ----------------

# import random
# sau 
# from random import randint
# from random import random, randrange <-------- se pot importa mai multe module despartite de virgule
# sau
# from random import randint as alalalala <------- alias, se poate punte orice nume dorit
# sau
# from random import * <------ importa tot din modulul import
# sau
# import random as rand <------ alias

# def calcul():
#     a = random.randint(1,5) # aloca un numar intreg aleator de la 1 la 5
#     b = random.randint(1,5)
    # sau
    # a = rand.randint(1,5)
    # b = rand.randint(1,5)
    # sau
    # a = alalalala(1,5)
    # b = alalalala(1,5)
#     return a+b
# print(calcul())

# Creare modul personal intr-un alt fisier ----------------
# def my_function () :
#     print("Hello from my_function")
# my_var = 30
# my_name = __name__
# ---------------------------------

# Apelare din modul personal -----------------------
# import fisier
# fisier.my_function() # apelare modul
# print(fisier.my_function) # ------> Hello from my_function
# print(fisier.my_name) # -------> aifseaza numele fisierului de unde importam
# ---------------------------------

# Import packete ------------------
# import fisier_package.fisier_modul # importa modulul : fisier_modul din package-ul : fisier_package
# print (fisier_package.fisier_modul.functie) # printeaza functia din modulul : fisier_modul din package-ul : fisier_package

# Argumente vector - scriere in terminal

# import argparse
# def parse_args():
#     my_parser = argparse.ArgumentParser(description='Afisza nume frumos')
#     my_parser.add_argument('--nume', type=str, required=True,help='Nume de familie')
#     my_parser.add_argument('--prenume', type=str, help='Prenumele omului')
#     args = my_parser.parse_args()
#     return args.nume, args.prenume
# def main():
#     nume, prenume = parse_args()
#     print(f'Nume: {nume}, Prenume: {prenume}')
#     if __name__ == 'main':
#         main()

# import sys
# def afisaza_nume(nume, prenume):
#     print(f'Nume: {nume}, Prenume: {prenume}')
# def main():
#     print(sys.argv)
# afisaza_nume(sys.argv[1], sys.argv[2])
# if __name__ == 'main':
#     main()

'''# import random ------------------------------------------------'''

# lista = [1,2,3,4,5,6,7]
# print(lista)
# random.shuffle(lista) # -------> 5627341
# print(lista)

# numar = random.randint(1, 100)
# print(numar) # -------> 57 (numar random intre 1 si 100)

'''# import json ------------------------------------------------'''

# persoane = {
#     1234 : {
#             'nume':'Popescu',
#             'prenume':'Ion',
#             'varsta':30,
#             'masina':{
#                 'marca':'Dacia',
#                 'model':'Logan',
#                 'tip_combustibil':'benzina'
#                     } 
#             },
#     5678 : {
#             'nume':'Ionescu',
#             'prenume':'Maria',
#             'varsta':25,
#             'masina':{
#                 'marca':'Ford',
#                 'model':'Focus',
#                 'tip_combustibil':'motorina'
#                     }
#             }
#             }
# print(json.dumps(persoane, indent=4)) # -----> afiseaza dictionarul persoane frumos formatat

# -----------------------------------------------------------------------------------------------------------------------------------

'''# -------------------------------------------------------- Fisiere ----------------------------------------------------------'''

# mesaj = "Avada cadavra\n"
# nume_fisier = "fisier-testing.txt"

# my_file = open("fisier-testing.txt", 'w')
# # print(type(my_file)) # ------> <class '_io.TextIOWrapper'>
# my_file.write(mesaj)
# # sau 
# # my_file.write("Merge si asa")
# my_file.close()

# my_file = open(nume_fisier, 'r')
# data = my_file.readlines()
# print(data)
# my_file.close()

# mesaj1 = "Ana are mere\n"
# mesaj2 = "Macbook Air M1\n"
# mesaj3 = "Vine politia\n"
# my_file = open(nume_fisier, 'a')
# # my_file.writelines(mesaj1, mesaj2, mesaj3) # nu o sa mearga, primeste doar un singur parametru
# my_file.writelines([mesaj1, mesaj2, mesaj3])
# my_file.close()

# my_file = open(nume_fisier, 'r')
# linii_fisier = my_file.readlines()
# my_file.close()
# for i in range(len(linii_fisier)):
#     if 'Ana' in linii_fisier[i] :
#         linii_fisier[i] = linii_fisier[i].replace('Ana', 'Ionela')
#         break
# my_file = open(nume_fisier, 'w')
# print(linii_fisier)
# my_file.writelines(linii_fisier)
# my_file.close()

# Context manager - folosind : with - ca sa nu mai folosim open() si close() de fiecare data

# with open(nume_fisier, 'r') as my_file:
#     linii_fisier = my_file.readlines()
# for i in range(len(linii_fisier)):
#     if 'Ana' in linii_fisier[i] :
#         linii_fisier[i] = linii_fisier[i].replace('Ana', 'Ionela')
#         break
# with open(nume_fisier, 'w') as my_file:
#     my_file.writelines(linii_fisier)

with open("fisier-testing.txt", 'r') as my_file:
    text = my_file.read()

text = text.replace("ana", "ionela")

with open("fisier-testing.txt", 'w') as my_file:
    my_file.write(text)
    print("a mers")
