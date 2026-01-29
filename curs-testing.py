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


"""# Functii : def si return """

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


def functie_nou (param1, param2) :
    global var # fiind definita ca si global, variabila poate sa sufere modificari atat in functie cat si inafara ei
    var = param1 + param2
    print(var)

print(var)

functie_nou (100,200)
var = var + 10
print(var)







