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