'''# 1. Creează două variabile cu valori numerice și afișează suma lor.'''

# a = 5
# b = 10
# print("Suma celor doua numere este:", a+b)

'''# 2. Afișează produsul a două numere introduse de la tastatură. '''

# a = 5
# b = 10
# print("Suma celor doua numere este:", a*b)

'''# 3. Primește un nume de la tastatură și afișează-l cu litere mari. '''

# nume = input("Introdu numele:")
# print ("Numele tau este : ", nume.upper())

'''# 4. Afișează lungimea unui string introdus de la tastatură. '''

# sir = input("Introdu un sir de caractere : ")
# print("Lungimea sirului : ", len(sir))

'''# 5. Verifică dacă un număr este par sau impar. '''

# numar = int(input("Introdu un numar:"))
# if numar % 2 == 0 :
#     print("Numar par")
# else : 
#     print("Numar impar")

'''# 6. Primește un text și un caracter, afișează de câte ori apare caracterul în text. '''

# text = input ("Introdu un text: ")
# caracter = input("Introdu un caracter: ")
# print ("caracterul '", caracter , "' apare de ", text.count(caracter), " ori in textul introdus.")

'''# 7. Afișează ultimul caracter dintr-un string introdus de la tastatură. '''

# text = input ("Introdu un text: ")
# print("Ultimul caracter din text este: ", text[-1])

'''# 8. Primește un număr și afișează dacă este pozitiv, negativ sau zero. '''

# numar = input ("Introdu un numar: ")
# if float(numar) > 0 :
#     print("Numarul este pozitiv")
# elif float(numar) < 0 :
#     print("Numarul este negativ")
# else :
#     print("Numarul este zero")

'''# 9. Afișează toate caracterele unui string, câte unul pe linie. '''

# text = input ("Introdu un text: ")
# for i in text :
#     print(i)

'''# 10. Primește două numere și afișează cel mai mare dintre ele. '''

# numar1 = float(input("Introdu primul numar: "))
# numar2 = float(input("Introdu al doilea numar: "))
# if numar1 > numar2:
#     print("Primul numar este mai mare.")
# elif numar2 > numar1:
#     print("Al doilea numar este mai mare.")
# else:
#     print("Numerele sunt egale."

'''# 11. Primește trei numere și afișează cel mai mic si cel mai mare dintre ele. '''

# numar1 = float(input("Introdu primul numar: "))
# numar2 = float(input("Introdu al doilea numar: "))
# numar3 = float(input("Introdu al treilea numar: "))
# if numar1 <= numar2 and numar1 <= numar3:
#     print("Primul numar este cel mai mic.")
# elif numar2 <= numar1 and numar2 <= numar3:
#     print("Al doilea numar este cel mai mic.")
# else:
#     print("Al treilea numar este cel mai mic.")

#  sau

# print("Cel mai mic numar este: ", min(numar1, numar2, numar3))
# print("Cel mai mare numar este: ", max(numar1, numar2, numar3))

'''# 12. Primește un text și verifică dacă este palindrom. '''

'''# 13. Primește o parolă și verifică dacă are cel puțin 8 caractere și conține o cifră. '''

'''# 14. Primește un text și construiește un nou string numai cu vocalele din el. '''

# text = input("Introdu un text: ")
# text_vocale = ""
# vocale = "aeiouAEIOU"
# for char in text:
#     if char in vocale:
#         text_vocale += char
# print("Textul format doar din vocale este:", text_vocale)

'''# 15. Primește un număr n și afișează toate numerele pare de la 0 la n (inclusiv). '''

'''# 16. Primește un text și afișează doar literele mici din el. '''

'''# 17. Primește două numere și afișează toate numerele între ele (inclusiv), în ordine crescătoare. '''

'''# 18. Primește un text și afișează fiecare cuvânt pe o linie nouă. '''

'''# 19. Primește un număr și afișează tabla înmulțirii pentru acel număr (de la 1 la 10). '''

'''# 20. Primește un text și verifică dacă toate caracterele sunt litere mici. '''

'''# 21. Primește un text și afișează-l inversat. '''

'''# 22. Primește o propoziție și numără câte cuvinte conține. '''

'''# 23. Primește un text și înlocuiește toate spațiile cu caracterul "_". '''

'''# 24. Primește un număr și afișează suma cifrelor sale. '''

# numar = input("Introdu un numar: ")
# suma_cifre = 0
# for cifra in numar:
#     suma_cifre += int(cifra)    
# print("Suma cifrelor numarului este:", suma_cifre)

'''# 25. Primește un text și afișează doar caracterele care sunt cifre. '''

'''# 26. Primește un text și verifică dacă începe și se termină cu aceeași literă. '''

# text = input("Introdu un text: ")
# if text[0].lower() == text[-1].lower():
#     print("Textul începe și se termină cu aceeași literă.")
# else:
#     print("Textul nu începe și nu se termină cu aceeași literă.")       

'''# 27. Primește un text și afișează toate caracterele distincte din el. '''

# text = input("Introdu un text: ")
# caractere_distincte = set()
# for char in text:
#     caractere_distincte.add(char)
# print("Caracterele distincte din text sunt:", caractere_distincte)

# sau

# text = input("Introdu un text: ")
# caractere_distincte = ""
# for char in text:
#     if char not in caractere_distincte:
#         caractere_distincte += char
# print("Caracterele distincte din text sunt:", caractere_distincte)

'''# 28. Primește un text și afișează literele care apar de exact două ori. '''

# text = input("Introdu un text: ")
# litere_doua_ori = ""
# for char in text:
#     if text.count(char) == 2 and char not in litere_doua_ori:
#         litere_doua_ori += char
# print("Literele care apar de exact doua ori sunt:", litere_doua_ori)

'''# 29. Primește un număr n și afișează toți divizorii săi. '''

# numar = int(input("Introdu un numar: "))
# divizori = []
# for i in range(1, numar + 1):
#     if numar % i == 0:
#         divizori.append(i)
# print("Divizorii numarului sunt:", divizori)

'''# 30. Primește un text și verifică dacă are cel puțin o literă mare, una mică și o cifră. '''

'''# 31. Fizz Buzz: Primește un număr n și afișează numerele de la 1 la n. 
# Pentru multiplii de 3, afișează "Fizz", pentru multiplii de 5, afișează "Buzz", iar pentru multiplii de ambele, afișează "FizzBuzz". '''

'''# 32. Primește un text și afișează-l cu fiecare cuvânt inversat, dar în aceeași ordine. (Exemplu: "Ana are mere" -> "anA era erem") '''

# text = input("Introdu un text: ")
# cuvinte = text.split()          
# cuvinte_inversate = []
# for cuvant in cuvinte:
#     cuvinte_inversate.append(cuvant[::-1])
#     text_inversat = ' '.join(cuvinte_inversate)
# print("Textul cu cuvintele inversate este:", text_inversat)

'''# 33. Primește un text care contine o insiruire de numere și afișează media lor. (Exemplu: "1,2,3,4,5,10" -> 25/6 = 4.1666) '''

# text_numere = input("Introdu o insiruire de numere separate prin virgula: ")
# numere_str = text_numere.split(",")             
# numere = []
# for numar in numere_str:
#     numere.append(float(numar))
# media = sum(numere) / len(numere)
# print("Media numerelor este:", media)

'''# 34. Trebuie implementat un meniu interactiv in consola care pune la dispozitie utilizatorului urmatoarele optiuni:
# Adunare / # Scadere / # Inmultire / # Impartire / # Iesire din program
# Utilizatorul trebuie sa introduca optiunea, iar apoi:
# Pentru optiunile 1->4, utilizatorul trebuie sa introduca doua numere, iar programul va afisa rezultatul operatiei.
# In cazul in care introduce 5, atunci iesim din program.  '''

# print("Meniu:")
# print("1. Adunarea a doua numere.")
# print("2. Scaderea a doua numere.")
# print("3. Inmultirea a doua numere.")
# print("4. Impartirea a doua numere.") # verificare impartire la zero
# print("5. Iesire program.")
# numar = int(input("Optiunea ta este: "))
# flag = True
# while flag :
#     if numar == 1 :
#         nr1 = float(input("Introdu primul numar: "))
#         nr2 = float(input("Introdu al doilea numar: "))
#         print("Suma celor doua numere este: ", nr1+nr2)
#         flag = False
#     elif numar == 2 :
#         nr1 = float(input("Introdu primul numar: "))
#         nr2 = float(input("Introdu al doilea numar: "))
#         print("Diferenta celor doua numere este: ", nr1-nr2)
#         flag = False
#     elif numar == 3 :
#         nr1 = float(input("Introdu primul numar: "))
#         nr2 = float(input("Introdu al doilea numar: "))
#         print("Produsul celor doua numere este: ", nr1*nr2)
#         flag = False
#     elif numar == 4 :
#         nr1 = float(input("Introdu primul numar: "))
#         nr2 = float(input("Introdu al doilea numar: "))
#         if nr2 != 0 :
#             print("Impartirea celor doua numere este: ", nr1/nr2)
#         else :
#             print("Nu se poate impartii la zero!")
#         flag = False
#     elif numar == 5 :
#         print("Iesire program.")
#         flag = False
#     else :
#         print("Optiune nepermisa. Alege o optiune valida!")
#         numar = int(input("Optiunea ta este: "))

'''# 35. Sa se afiseze toate puterile lui 2 aflate intre un interval dat de utilizator.
# Exemplu: 10, 50 -> 16, 32 '''

# lim_min = int(input("Introdu limita inferioara: "))
# lim_max = int(input("Introdu limita superioara: "))
# val = 2
# for i in range(1, int(lim_max/2) + 1):
#     val = 2 ** i
#     if lim_min < val & val <lim_max :
#         print(val)

'''# 36. Creează o listă cu 7 numere întregi, apoi afișează suma și media elementelor fara a utiliza functiile sum() si avg().
# Exemplu: [1,2,3,4,5,6,7] -> suma=28, media=4.0 '''

# lista = [1,2,3,4,5,6,7]
# sum = 0
# for i in lista:
#     sum += i
# print("Suma elementelor este: ", sum)
# print("Media elementelor este: ", sum/len(lista))

'''# 37. Primește o listă de la tastatură (elemente separate prin spațiu) și afișează lista inversată.
# Exemplu: input: 1 2 3 4 5 -> output: [5,4,3,2,1] '''

# lista = input("Introdu o lista de elemente separate prin spatiu: ").split()
# lista_inversata = lista[::-1]
# print("Lista inversată este:", lista_inversata)

# sau

# lista = input("Introdu o lista de elemente separate prin spatiu: ").split()
# lista_inversata = list(reversed(lista))
# print("Lista inversată este:", lista_inversata)

'''# 38. Afișează toate elementele de pe poziții impare dintr-o listă dată.
# Exemplu: [10,20,30,40,50,60] -> 20,40,60 '''

#.       0. 1. 2. 3. 4. 5. 
# lista = [10,20,30,40,50,60]
# for i in range(1, len(lista), 2):
#     print(lista[i])

'''# 39. Înlocuiește toate aparițiile unui element dat cu altă valoare într-o listă.
# Exemplu: [1,2,3,2,4], inlocuieste 2 cu 5 -> [1,5,3,5,4] '''

# lista = [1,2,3,2,4]
# for i in range(len(lista)):
#     if lista[i] == 2:
#         lista[i] = 5
# print(lista)

# sau 

# lista = [1,2,3,2,4]
# lista2 = []
# for i in lista :
#     if i == 2 :
#         lista2.append(5)
#     else :
#         lista2.append(i)
# print(lista2)

# sau

# a = [1,2,3,2,4]
# userinput = input('please choose a number from 1-4: ')
# x = int(input("What's the new number? "))
# a = [num if num != int(userinput) else x for num in a]
# print(a)

'''# 40. Afișează elementul maxim și minim dintr-o listă fără a folosi funcțiile max/min.
# Exemplu: [3,1,4,1,5,9,2] -> max=9, min=1 '''

# lista = [3,1,4,1,5,9,2]
# maxim = lista[0]
# minim = lista[0]
# for i in lista :
#     if i > maxim :
#         maxim = i
#     if i < minim :
#         minim = i
# print("Maximul este: ", maxim)
# print("Minimul este: ", minim)

'''# 41. Elimină toate elementele pare dintr-o listă de numere.
# Exemplu: [1,2,3,4,5,6] -> [1,3,5] '''

# lista = [1,2,3,2,5,6]
# for i in lista :
#     if i % 2 == 0 :
#         lista.remove(i)
# print(lista)

'''# 42. Primește o listă de stringuri și construiește o nouă listă cu stringurile care conțin litera 'a'.
# Exemplu: ['ana', 'mere', 'casa', 'masina'] -> ['ana', 'casa', 'masina'] '''

# lista = ['ana', 'mere', 'casa', 'masina']
# lista_noua = []
# for i in lista :
#     for x in i :
#         if x == 'a' :
#             lista_noua.append(i)
#             break
# print("Lista ce contine cuvinte cu litera 'a' este: ",lista_noua)

# # sau 

# mylist = ['ana', 'mere', 'casa', 'masina']
# mylist2 = []
# for word in mylist:
#     if "a" in word:
#         mylist2.append(word)
# print(mylist2)

'''# 43. Verifică dacă o listă este palindrom (se citește la fel de la stânga la dreapta și invers).
# # Exemplu: [1,2,3,2,1] -> True, [1,2,3,4] -> False '''

# lista = [1,2,3,2,1]
# flag = True
# for i in range(len(lista) // 2):
#     if lista[i] != lista[-(i + 1)]:
#         flag = False
#         break
# if flag:
#     print("Lista este palindrom.")
# else:
#     print("Lista nu este palindrom.")

'''# 44. Interclasează două liste de aceeași lungime într-o singură listă.
# # Exemplu: [1,2], [3,4] => [1,3,2,4] '''

# lista1 = [1,2]
# print(lista1)
# lista2 = [3,4]
# print(lista2)
# lista1.extend(lista2)
# print(lista1)

'''# 45. Creează o listă de liste [index, valoare] pentru fiecare element dintr-o listă dată.
# # Exemplu: [10,20,30] -> [[0,10],[1,20],[2,30]] '''

# lista = [10,20,30]
# lista2 = []
# for i in range(len(lista)) :
#     lista2.append([i, lista[i]])
# print(lista2)

'''# 46. Primește o listă de numere și elimină toate elementele care apar de mai mult de o dată (păstrează doar elementele unice).
# Fara a folosi set().
# # Exemplu: [1,2,2,3,4,4,5] -> [1,3,5] '''

# lista = [1,2,2,3,4,4,5]
# lista_unica = []
# for i in lista:
#     if lista.count(i) == 1:
#         lista_unica.append(i)
# print(lista_unica)

'''# 47. Primește o listă de numere și grupează elementele în două liste: una cu numere negative, alta cu numere pozitive și zero.
# # Exemplu: [10,-1,2,-3,0,4,-5] -> negative: [-1,-3,-5], pozitive_si_zero: [10,2,0,4]'''

# lista = [10,-1,2,-3,0,4,-5]
# negative = []
# restul = []
# for i in lista :
#     if i < 0 :
#         negative.append(i)
#     else : # i>= 0
#         restul.append(i)
# print("Numerele negative : ",negative)
# print("Pozitive si zero : ",restul)

'''# 48. Primește o listă de stringuri și sorteaz-o crescător după numărul de vocale din fiecare string.
# Fara a folosi functia sort() sau sorted().
# # Exemplu: ['ana', 'masina', 'casa', 'mere'] -> ['ana', 'casa', 'mere', 'masina'] '''

# lista  = ['ana', 'masina', 'casa', 'mere']
# vocale = 'aeiou'
# temporar = ''
# for i in range(len(lista)):
#     for j in range(i + 1, len(lista)):
#         count_i = 0
#         for char in lista[i]:
#             if char in vocale:
#                 count_i += 1
#         count_j = 0
#         for char in lista[j]:
#             if char in vocale:
#                 count_j += 1
#         if count_i > count_j:
#             # lista[i], lista[j] = lista[j], lista[i] 
#             temporar = lista[i] 
#             lista[i] = lista[j] 
#             lista[j] = temporar
# print(lista)   

'''# 49. Primește o listă de liste (matrice) și calculează suma elementelor de pe diagonala principală (doar dacă matricea este pătratică).
# # Exemplu: [[1,2,3],[4,5,6],[7,8,9]] -> 15 (1+5+9) '''

# lista = [[1,2,3],[4,5,6],[7,8,9]]
# lista = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# lista = [ [1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25] ]
# count_i = 0
# sum_diag = 0
# for i in lista :
#     if len(i) == len(lista) :
#         count_i = count_i + 1
# if count_i == len(lista) :
#     for j in range(len(lista)) :
#         sum_diag = sum_diag + lista[j][j]
#     print("suma este : ",sum_diag)
# else :
#     print ("nu e matrice patratica")

'''# 50. Se da lista: [ [10, 5, 29] , ["Marian", "Ionut", "Marcel"] , [10.2, 7.5, 3.4] ]. Sa se extraga numele "Ionut" si sa se afiseze.'''

# lista = [ [10, 5, 29] , ["Marian", "Ionut", "Marcel"] , [10.2, 7.5, 3.4] ]
# for i in lista :
#     for j in i :
#         if j == "Ionut" : 
#             print(j)

# for sublista in lista:
#     for element in sublista:
#         if element == "xxxxx":
#             print(element)

'''# 51. Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]. Sa se extraga litera "r" din numele "Marcel" si sa se afiseze.'''

# lista = [ [10, 5, 29], ["Marian", "Ionut", "Marcel"] , [10.2, 7.5, 3.4] ]
# for sublista in lista :
#     #print("Sublista",type(sublista),sublista)
#     for element in sublista[-1::] :
#         #print("Element",type(element),element)
#         if type(element) == str :
#             for caracter in element :
#                 #print("Caracter",type(caracter),caracter)
#                 if caracter == "r":
#                     print(caracter," din ",element)

'''# 52. Sa se numere de cate ori apare un element intr-o lista incluzand si listele imbricate.
# Exemplu: [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]] si elementul 1 -> apare de 4 ori '''

# lista = [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]]
# element_cautat = 1
# count = 0
# for i in lista :
#     if type(i) == list : # verificam daca elementul este o lista
#         for j in i : 
#             if type(j) == list :
#                 for k in j :
#                     if k == element_cautat :
#                         count = count + 1
#             else :
#                 if j == element_cautat :
#                     count = count + 1
#     else :
#         if i == element_cautat :
#             count = count + 1
# print("Elementul ", element_cautat, " apare de ", count, " ori.")

# sau 

# lista = [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]]
# text_lista = str(lista) #convertim lista intr-un string cu tot de paranteze, virgule si spatii
# rezultat = text_lista.count('1')
# print(rezultat)

# sau

# lista_elemente = [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]]
# element = 1
# count = 0
# index = 0
# while index < len(lista_elemente):
#     if isinstance(lista_elemente[index], list):
#         lista_elemente.extend(lista_elemente[index])
#     else:
#         if lista_elemente[index] == element:
#             count += 1
#     index += 1

'''# 53. Scrieti un program care sa genereze un numar aleator intre 1 si 100. Utilizatorul trebuie sa
# ghiceasca numarul, iar programul sa ii ofere indicatii daca numarul introdus este mai mare sau mai mic decat cel generat.
# Programul se termina cand utilizatorul ghiceste numarul corect sau daca introduce cuvantul exit. 
# La final se afiseaza numarul de incercari facute.'''

# import random
# numar_random = random.randint(1,100)
# print(numar_random) # de test sa verific daca functioneaza
# nr_g = ''
# count = 1
# flag = True
# while flag :
#     nr_ales = input("Ghiceste numar : ")
#     if nr_ales == "exit" :
#         break
#     if numar_random == int(nr_ales) :
#         print ("ai gasit numarul")
#         flag = False
#     elif int(nr_ales) > numar_random :
#         print("Numarul ghicit e mai mare ")
#         count += 1
#     else :
#         print("Numarul ghicit e mai mic ") 
#         count += 1
# print("Ti-a luat "+str(count)+" incercari sa ghicesti")

# sau 

# import random
# def cere_numar():
#     """Cere input de la utilizator și îl returnează."""
#     return input("Introdu un număr (sau 'exit' pentru a ieși): ")
# def main():
#     """Docstring main"""
#     numar_aleator = random.randint(1, 100)
#     while True:
#         raspuns = cere_numar()
#         if raspuns.upper() == "EXIT":
#             print("Joc încheiat.")
#             break
#         try:
#             incercare = int(raspuns)
#         except ValueError:
#             print("Te rog introdu un număr valid sau 'exit'.")
#             continue
#         if incercare > numar_aleator:
#             print("Numărul tău este prea mare!")
#         elif incercare < numar_aleator:
#             print("Numărul pe care îl cauți este mai mare.")
#         else:
#             print(f"Felicitări! Ai ghicit numărul {numar_aleator}!")
#             break
# if name == "main":
#     main()

'''# 54. Sa se scrie un program primeste date in urmatorul format: 
# "Nume: Ionescu Prenume: Ion" pana cand se introduce caracterul #. 
# Programul trebuie sa stocheze toate datele citite, iar la final sa le afiseze in ordine alfabetica
# in functie de numele de familie.'''

# lista = []
# sublista = []
# while True :
#     data = input("Introdu un nume :")
#     if data == "#" :
#         print("iesire")
#         break
#     else : 
#         sublista.append(data)
#         data = input("Introdu un prenume :")  
#         sublista.append(data)      
#         lista.append(sublista)
#         # treci pe indexul urmator in lista
#         sublista = [] # resetare sublista pentru urmatorul nume prenume
# lista.sort()
# print("Lista sortata este : ",lista)

# sau Chat GPT

# persoane = []
# for _ in range(1000):   # număr suficient de mare iar _ pentru că nu folosim valoarea
#     linie = input("Introdu datele: ")
#     if linie == "#":
#         break
#     parti = linie.split()
#     nume = parti[0]
#     prenume = parti[1]
#     persoane.append([nume, prenume])
# persoane.sort(key=lambda x: x[0])
# for p in persoane:
#     print(f"Nume: {p[0]} Prenume: {p[1]}")

# sau Visual Studio

# date_intrare = []
# while True :
#     date = input("Introduceti datele in formatul 'Nume: Ionescu Prenume: Ion' sau '#' pentru a termina: ")
#     if date == "#" :
#         break
#     date_intrare.append(date)
# date_intrare.sort()
# print("Datele in ordine alfabetica dupa numele de familie:")
# for date in date_intrare :
#     print(date)

'''# 55. Sa se scrie un program care sa implementeze un joc de tip quiz cu adevarat/fals. Sa se foloseasca o lista de intrebari.
# La final sa se afiseze scorul obtinut de utilizator. Se poate folosii random pentru a amesteca intrebarile. '''

# import random
# name = input("Care este numele tau ? ")
# print("Multumesc," + " " + name)
# print("Regulile sunt urmatoarele :")
# print("1. Set de intrebari cu punctaj si raspuns cu T sau F")
# print("2. La final se afiseaza scorul")
# scor = 0

# varianta 1 -------------
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

# sau

# varianta 2 -------------
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

'''# 56. Sa se sccrie un prog care verifica complexitatea unei parole. 
# Cel putin 10 caractere, cel putin o litera, cel putin un caracter special, cel putin o cifra. '''

# # create list for special characters
# pool_special = [ '!' , '#' , '$' , '%' , '&' , '(' , ')' , '*' , '+' , ',' , '-' , '.' , '/' , ':' , ';' , '<' , '=' , '>' , '?' , '@' , '^' , '_' , '' , '|' , '~' ]

# # create list for letters
# pool_letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

# # create list for digits
# pool_digits = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]

# # ask user to enter the password following the mentioned rules
# print("The password's lenght must be grater than 10 and contain at least one letter, one special character and one digit")
# password = input('Type your password : ')

# # the key varriable turns true if the password meet the requirements
# # start the loop as if the password doesn't meet the requirements
# key = False
# flag_special = False
# flag_letters = False
# flag_digits = False
# flag_len = False

# while key == False :    
#     for p in password :
#         for s in pool_special :
#             if s == p :
#                 flag_special = True
#                 break
#         for l in pool_letters :
#             if l == p or l.upper() == p :
#                 flag_letters = True
#                 break
#         for d in pool_digits :
#             if d == p :
#                 flag_digits = True
#                 break
#     if len(password) > 9 :
#         flag_len = True
#     if flag_special and flag_letters and flag_digits and flag_len :        
#         key = True
#     else :
        # print status to check and reset all flags in order to avoid partial checks
#         print ('Special :', flag_special, 
#                '---- Letter :',flag_letters, 
#                '---- Digits :', flag_digits, 
#                '---- Length :', flag_len)
#         flag_special = False
#         flag_letters = False
#         flag_digits = False
#         flag_len = False
#         print('Requirements not met ')
#         password = input('Re-Type your password : ')

# if key == True :
#     print('Your password is : ' + password)
# else :
#     print('Errrrr.....')

# sau optimised version

# def password_check(password) :
#     if len(password) < 9 :
#         print ('Not long enough')
#         return False
    
#     big = any(c.isupper() for c in password)
#     small = any(c.islower() for c in password)
#     digit = any(c.isdigit() for c in password)
#     alfanum = any(not c.isalnum() for c in password)

#     return all([big, small, digit, alfanum])

# password = input ("Enter password : ")

# if password_check(password) :
#     print("All good ✅ : ", password)
# else:
#     print("Not good enough ❌")

'''# Folositi list comprehension pentru a rezolva urmatoarele exercitii : '''
'''# 57. Creeaza o lista cu patratele numerelor de la 0 la 9. Ex: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] '''

# lista = [i**2 for i in range(10)]
# print (lista)

'''# 58. Creeaza o lista cu toate numerele pare divizibile cu 3 de la 1 la 50 inclusiv. Ex: [6, 12, 18, 24, 30, 36, 42, 48] '''

# lista = [i for i in range(50) if i%3 == 0 and i%2 == 0]
# print (lista)

'''# 59. Dintr-o lista cu cuvinte creeaza o lista cu lungimile fiecarui cuvant. Ex: ['ana', 'maria', 'ion', 'marioara', '1468912'] -> [3, 5, 3, 8, 7] '''

# lista = ['ana', 'maria', 'ion', 'marioara', '1468912']
# lungime = [ len(i) for i in lista ]
# print(lungime)

'''# 60. Dintr-o lista cu numere de la 1 la 50, creeaza o lista cu patratele numerelor care sunt divizibile cu 4 si cu 6. Ex: [144, 576, 1296, 2304] '''

# lista = [i**2 for i in range(1,25) if i%4 == 0 and i%6 == 0]
# print (lista)

'''# 61. Creeaza o lista cu toate vocalele dintr-un text dat. 
# Ex: 'Aceasta este o propozitie de test.' -> ['A', 'e', 'a', 'a', 'e', 'o', 'o', 'i', 'i', 'e', 'e'] '''

# lista = input("Introdu text : ")
# lista_vocale = "aeiouAEIOU"
# lista_extrase = [char for char in lista if char in lista_vocale]
# print("Lista vocalelor extrase este : ", lista_extrase)

'''# Folositi any pentru rezolvarea urmatoarelor exercitii:
# 62. Verifica daca intr-o lista de numere exista cel putin un numar par. Ex: [1, 3, 5, 7, 8] -> True '''

# lista = [1, 3, 5, 7, 9]
# verificare = any(i%2 == 0 for i in lista)
# print(verificare)

'''# 63. Verifica daca intr-o lista de cuvinte exista cel putin un cuvant care sa contina litera 'z'. Ex: ['azna', 'maria', 'ioana', 'ebra'] -> True '''

# lista = ['ana', 'maria', 'ioana', 'zebra']
# verificare = any('z' for i in lista)
# print(verificare)

'''# 64. Verifica daca intr-o lista de numere exista cel putin un numar negativ. Ex: [4, 5, -1, 3, 0] -> True '''

# lista = [4, 5, -1, 3, 0]
# verificare = any(i for i in lista if i <0 )
# print(verificare)

'''# 65. Verifica daca intr-o lista de stringuri exista cel putin un string care sa fie gol. Ex: ['ana', '', 'maria'] -> True '''

# lista = ['ana', '', 'maria']
# verificare = any( i == "" for i in lista)
# print(verificare)

'''# 66. Verifica daca intr-o lista de caractere exista cel putin o vocala mare (A, E, I, O, U). Ex: ['a', 'b', 'C', 'D', 'E'] -> True  '''

# lista = ['a', 'b', 'C', 'D', 'E']
# lista_vocale = "AEIOU"
# verificare = [char for char in lista if char in lista_vocale]
# print("Lista vocalelor extrase este : ", verificare)
# verificare_bool = any([char for char in lista if char in lista_vocale])
# print("Adev sau fals : ", verificare_bool)

'''# Exercitii pentru tuples: '''
'''# 67. Creează un tuplu care conține numele a trei fructe și afișează-le pe ecran. '''
#     Exemplu: ('măr', 'banană', 'cireașă') -> măr, banană, cireașă

# Se da tuplul: fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi').

# fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')
# for i in fructe :
#     print(i)

'''# 68. Afișează al doilea și al patrulea fruct din tuplu. '''

# fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')
# print(fructe[1], fructe[3])

'''# 69. Afișează tuplul inversat. '''

# fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')
# fructe_inversate = tuple(reversed(fructe)) # tuple apare „în față” pentru că reversed() NU returnează un tuple, ci un iterator.
# print(fructe_inversate)

# sau cu slicing

# fructe_inversate = fructe[::-1]
# print(fructe_inversate)


'''# 70. Verifică dacă 'kiwi' este în tuplu și afișează un mesaj corespunzător. '''

# fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')
# print('kiwi' in fructe) # -------> True

# sau

# if 'kiwi' in fructe :
#     print("Am gasit kiwi in fructe")
# else :
#     print("Nu am gasit kiwi in fructe")

'''# 71. Creează un tuplu nou care conține doar fructele de la pozițiile(index) pare din tuplul original. '''

# fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')

# fructe_noi = fructe[::2]
# print("varianta 1 ", fructe_noi)

# sau 

# fructe_noi2 = tuple(fructe[i] for i in range(len(fructe)) if i % 2 == 0)
# print("varianta 2 ", fructe_noi2)

# sau 

# fructe_noi3 = tuple(elem for i, elem in enumerate(fructe) if i % 2 == 0)
# print("varianta 3 ", fructe_noi3)

'''# 72. Afișează lungimea fiecarui element din tuplu. '''

# fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')
# lungime = tuple(len(i) for i in fructe)
# print(lungime)

'''# 73. Concatenează tuplul cu un alt tuplu care conține alte două fructe și afișează rezultatul. '''

# fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')
# legume = ('rosie', 'cartof', 'varza')
# lista_cumparaturi = fructe + legume 
# print(lista_cumparaturi)

# sau prin conversie la liste si apoi afisare ca tuple

# lista_fructe = list(fructe)
# lista_legume = list(legume)
# lista_fructe.extend(lista_legume)
# print(tuple(lista_fructe))

# sau dar nu merge

# fructe = fructe.extend(legume) # extend nu se aplica la tuple doar la liste pentru ca string-ul este immutable
# print(fructe) # nu o sa mearga

'''# 74. Adauga un fruct nou 'ananas' in tuplu. '''

# fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')
# fructe += ('ananas',)
# print(fructe)

'''# 75. Se da tuplul: ('măr', 'banană', 'cireașă'). Faceti unpacking pentru a extrage fiecare element in variabile separate si afisati-le. '''

# fructe = ('măr', 'banană', 'cireașă')
# a,b,c = fructe
# print("Unpacking : ",a,b,c)

'''# Exerciții pentru seturi: '''
'''# 76. Creează un set care conține numele a cinci culori și afișează-le pe ecran. '''

# culori = {'rosu', 'galben', 'albastru', "verde", 'portocaliu' }
# for culoare in culori :
#     print(culoare)

'''# 77. Adaugă o culoare nouă în setul de mai sus și afișează setul actualizat. '''

# culori = {'rosu', 'galben', 'albastru', "verde", 'portocaliu' }
# culori.add("negru") # il adauga pe pozitie random
# print(culori)

'''# 78. Elimină o culoare din set și afișează setul actualizat. '''

# culori = {'rosu', 'galben', 'albastru', "verde", 'portocaliu' }
# culori.remove("rosu")
# print(culori)

'''# 79. Verifică dacă o anumită culoare (de exemplu, 'albastru') este în set și afișează un mesaj corespunzător. '''

# culori = {'rosu', 'galben', 'albastru', "verde", 'portocaliu' }
# if 'albastru' in culori : 
#     print("gasit")
# else :
#     print("nu am gasit")

'''# 80. Creează un alt set cu alte trei culori și afișează elementele comune din cele două seturi. '''

# culori = { 'rosu', 'galben', 'albastru', "verde", 'portocaliu' }
# culori2 = { 'rosu', 'galben', 'albastru', 'alb', 'gri' }
# print("Culori comune", culori.intersection(culori2))  # --------> {'rosu', 'galben', 'albastru'}
# sau 
# print(culori & culori2)

'''# 81. Afișează toate culorile din primul set care nu sunt în al doilea set. '''

# culori = {'rosu', 'galben', 'albastru', "verde", 'portocaliu' }
# culori2 = {'rosu', 'galben', 'albastru', 'alb', 'gri' }

# culori_diferite = culori.difference(culori2)
# print("diferite",culori_diferite) # --------> {'portocaliu', 'verde'}
# sau
# print("sau asa : ",culori - culori2) # --------> {'portocaliu', 'verde'}

'''# 82. Se da lista: [1, 3, 5, 1, 6, 7, 9, 9, 1, 3, 4, 7, 1, 6, 7, 9, 5, 3, 3, 2, 1, 8, 4]. Eliminati duplicatele din lista, 
# astfel incat fiecare element sa apara o singura data.'''

# numere = [1, 3, 5, 1, 6, 7, 9, 9, 1, 3, 4, 7, 1, 6, 7, 9, 5, 3, 3, 2, 1, 8, 4]
# numere_duble = list(set(numere)) # daca se doreste returnare tot in lista
# print(numere_duble)

'''# 83. Exercitiu extra:
# Se dau urmatoarele expresii matematice:
# ( (a + b) * (c - d) + e ) / f - ( g * (h + i) ) -> corect deschise si inchise
# ( (a + b) * (c - d) + e ) / f - ) g * (h + i) ( -> incorect deschise si inchise
# Sa se verifice daca parantezele sunt corect deschise si inchise. '''

# expresie = "( (a + b) * (c - d) + e ) / f - ) g * (h + i) ("
# expresie = "( (a + b) * (c - d) + e ) / f - ( g * (h + i) )"
# contor = 0
# for i in expresie :
#     if contor < 0 :
#         break
#     if i == "(" :
#         contor += 1
#     elif i == ")" :
#         contor -= 1
# if contor == 0 :
#     print ("Corect")
# else : 
#     print("Incorect")

# sau cu lista cu verificare ordine inchideri si deschideri

# expresie = "( (a + b) * (c - d) + e ) / f - ) g * (h + i) ("
# expresie = "( (a + b) * (c - d) + e ) / f - ( g * (h + i) )"
# stiva = []
# flag = True
# for i in expresie :
#     if i == "(" :
#         stiva.append(i)
#     elif i ==")" :
#         if not stiva :
#             flag = False
#             break
#         else : 
#             stiva.pop()
# if flag and len(stiva) == 0 :
#     print("corect")
# else : 
#     print ("incorect")

'''# 84. Verifica daca intr-o lista de cuvinte exista cel putin un cuvant care sa contina litera 'z'. 
# Ex: ['ana', 'maria', 'ioana', 'zebra'] -> True '''

# lista = ['ana', 'maria', 'ioana', 'zebra']
# verificare = any('z' in i for i in lista)
# print(verificare)

'''# 85. Dintr-o lista cu numere de la 1 la 50, creeaza o lista cu patratele numerelor care sunt divizibile cu 4 si cu 6.
# Ex: [144, 576, 1296, 2304] '''

# lista = [i**2 for i in range(1,51) if i%4 == 0 and i%6 == 0]
# print (lista)

'''# 86. Creeaza un dictionar care sa contina numele si varsta a 5 persoane.'''

# dic_persoane = {"paul" : 31, "catalin" : 21, "aura" : 25, "mama" : 50, "tata" : 52}

'''# 87. Afiseaza varsta unei persoane specifificate de utilizator.'''

# dic_persoane = {"paul" : 31, "catalin" : 21, "aura" : 25, "mama" : 50, "tata" : 52}
# varianta = input("Introdu persoana la care doresti sa afisezi varsta: ")
# flag = True
# while flag : 
#         if varianta == "paul" :
#                 print(dic_persoane["paul"])
#         elif varianta == "catalin" :
#                 print(dic_persoane["catalin"])
#         elif varianta == "aura" : 
#                 print(dic_persoane["aura"])
#         elif varianta == "mama" :
#                 print(dic_persoane["mama"])
#         elif varianta == "tata" :
#                 print(dic_persoane["tata"])
#         else :
#                 print("Persoana nu exista in dictionar")
#                 break
#         varianta2 = input("Mai vrei sa afisezi si alta varsta ? y/n  ")
#         if varianta2 == "y" :
#                 varianta = input("Introdu persoana la care doresti sa afisezi varsta: ")
#         else : 
#                 flag = False

'''# 88. Afiseaza cea mai mare si cea mai mica varsta din dictionar.'''

# persoane = {"paul" : 31, "catalin" : 21, "aura" : 25, "mama" : 50, "tata" : 52}
# cea_mai_mica = min(persoane.values())
# cea_mai_mare = max(persoane.values())
# print("Cea mai mică vârstă:", cea_mai_mica)
# print("Cea mai mare vârstă:", cea_mai_mare)

'''# 89. Adauga 3 noi persoane in dictionar.'''

# persoane = {"paul" : 31, "catalin" : 21, "aura" : 25, "mama" : 50, "tata" : 52}
# persoane["Ana"] = 25
# persoane["Pope"] = 27
# persoane["Benny"] = 3
# print(persoane)

'''# 90. Afiseaza varsta medie a persoanelor din dictionar.'''

# persoane = {"paul" : 31, "catalin" : 21, "aura" : 25, "mama" : 50, "tata" : 52}
# suma = 0
# for x in persoane.values() :
#     suma += x
# medie = suma / len(persoane)
# print("Media varstelor este : ",medie)

'''# 91. Sterge o persoana specificata de utilizator din dictionar.'''

# dic_persoane = {"paul" : 31, "catalin" : 21, "aura" : 25, "mama" : 50, "tata" : 52}
# print("Acestea sunt persoanele : ")
# for x in dic_persoane.keys():
#         print(x)
# varianta = input("Introdu persoana pe care doresti sa o stergi: ")
# flag = True
# while flag : 
#         if varianta == "paul" :
#                 dic_persoane.pop("paul")
#                 print("Persoanle ramase sunt :")
#                 for x in dic_persoane.keys():
#                     print(x)
#         elif varianta == "catalin" :
#                 dic_persoane.pop("catalin")
#                 print("Persoanle ramase sunt :")
#                 for x in dic_persoane.keys():
#                     print(x)
#         elif varianta == "aura" : 
#                 dic_persoane.pop("aura")
#                 print("Persoanle ramase sunt :")
#                 for x in dic_persoane.keys():
#                     print(x)
#         elif varianta == "mama" :
#                 dic_persoane.pop("mama")
#                 print("Persoanle ramase sunt :")
#                 for x in dic_persoane.keys():
#                     print(x)
#         elif varianta == "tata" :
#                 dic_persoane.pop("tata")
#                 print("Persoanle ramase sunt :")
#                 for x in dic_persoane.keys():
#                     print(x)
#         else :
#                 print("Persoana nu exista in dictionar")
#                 break
#         varianta2 = input("Mai vrei sa stergi si alta persoana ? y/n  ")
#         if varianta2 == "y" :
#                 varianta = input("Introdu persoana pe care doresti sa o stergi: ")
#         else : 
#                 flag = False

'''# 92. Afiseaza toate persoanele cu varsta peste o valoare specificata de utilizator.'''

# dic_persoane = {"paul" : 31, "catalin" : 21, "aura" : 25, "mama" : 50, "tata" : 52}
# varsta = int(input("Introdu varsta pentru care vrei sa afisezi persoanele ce depasesc minimul :"))
# minimul = min(dic_persoane.values())
# if varsta < minimul :
#         print("Nu avem persoane")
# else : 
#     for x in dic_persoane:
#         if dic_persoane[x] > varsta:
#             print(x)

'''# 93. Afiseaza toate persoanele din dictionar in urmatorul format: "Nume: <nume_persoana>, Varsta: <varsta_persoana>".'''



'''
Exercitii pentru dictionare:

9) Verifica daca o persoana specificata de utilizator exista in dictionar.
10) Actualizeaza varsta unei persoane specificate de utilizator.
11) Afiseaza numarul total de persoane din dictionar.
12) Creeaza o lista cu toate numele persoanelor din dictionar si afiseaza-le.
13) Creeaza un nou dictionar care sa contina doar persoanele cu varsta peste 18 ani.
14) Creeaza o lista care contine toate varstele din dictionar, fara duplicate, si afiseaz-o.
15) Afiseaza persoana cu cea mai apropiata varsta de o valoare specificata de utilizator.
16) Afiseaza toate persoanele grupate dupa decadele varstei (0-9, 10-19, 20-29, etc.).
17) Afiseaza persoanele sortate alfabetic dupa nume. (Utilizati functia sorted pentru a rezolva acest exercitiu).
18) Afiseaza persoanele sortate dupa varsta, de la cea mai mica la cea mai mare. (Utilizati functia sorted pentru a rezolva acest exercitiu).
   (Folositi functia sorted() si pentru cheia de sortare (key) accesati valorile dictionarului).
19) Se da urmatorul text: "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani".
    Creeaza un dictionar care sa contina numele persoanelor ca si chei si varstele ca si valori.
20) Se da urmatorul text: "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani".
    Creeaza un dictionar care sa stocheze frecventa literelor din text si afiseaza-l. Exemplu: {'a': 7, 'n': 3, ... }.
'''

'''
Exercitii Functii Python:
1) Scrie o funcție care primește un nume și afișează "Salut, <nume>!".
2) Scrie o funcție care primește două numere și returnează suma lor.
3) Scrie o funcție care primește două numere și returnează suma, diferența și produsul lor (returnează un tuple).
4) Scrie o funcție care primește un număr și returnează True dacă este par, altfel False.
5) Scrie o functie care primeste ca parametru un numar si modifica valoarea unei variabile globale cu valoarea numarului la patrat.
'''

''' # 5) Scrie o funcție care primește o listă de numere de la tastatura cu spatii si | și returnează suma tuturor numerelor. '''
'''# 1 | 3 | 4 | 6 | 9 | 75'''

# def suma_numere(lista) :
#     suma = 0 
#     for i in lista :
#         suma+= i
#     return suma

# char = input("Introdu sirul")
# numar_clar = char.split("|")
# lista = [int(i.strip()) for i in numar_clar]
# rezultat = suma_numere(lista)
# print("Rezultatul este : ", rezultat)

'''
6) Scrie o funcție care primește un string și returnează stringul inversat.
7) Scrie o funcție care primește o listă de stringuri și returnează o listă cu lungimile fiecărui string.
8) Scrie o funcție care primește doua liste de numere si returneaza o lista cu numerele comune celor doua liste.
9) Scrie o functie care primeste un dictionar de forma {nume: varsta} si returneaza numele persoanei cu cea mai mica varsta.
10) Scrie o functie care primeste un dictionar de forma {nume: varsta} si returneaza un dictionar cu persoanele care au varsta peste 18 ani.'''

# Nume - Ionescu | Varsta - 18
# Nume - Popescu | Varsta - 15
# Nume - Ana | Varsta - 21
# Nume - Paul | Varsta - 31

# persoane = {}
# def filtru (persoane):
#     rezultat = {}
#     for nume, varsta in persoane.items() :
#         if int(varsta) >= 18 :
#             rezultat[nume] = varsta
#     return rezultat
# while True :
#     date = input("Introdu datele : ")
#     if date == 'stop' :
#         break
#     date_separate = date.split()
#     nume = date_separate[2]
#     varsta = date_separate[-1]
#     persoane[nume] = varsta
# print(filtru(persoane))

'''
11) Scrie o functie care primeste o lista de numere si un numar n, si returneaza o lista cu numerele mai mici decat n.
12) Scrie o functie care primeste o lista de numere si returneaza cel mai mic numar, cel mai mare numar si media aritmetica a numerelor din lista.
13) Scrie o functie care primeste o lista de numere si returneaza un dictionar cu frecventa fiecarui numar in lista (cheia este numarul, valoarea este frecventa). '''

# def frecv_numere(lista) : 
#     dictionar = {}
#     for x in lista : 
#         if x in dictionar :
#             dictionar[x] += 1
#         else :
#             dictionar[x] = 1 
#     return dictionar

# numere = [10, 20, 10 ,20 ,30, 40, 30 ,40 ,50]
# rezultat = frecv_numere(numere)
# print(rezultat)

'''
14) Scrie o functie care primeste o lista de numere si returneaza o lista care contine numerele fara duplicate.
15) Scrie o functie care primeste o lista de numere si returneaza o lista doar cu numerele prime.
'''

# Sa se scrie un program care tine evidenta elevilor dintr-o scoala. Programul trebuie sa dispuna de un meniu care ne pune la dispozitie urmatoarele optiuni:
# 		1. Adaugare elev
# 		2. Afisarea elevilor existenti
# 		3. Modificare informatii elev existent
# 		4. Stergere elev
# 		5. Cautare elev dupa nume si prenume
# 		6. Afisare elevi in ordinea mediilor
# 		7. Afisare elevi cu media peste 8
# 		8. Afisare elevi in ordine alfabetica (dupa nume)

# 	Pentru fiecare elev trebuie sa retinem urmatoarele informatii:
#     Nume
#     Prenume
#     Nota romana
#     Nota matematica
#     Nota engleza
#     Media

# print(
#     """
# 		1. Adaugare elev
# 		2. Afisarea elevilor existenti
# 		3. Modificare informatii elev existent
# 		4. Stergere elev
# 		5. Cautare elev dupa nume si prenume
# 		6. Afisare elevi in ordinea mediilor
# 		7. Afisare elevi cu media peste 8
# 		8. Afisare elevi in ordine alfabetica (dupa nume)
# """
# )

# elevi = [{'nume': 'popescu', 'prenume': 'ana', 'nota romana': 6.0, 'nota mate': 7.0, 'nota engleza': 8.0, 'media': 7.0}, 
#          {'nume': 'abesei', 'prenume': 'paul', 'nota romana': 7.0, 'nota mate': 8.0, 'nota engleza': 9.0, 'media': 8.0},
#          {'nume': 'popescu', 'prenume': 'andrei', 'nota romana': 3.0, 'nota mate': 4.0, 'nota engleza': 5.0, 'media': 4.0}
#          ]

# def adauga_elev ():
#     nume = input("Nume : ")
#     prenume = input("Prenume : ")
#     nota_romana = float(input("Nota romana :"))
#     nota_mate = float(input("Nota mate :"))
#     nota_engl = float(input("Nota engleza :"))
#     elev = {
#         "nume": nume,
#         "prenume": prenume,
#         "nota romana" : nota_romana,
#         "nota mate" : nota_mate,
#         "nota engleza" : nota_engl,
#         "media" : calculeaza_media(nota_romana, nota_mate, nota_engl)
#     }
#     elevi.append(elev)

# def calculeaza_media(nota_romana, nota_mate, nota_engl):
#     x = round((nota_romana + nota_mate + nota_engl)/3,2)
#     return x

# def ia_media(elev):
#     return elev['media']

# def ia_nume(elev):
#     return elev['nume']

# def afiseaza_elevi():
#     for elev in elevi :
#         print(f"{elev['nume']} {elev['prenume']} | "
#             f"Romana: {elev['nota romana']} | "
#             f"Matematica: {elev['nota mate']} | "
#             f"Engleza: {elev['nota engleza']} | "
#             f"Media: {elev['media']}")
        
# def afisare_alfabetic():
#     elevi_sortati = sorted(elevi, key=ia_nume)
#     for elev in elevi_sortati:
#         print(f"{elev['nume']} {elev['prenume']}")
        
# def sterge_elevi():
#     nume = input("Ce nume vrei elimini ? ")
#     prenume = input("Ce prenume vrei sa elimini ?")
#     for elev in elevi :
#         if elev["nume"] == nume and elev["prenume"] == prenume:
#             elevi.remove(elev)
#             print("Am sters")
#             return
#     print("Elevul nu a fost gasit")

# def modificare ():
#     nume = input("Ce nume sa modific : ")
#     prenume = input("Ce prenume sa modific : ")
#     for elev in elevi: 
#         if elev['nume'] == nume and elev['prenume'] == prenume:
#             elev['nota romana'] = float(input("Nota roamana noua: "))
#             elev['nota mate'] = float(input("Nota mate noua: "))
#             elev['nota engleza'] = float(input("Nota engleza noua: "))
#             elev['media'] = calculeaza_media(elev['nota romana'], elev['nota mate'], elev['nota engleza'])
#             print("Date modificate success!")
#             return
#     print("Elev negasit!")

# def cauta_elevi():
#     nume = input("Ce nume vrei ? ")
#     prenume = input("Ce prenume vrei ?")
#     for elev in elevi :
#         if elev["nume"] == nume and elev["prenume"] == prenume:
#             print(f"{elev['nume']} {elev['prenume']} | "
#             f"Romana: {elev['nota romana']} | "
#             f"Matematica: {elev['nota mate']} | "
#             f"Engleza: {elev['nota engleza']} | "
#             f"Media: {elev['media']}")
#             return
#     print("Elevul nu a fost gasit")

# def afiseaza_media_crescator():
#     elevi_sortati = sorted(elevi, key=ia_media)
#     for elev in elevi_sortati:
#         print(f"{elev['nume']} {elev['prenume']} | Media: {elev['media']}")

# def medie_5 ():
#     for elev in elevi :
#         if elev['media'] >= 5:
#             print(f"{elev['nume']} {elev['prenume']} | Media: {elev['media']}")
            
# while True :
#     optiune = input("Alege optiune : ")
#     if optiune == '0' :
#         print("Ai iesit din sistem")
#         break
#     if optiune == "1" :
#         adauga_elev()
#     if optiune == "2" :
#         afiseaza_elevi()
#     if optiune == "3" :
#         modificare()
#     if optiune == "4":
#         sterge_elevi()
#     if optiune == "5":
#         cauta_elevi()
#     if optiune == "6":
#         afiseaza_media_crescator()
#     if optiune == "7":
#         medie_5()
#     if optiune == "8":
#         afisare_alfabetic()

"""
Exercitii Functii recursive:
1) Scrie o funcție recursivă care calculează factorialul unui număr.
Ex: pentru n = 5, 5 x 4 x 3 x 2 x 1 = 120
2) Scrie o funcție recursivă care calculează suma numerelor de la 1 la n.
Ex: pentru n=5, returnează 15 (1+2+3+4+5)
3) Scrie o functie recursiva care calculeaza cate cifre are un numar dat.
Ex: pentru 1234 returneaza 4
4) Scrie o functie recursiva care calculeaza adancimea(cate liste nivele de liste sunt) unei liste imbricate.
Ex: pentru [1, 2, [3, 4, [5, 6]], 7] returneaza 3
5) Scrie o functie recursiva care calculeaza suma tuturor elementelor dintr-o lista imbricata.
Ex: pentru [1, 2, [3, 4, [5, 6]], 7] returneaza 28
"""