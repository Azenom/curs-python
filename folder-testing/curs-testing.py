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

import json

persoane = {
    1234 : {
            'nume':'Popescu',
            'prenume':'Ion',
            'varsta':30,
            'masina':{
                'marca':'Dacia',
                'model':'Logan',
                'tip_combustibil':'benzina'
                    } 
            },
    5678 : {
            'nume':'Ionescu',
            'prenume':'Maria',
            'varsta':25,
            'masina':{
                'marca':'Ford',
                'model':'Focus',
                'tip_combustibil':'motorina'
                    }
            }
            }

with open('fisier_3.json', 'w') as my_file :
    json.dump(persoane, my_file, indent = 4)