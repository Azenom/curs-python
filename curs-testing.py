# Functie recursiva atentie la oprire pentru a evita : # eroare de stack overflow

lista = [1,2,3, [1,3,5], 6, [1, [1,2,3,1], 6,7],8]

lista_simpla = [1,2,3,4,5,6,6,7,8,8,1]

def frecv_nr (lista_in_care_caut, nr_cautat) :
    counter = 0
    for nr in lista_in_care_caut :
        if type(nr) == list : 
            counter += frecv_nr(nr , nr_cautat)
        elif nr == nr_cautat :
            counter += 1
    return counter

print(frecv_nr(lista,1))
            

