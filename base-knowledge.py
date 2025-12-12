# nume = "Paul"
# nume = "Aura"
# print(nume)

# mai sus am printat Aura deoarece a suprascris peste Paul

# text = 'aici putem scrie un "text" simplu'
# text2 = "Paul's bike is blue."
# text3 = 
# """aici
# putem
# scrie
# pe'
# "mai"
# multe linii."""

# print(text3)

# titlu = '   Luceafarul'
# autor = '         de Mihai Eminescu'
# strofa1 = """A fost odată ca ’n poveşti,
# A fost ca niciodată,
# Din rude mari împărăteşti,
# O prea frumoasă fată."""

# print(titlu)
# print(autor)
# print(strofa1)

# numar_intreg = 5
# print(numar_intreg)
# numar_zecimal = 5.5
# print(numar_zecimal)

# print('Care este numele tau ?')
# nume = input("care este numele tau : ")
# print('Numele tau este :')
# print(nume)

# text1 = 'Paul merge'
# text2= 'la piata'
# # print(text1 + ' ' + text2)
# text3 = text1 + ' ' + text2
# print(text3)

# Printare de 100 ori sau oricat
# text = 'IT School'
# print(text * 100)

#Operatii
# ----------------------------------------
# #Adunarea
# print(5 + 2)

# #Scadere
# print(7 - 4)

# #Inmultire
# print(5 * 2)

# #Impartire
# print(5 /2 )

# #Impartire prin lipsa, nu exista prin adaos
# print(5 / 2)
# ----------------------------------------

#Afisare tip de date
# ----------------------------------------
# text = 'Python'
# numar_intreg = 10
# numar_zecimal = 14.7

# #type afiseaza tipul de clasa al variabilei introduse
# print(type(text))
# print(type(numar_intreg))
# print(type(numar_zecimal))
# ----------------------------------------

#Conversii
# ----------------------------------------
#conversie int la str si concatenare
# print(text + ' vechime : ' + str(numar_intreg) + ' ani')

#conversie de la str la int si adunare
# text = "30"
# print(int(text) + 10)
# ----------------------------------------

#Quiz1 
# ---------------------------------------
#cerem utiliz numele si varsta
#calculam si anuntam utilz cati ani mai are de trait pana la 100 de ani
# nume = input("Numele tau este : ")
# varsta = input("Varsta ta este  : ")
# print(nume + " ,pana la 100 de ani mai ai : " + str(100 - int(varsta)) + " ani.")
# ---------------------------------

# string[] si len()
# ------------------------------------------------
# nume = "Paul"
#         01234
# print(nume[2]) # ------> litera u
# nume = "abracadabra"
# print(len(nume)) # --------> 11 caractere
# ------------------------------------------------

# liste
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
# ------------------------------------------------

# operatorul de comparatie ==
# ------------------------------------------------
# adevarat = True
# fals = False

# print(adevarat)
# print(type(adevarat)) # -------> <class 'bool'>
# print(fals)
# print(type(fals))

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

# Loops
# ------------------------------------------------
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

# Methods : upper, lower, append
# ------------------------------------------------
# nume = "paul"
# print(nume.upper())

# nume = "PAUL"
# print(nume.lower())

# lista_fructe = ["banane", "capsuni"]
# print(lista_fructe)
# lista_fructe.append("kiwi")
# print(lista_fructe)
# print(lista_fructe[2])
# ------------------------------------------------

# Modules : import
# ------------------------------------------------
# import random
# lista = [1,2,3,4,5,6,7]
# print(lista)
# random.shuffle(lista) -------> 5627341
# print(lista)
# ------------------------------------------------

#Quiz2 : len - lungime
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
# lista = [] # ------> aici este initializata o lista goala la care se adauga cu .append elemente in aceasta
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