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