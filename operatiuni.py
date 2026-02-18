'''
1. Sa se creeze un modul numit "operations" care sa contina functii pentru adunare, scadere, inmultire si impartire a doua numere.
   Din fisierul principal, sa se importe modulul si sa se execute fiecare operatie cu doua numere generate aleatoriu.
'''

def adunare (param1,param2):
    suma = param1 + param2
    return suma

def scadere (param1,param2):
    diferenta = param1-param2
    return diferenta

def inmultire (param1,param2):
    produs = param1*param2
    return produs

def impartire (param1,param2):
    catul = param1/param2
    return catul