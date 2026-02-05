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