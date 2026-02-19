'''
2. Sa se creeze un pachet numit "geometry" care sa contina doua module: "area" si "perimeter". 
Modulul "area" sa contina functii pentru calcularea ariei unui cerc, patrat si dreptunghi.
Modulul "perimeter" sa contina functii pentru calcularea perimetrului acelorasi forme geometrice.
Din fisierul principal, sa se importe pachetul si sa se execute fiecare functie cu valori generate aleatoriu.
'''
from math import pi

def aria_cerc (raza):
    aria = round(pi,4) * (raza ** 2)
    return aria

def aria_patrat (latura):
    aria = latura ** 2
    return aria

def aria_dreptunghi (latura_mica, latura_mare):
    aria = latura_mica * latura_mare
    return aria
