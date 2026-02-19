# Fisere JSON si CSV -----------------------

# fisierul json arata exact ca un dictionar din Python :

# import json
# persoane = {
#     1234 : {
#             'nume':'Popescu',
#             'prenume':'Ion',
#             'varsta':30,
#             'masina':{
#                 'marca':'Dacia',
#                 'model':'Logan',
#                 'tip_combustibil' : null # vine din java in loc de None din Python
#                     } 
#             },
#             }
# print(json.dumps(persoane, indent=4)) # -----> afiseaza dictionarul persoane frumos formatat

# import json
# with open ('fisier_1.json', 'r') as my_file:
#     date= json.load(my_file)
# print (json.dumps(date, indent = 4)) # type-ul este dic
# nume = date ['nume']
# varsta = date ['varsta']
# numar_copii = len(date ['copii'])
# print(f'{nume} are {varsta} ani si {numar_copii} copii')
# oras = date.get('adresa').get('oras')
# print (f'{nume} este din orasul {oras}' )

# import json
# persoane = {
#     1234 : {
#             'nume':'Popescu',
#             'prenume':'Ion',
#             'varsta':30,
#             'masina':{
#                 'marca':'Dacia',
#                 'model':'Logan',
#                 'tip_combustibil':'benzina'
#                     } 
#             },
#     5678 : {
#             'nume':'Ionescu',
#             'prenume':'Maria',
#             'varsta':25,
#             'masina':{
#                 'marca':'Ford',
#                 'model':'Focus',
#                 'tip_combustibil':'motorina'
#                     }
#             }
#             }
# with open('fisier_3.json', 'w') as my_file :
#     json.dump(persoane, my_file, indent = 4)

# import json
# with open('fisier_1.json', 'r') as my_file :
#     date = json.load(my_file)
# print(json.dumps(date, indent=4))
# date['copii'].append("Mihaela")
# date["telefon"] = '0723232323'
# print(json.dumps(date, indent=4))
# with open ('fisier_3.json', 'w') as my_file :
#     json.dump(date, my_file, indent = 4)

# import json
# import random
# with open ("fisier_2.json", 'r') as my_file:
#     data = json.load(my_file)

# for element in data :
#     element.update({'copii':random.randint(0,5)})

# with open ("fisier_2.json", 'w') as my_file:
#     print(json.dump(data, my_file, indent=4))


# Lucru cu CSV

# se face totul in fiserul deschis pt ca se citeste linie cu linie csv-ul in Python 
# import csv
# with open ( 'fisier1.csv' , 'r', newline='') as my_file:
#     reader = csv.reader(my_file)
#     my_csv_rows = []
#     for row in reader :
#         my_csv_rows.append(row)
# print(my_csv_rows)

# # sau ca sa pui toate liniile intr-o lista si sa nu mai tii fisierul deschis pe toata durata prelucrarii datelor

# import csv
# with open ( 'fisier1.csv' , 'r', newline='') as my_file:
#     reader = csv.reader(my_file)
#     my_csv_rows = list[reader]
# print(my_csv_rows)

# se srie linie cu linie folosind writerow()
# import csv
# with open ( 'fisier1.csv' , 'r', newline='') as my_file:
#     writer = csv.writer(my_file)
#     writer.writerow(["nume","varsta","oras"]) 
#     writer.writerow(["Ion Popescu",30,"Bucuresti"])

# daca vrei sa scrii mai multe date dintr-o data se foloseste writerows()
# import csv
# date_multiple = [
#     [[1,2,3,4],
#      [5,6,7,8],
#      [9,10,11,12]]
# ]
# with open ( 'fisier1.csv' , 'w', newline='') as my_file:
#     writer = csv.writer(my_file)
#     writer.writerow(["nume","varsta","oras"]) 
#     writer.writerows(date_multiple)

# citire fisier in format dictionar si pus intr-o lista ca sa nu tinem fisier :
# import csv
# with open ( 'fisier1.csv' , 'r', newline='') as my_file:
#     dic_read = csv.DictReader(my_file)
#     date = list(dic_read)
# print(date)

# pastrare antet folosind fieldnames apoi adaugare fara suprascriere folosind a in loc de w :
# import csv
# with open ( 'fisier1.csv' , 'a', newline='') as my_file:
#     antet = (["nume","varsta","oras"]) # exista ca si paramentru ce contine head-ul fisierului
#     dict_write = csv.DictWriter(my_file, fieldnames=antet)
#     dict_write.writerow({'nume':'paul', 'varsta':31, 'oras':'bucuresti'})
