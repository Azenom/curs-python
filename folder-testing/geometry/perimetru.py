'''
2. Sa se creeze un pachet numit "geometry" care sa contina doua module: "area" si "perimeter". 
Modulul "area" sa contina functii pentru calcularea ariei unui cerc, patrat si dreptunghi.
Modulul "perimeter" sa contina functii pentru calcularea perimetrului acelorasi forme geometrice.
Din fisierul principal, sa se importe pachetul si sa se execute fiecare functie cu valori generate aleatoriu.
'''

from math import pi

def perimetru_cerc (raza):
    perimetru = 2 * round(pi,4) * raza
    return perimetru

def perimetru_patrat (latura):
    perimetru = 4 * latura
    return perimetru

def perimetru_dreptunghi (latura_mica, latura_mare):
    perimetru = 2 * latura_mica + 2 * latura_mare
    return perimetru
