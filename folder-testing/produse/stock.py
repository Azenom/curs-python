'''# 134. Se da urmatorul fisier "produse.txt" care contine informatii despre produse.
   Sa se scrie un program care citeste informatiile despre produse din fisierul "produse.txt"
   si calculeaza pretul total al stocului pentru fiecare produs.'''

# import json

# def nume_produs(text):
#    return text.split("-", 1)[0].rstrip()

# with open("produse.txt", 'r') as my_file :
#    linii_fisier = my_file.readlines()

# produs = {}

# for linii in linii_fisier:
#    date = linii.split()
#    nume = nume_produs(linii)
#    pret_total = int( date[-5] ) * int( date[-2] )
#    produs.update({nume : pret_total})

# print(json.dumps(produs, indent=4))

# sau

# produse = []
# lista_p = []
# cantitate = []
# with open("produse.txt", "r") as my_file:
#    linii_fisier = my_file.readlines()

# for linie in linii_fisier:
#    produs = linie.strip().split("-")
#    produse.append(produs)
#    lista_p.append(int(produs[1].split()[0]))
#    cantitate.append(int(produs[2].split()[0]))

# for i in range(len(produse)):
#    nume_produs = produse[i][0]
#    total = lista_p[i] * cantitate[i]
#    print(f"{nume_produs} - {total} lei")
# SAU
# for i, produs_info in enumerate(produse):
#    nume_produs = produs_info[0]
#    total = lista_p[i] * cantitate[i]
#    print(f"{nume_produs} - {total} lei")