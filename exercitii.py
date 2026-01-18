# Exerciții de vacanță – recapitulare Python (variabile, operatori, stringuri, control flow)
# Perioada: 23 decembrie – 11 ianuarie

# Încălzire (1-10):
# 1. Creează două variabile cu valori numerice și afișează suma lor.

# a = 5
# b = 10
# print("Suma celor doua numere este:", a+b)

# 2. Afișează produsul a două numere introduse de la tastatură.

# a = 5
# b = 10
# print("Suma celor doua numere este:", a*b)

# 3. Primește un nume de la tastatură și afișează-l cu litere mari.

# nume = input("Introdu numele:")
# print ("Numele tau este : ", nume.upper())

# 4. Afișează lungimea unui string introdus de la tastatură.

# sir = input("Introdu un sir de caractere : ")
# print("Lungimea sirului : ", len(sir))

# 5. Verifică dacă un număr este par sau impar.

# numar = int(input("Introdu un numar:"))
# if numar % 2 == 0 :
#     print("Numar par")
# else : 
#     print("Numar impar")

# 6. Primește un text și un caracter, afișează de câte ori apare caracterul în text.

# text = input ("Introdu un text: ")
# caracter = input("Introdu un caracter: ")
# print ("caracterul '", caracter , "' apare de ", text.count(caracter), " ori in textul introdus.")

# 7. Afișează ultimul caracter dintr-un string introdus de la tastatură.

# text = input ("Introdu un text: ")
# print("Ultimul caracter din text este: ", text[-1])

# 8. Primește un număr și afișează dacă este pozitiv, negativ sau zero.

# numar = input ("Introdu un numar: ")
# if float(numar) > 0 :
#     print("Numarul este pozitiv")
# elif float(numar) < 0 :
#     print("Numarul este negativ")
# else :
#     print("Numarul este zero")

# 9. Afișează toate caracterele unui string, câte unul pe linie.

# text = input ("Introdu un text: ")
# for i in text :
#     print(i)

# 10. Primește două numere și afișează cel mai mare dintre ele.

# numar1 = float(input("Introdu primul numar: "))
# numar2 = float(input("Introdu al doilea numar: "))
# if numar1 > numar2:
#     print("Primul numar este mai mare.")
# elif numar2 > numar1:
#     print("Al doilea numar este mai mare.")
# else:
#     print("Numerele sunt egale."

# 11. Primește trei numere și afișează cel mai mic si cel mai mare dintre ele.

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

# 12. Primește un text și verifică dacă este palindrom.
# 13. Primește o parolă și verifică dacă are cel puțin 8 caractere și conține o cifră.
# 14. Primește un text și construiește un nou string numai cu vocalele din el.

# text = input("Introdu un text: ")
# text_vocale = ""
# vocale = "aeiouAEIOU"
# for char in text:
#     if char in vocale:
#         text_vocale += char
# print("Textul format doar din vocale este:", text_vocale)

# 15. Primește un număr n și afișează toate numerele pare de la 0 la n (inclusiv).
# 16. Primește un text și afișează doar literele mici din el.
# 17. Primește două numere și afișează toate numerele între ele (inclusiv), în ordine crescătoare.
# 18. Primește un text și afișează fiecare cuvânt pe o linie nouă.
# 19. Primește un număr și afișează tabla înmulțirii pentru acel număr (de la 1 la 10).
# 20. Primește un text și verifică dacă toate caracterele sunt litere mici.
# 21. Primește un text și afișează-l inversat.
# 22. Primește o propoziție și numără câte cuvinte conține.
# 23. Primește un text și înlocuiește toate spațiile cu caracterul "_".
# 24. Primește un număr și afișează suma cifrelor sale.

# numar = input("Introdu un numar: ")
# suma_cifre = 0
# for cifra in numar:
#     suma_cifre += int(cifra)    
# print("Suma cifrelor numarului este:", suma_cifre)

# 25. Primește un text și afișează doar caracterele care sunt cifre.
# 26. Primește un text și verifică dacă începe și se termină cu aceeași literă.

# text = input("Introdu un text: ")
# if text[0].lower() == text[-1].lower():
#     print("Textul începe și se termină cu aceeași literă.")
# else:
#     print("Textul nu începe și nu se termină cu aceeași literă.")       

# 27. Primește un text și afișează toate caracterele distincte din el.

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

# 28. Primește un text și afișează literele care apar de exact două ori.

# text = input("Introdu un text: ")
# litere_doua_ori = ""
# for char in text:
#     if text.count(char) == 2 and char not in litere_doua_ori:
#         litere_doua_ori += char
# print("Literele care apar de exact doua ori sunt:", litere_doua_ori)

# 29. Primește un număr n și afișează toți divizorii săi.

# numar = int(input("Introdu un numar: "))
# divizori = []
# for i in range(1, numar + 1):
#     if numar % i == 0:
#         divizori.append(i)
# print("Divizorii numarului sunt:", divizori)

# 30. Primește un text și verifică dacă are cel puțin o literă mare, una mică și o cifră.

# Exercitii pentru oameni supraincalziti (31-33):
# 31. Fizz Buzz: Primește un număr n și afișează numerele de la 1 la n. Pentru multiplii de 3, afișează "Fizz", pentru multiplii de 5, afișează "Buzz", iar pentru multiplii de ambele, afișează "FizzBuzz".
# 32. Primește un text și afișează-l cu fiecare cuvânt inversat, dar în aceeași ordine. (Exemplu: "Ana are mere" -> "anA era erem")

# text = input("Introdu un text: ")
# cuvinte = text.split()          
# cuvinte_inversate = []
# for cuvant in cuvinte:
#     cuvinte_inversate.append(cuvant[::-1])
#     text_inversat = ' '.join(cuvinte_inversate)
# print("Textul cu cuvintele inversate este:", text_inversat)

# 33. Primește un text care contine o insiruire de numere și afișează media lor. (Exemplu: "1,2,3,4,5,10" -> 25/6 = 4.1666)

# text_numere = input("Introdu o insiruire de numere separate prin virgula: ")
# numere_str = text_numere.split(",")             
# numere = []
# for numar in numere_str:
#     numere.append(float(numar))
# media = sum(numere) / len(numere)
# print("Media numerelor este:", media)

# 34. Trebuie implementat un meniu interactiv in consola care pune la dispozitie utilizatorului urmatoarele optiuni:
# Adunare / # Scadere / # Inmultire / # Impartire / # Iesire din program
# Utilizatorul trebuie sa introduca optiunea, iar apoi:
# Pentru optiunile 1->4, utilizatorul trebuie sa introduca doua numere, iar programul va afisa rezultatul operatiei.
# In cazul in care introduce 5, atunci iesim din program. 
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

# 35. Sa se afiseze toate puterile lui 2 aflate intre un interval dat de utilizator.
# Exemplu: 10, 50 -> 16, 32

# lim_min = int(input("Introdu limita inferioara: "))
# lim_max = int(input("Introdu limita superioara: "))
# val = 2
# for i in range(1, int(lim_max/2) + 1):
#     val = 2 ** i
#     if lim_min < val & val <lim_max :
#         print(val)

# 36. Creează o listă cu 7 numere întregi, apoi afișează suma și media elementelor fara a utiliza functiile sum() si avg().
# Exemplu: [1,2,3,4,5,6,7] -> suma=28, media=4.0

# lista = [1,2,3,4,5,6,7]
# sum = 0
# for i in lista:
#     sum += i
# print("Suma elementelor este: ", sum)
# print("Media elementelor este: ", sum/len(lista))

# 37. Primește o listă de la tastatură (elemente separate prin spațiu) și afișează lista inversată.
# Exemplu: input: 1 2 3 4 5 -> output: [5,4,3,2,1]

# lista = input("Introdu o lista de elemente separate prin spatiu: ").split()
# lista_inversata = lista[::-1]
# print("Lista inversată este:", lista_inversata)

# sau

# lista = input("Introdu o lista de elemente separate prin spatiu: ").split()
# lista_inversata = list(reversed(lista))
# print("Lista inversată este:", lista_inversata)

# 38. Afișează toate elementele de pe poziții impare dintr-o listă dată.
# Exemplu: [10,20,30,40,50,60] -> 20,40,60

# lista = [10,20,30,40,50,60]
# for i in range(1, len(lista), 2):
#     print(lista[i])

# 39. Înlocuiește toate aparițiile unui element dat cu altă valoare într-o listă.
# Exemplu: [1,2,3,2,4], inlocuieste 2 cu 5 -> [1,5,3,5,4]

# lista = [1,2,3,2,4]
# for i in range(len(lista)):
#     if lista[i] == 2:
#         lista[i] = 5
# print(lista)

# 40. Afișează elementul maxim și minim dintr-o listă fără a folosi funcțiile max/min.
# Exemplu: [3,1,4,1,5,9,2] -> max=9, min=1

# lista = [3,1,4,1,5,9,2]
# maxim = lista[0]
# minim = lista[0]
# for i in lista:
#     if i > maxim:
#         maxim = i
#     if i < minim:
#         minim = i
# print("Maximul este: ", maxim)
# print("Minimul este: ", minim)

# 41. Elimină toate elementele pare dintr-o listă de numere.
# Exemplu: [1,2,3,4,5,6] -> [1,3,5]

# lista = [1,2,3,4,5,6]
# for i in lista :
#     if i % 2 == 0 :
#         lista.remove(i)
# print(lista)

# 42. Primește o listă de stringuri și construiește o nouă listă cu stringurile care conțin litera 'a'.
# Exemplu: ['ana', 'mere', 'casa', 'masina'] -> ['ana', 'casa', 'masina']

# lista = ['ana', 'mere', 'casa', 'masina']
# lista_noua = []
# for i in lista :
#     for x in i :
#         if x == 'a' :
#             lista_noua.append(i)
#             break
# print("Lista ce contine cuvinte cu litera 'a' este: ",lista_noua)

# 43. Verifică dacă o listă este palindrom (se citește la fel de la stânga la dreapta și invers).
# # Exemplu: [1,2,3,2,1] -> True, [1,2,3,4] -> False

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

# 44. Interclasează două liste de aceeași lungime într-o singură listă.
# # Exemplu: [1,2], [3,4] => [1,3,2,4]

# lista1 = [1,2]
# print(lista1)
# lista2 = [3,4]
# print(lista2)
# lista1.extend(lista2)
# print(lista1)

# 45. Creează o listă de liste [index, valoare] pentru fiecare element dintr-o listă dată.
# # Exemplu: [10,20,30] -> [[0,10],[1,20],[2,30]]

# lista = [10,20,30]
# lista2 = []
# for i in range(len(lista)) :
#     lista2.append([i, lista[i]])
# print(lista2)

# 46. Primește o listă de numere și elimină toate elementele care apar de mai mult de o dată (păstrează doar elementele unice).
# Fara a folosi set().
# # Exemplu: [1,2,2,3,4,4,5] -> [1,3,5]

# lista = [1,2,2,3,4,4,5]
# lista_unica = []
# for item in lista:
#     if lista.count(item) == 1:
#         lista_unica.append(item)
# print(lista_unica)

# 47. Primește o listă de numere și grupează elementele în două liste: una cu numere negative, alta cu numere pozitive și zero.
# # Exemplu: [10,-1,2,-3,0,4,-5] -> negative: [-1,-3,-5], pozitive_si_zero: [10,2,0,4]

# lista = [10,-1,2,-3,0,4,-5]
# negative = []
# restul = []
# for i in lista :
#     if i < 0 :
#         negative.append(i)
#     else :
#         restul.append(i)
# print("Numerele negative : ",negative)
# print("Pozitive si zero : ",restul)

# 48. Primește o listă de stringuri și sorteaz-o crescător după numărul de vocale din fiecare string.
# Fara a folosi functia sort() sau sorted().
# # Exemplu: ['ana', 'mere', 'casa', 'masina'] -> ['ana', 'casa', 'mere', 'masina']

# lista  = ['ana', 'masina', 'casa', 'mere']
# vocale = 'aeiou'
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
#             lista[i], lista[j] = lista[j], lista[i]
# print(lista)   

# 49. Primește o listă de liste (matrice) și calculează suma elementelor de pe diagonala principală (doar dacă matricea este pătratică).
# # Exemplu: [[1,2,3],[4,5,6],[7,8,9]] -> 15 (1+5+9)

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

# 17) Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel], [10.2, 7.5, 3.4]]. Sa se extraga numele "Ionut" si sa se afiseze.

# 18) Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel], [10.2, 7.5, 3.4]]. Sa se extraga litera "r" din numele "Marcel" si sa se afiseze.

# 19) Sa se numere de cate ori apare un element intr-o lista incluzand si listele imbricate.
# # Exemplu: [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]] si elementul 1 -> apare de 4 ori

# 20) Scrieti un program care sa genereze un numar aleator intre 1 si 100. Utilizatorul trebuie sa
# ghiceasca numarul, iar programul sa ii ofere indicatii daca numarul introdus este mai mare sau mai mic decat cel generat.
# Programul se termina cand utilizatorul ghiceste numarul corect sau daca introduce cuvantul exit. La final se afiseaza numarul de incercari facute.

# Pentru generarea numarului aleator:
# import random
# numar_aleator = random.randint(1, 100)

# 21) Sa se scrie un program primeste date in urmatorul format: "Nume: Ionescu Prenume: Ion" pana cand se introduce
# caracterul #. Programul trebuie sa stocheze toate datele citite, iar la final sa le afiseze in ordine alfabetica
# in functie de numele de familie.
#
