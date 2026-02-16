# Parcurgere structurata de fisiere si foldere

# import os 
# print(os.listdir("/Users/paul/Documents/GitHub/curs-python/")) # ---> ['.DS_Store', 'temp_file.txt', '__pycache__', 'curs-testing.py', 'exercitii.py', 'base-knowledge.py', 'fisier-testing.txt', '.git']
# my_path = os.path.join("/Users/paul/Documents/GitHub/curs-python/ceva")
# print(my_path)
# print(os.path.isdir(my_path))
# print(os.path.isfile(my_path))

# o sa verificam daca in folder-testing -> curs-python exista fisier-folder-testing.txt
# import os
# continut_proiect = os.listdir("/Users/paul/Documents/GitHub/curs-python/")
# print(continut_proiect)
# continut_proiect = os.path.join("/Users/paul/Documents/GitHub/curs-python/","folder-testing")
# print(continut_proiect)
# continut_data = os.listdir(continut_proiect)
# if "fisier-folder-testing.txt" in continut_data:
#     print("ok")
# else:
#     print("inexistent")

# o sa verificam daca in folder-testing din curs-python exista un fisier cu extensia .txt si il afisam continutul fisier-folder-testing.txt

import os
path_proiect = "/Users/paul/Documents/GitHub/curs-python/"
for elem in os.listdir(path_proiect):
    if elem.endswith(".txt") :
        with open(elem, 'r') as my_file: 
            print(elem)           
            print()
            print(my_file.read())     

# Error handling cu try, except, else si finally

# try:
#     with open("fisier-ce-nu-exista.txt", "r") as my_file:
#         print(my_file.read())
# except Exception as my_exception : 
#     print("Fisierul nu exista") # desi fisierul nu exista, se merge mai departe si se printeaza eroarea
#     print(my_exception)
# else :
#     print("fisierul deschis cu succes") # se printeaza acest mesaj si continutul fisierului  "fisier-ce-nu-exista.txt" daca ar exista
# finally :
#     print("aici se pune codul ce se va executa tot timpul")

# while True:
#     try:
#         numar = int(input("introdu un nurmar : "))
#     except Exception as ex:
#         print(ex)
#     else : 
#         print("ai introdus numarul : ", numar)
#         if numar == 0 :
#             break



