'''# Logging, assertions si tracebacks ----------------------------------------------------'''

# import logging
# name = 'Ionut'

# scriere in fisier
# logging.basicConfig(filename = 'app.log',level = logging.DEBUG, format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')
# sau
# scriere in consola 
# logging.basicConfig(level = logging.DEBUG, format='%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

# Selectarea nivelului permite afisare mesajelor de logging >= decat acel nivel
# logging.debug(f"Acesta este un mesaj de debug generat de {name}")
# logging.info("Acesta este un mesaj de info")
# logging.critical("Acesta este un mesaj de critical")
# logging.warning("Acesta este un mesaj de warning")
# logging.error("Acesta este un mesaj de error")

# se citesc 2 nr si se calc suma lor
# prog ruleaza pana la introducerea : x 

# import logging
# logging.basicConfig(level = logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# def aduna (nr1, nr2):
#     try :
#         suma = int(nr1) + int(nr2)
#     except ValueError:
#         logging.error("unul dintre nr nu este int")
#     else : 
#         return suma
# logging.info("App started")
# while True :
#     nr1 = input("val nr 1 : ")
#     nr2 = input("val nr 2 : ")
#     logging.debug(f'nr introduse sunt : {nr1} si {nr2}')
#     if nr1 == 'x' or nr2 == 'x':
#         break
#     print(aduna(nr1,nr2))
# logging.info("App closed")

# Se da lista [10,-5,5,12,20,30,-6], vreau sa verific cand apare la citire o valoare negativa

# import logging
# logging.basicConfig(filename = 'app.log', level = logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# def data_process(lista):
#     logging.info("Incepere procesare")
#     for index,value in enumerate(lista) : 
#         if value < 0 :
#             logging.warning(f'Valoare negativa : {value} la pozitia {index}')
#         else : 
#             logging.debug(f'Valoare citita : {value} la pozitia {index}')
#             processing_result = value / 2
#             print(f'Processed result : {processing_result}')
#             logging.debug(f'Processed result : {processing_result}')
#     logging.info("Procesare finalizata")

# date = [10,-5,5,12,20,30,-6]
# data_process(date)

'''# Assertions ------------------------------------------------------'''

# import math
# def calcul_logaritm (x):
#     assert x > 0, f'numarul introdus trebuie sa fie pozitiv ( val intordusa : {x})'
#     logaritm = math.log(x)
#     return logaritm

# print(calcul_logaritm(10))
# print(calcul_logaritm(-3))

'''# Trace back ------------------------------------------------------'''

# import traceback
# while True :
#     var = input('Introdu numar : ')
#     if var == 'x' :
#         break
#     try :
#         print(10/int(var))
#     except Exception as exceptie:
#         print('A aparut o eroare la impartie ')
#         traceback.print_exc()
#         print(f'Eceptia aparuta este : {exceptie}')

# import traceback
# def functie_a(x):
#     return functie_b(x)
# def functie_b(y):
#     return functie_c(y)
# def functie_c(z):
#     return 10/z
# while True :
#     var = input('Introdu numar')
#     if var == "x":
#         break
#     try :
#         rezultat = functie_a(int(var))
#     except Exception as exceptie:
#         print('A aparut o eroare la apelarea functie_a ')
#         traceback.print_exc()
#         print(f'Eceptia aparuta este : {exceptie}')
#     print(rezultat)