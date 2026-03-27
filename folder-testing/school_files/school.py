'''# 147. Se da urmatoarea structura de directoare care contine informatii despre elevii dintr-o scoala:

school_files/high_school/classA - contine fisiere CSV cu informatii despre elevii de la filologie
school_files/high_school/classB - contine fisiere JSON cu informatii despre elevii de la mate-info 

Sa se scrie un program care parcurge recursiv structura de directoare "school_files" si:
Afiseaza toti elevii din clasele de Filologie (ClassA) care au nota peste 90 la Istorie
Afiseaza toti elevii din clasele de Mate-Info (ClassB) care au media mai mica deca 80,
Calculeaza media generala a tuturor claselor de Filologie,
Afiseaza clasele de Mate-info in ordine crescatoare a mediei generale pe clasa,
Afiseaza elevii cu cea mai mare medie din fiecare clasa,
Convertește fisierele csv in care sunt salvate informatiile despre elevii de la Filologie in fisiere json.
Convertește fisierele json in care sunt salvate informatiile despre elevii de la Mate-Info in fisiere csv. '''

# import csv, json, os

# class_A = '/Users/paul/Documents/GitHub/curs-python/folder-testing/school_files/high_school/classA'
# for file_name in os.listdir(class_A):
#    cale_fisier = os.path.join (class_A, file_name)
#    #print()
#    print(cale_fisier)
#    #print()
#    with open(cale_fisier, 'r', newline='') as my_file :
#       reader = csv.DictReader(my_file)
#       for row in reader:
#          #print(row)
#          if(int(row['History']) >= 90):
#             print('Elevii din classA care au nota la istorie peste 90 sunt : ', row['Name'])

# class_B = '/Users/paul/Documents/GitHub/curs-python/folder-testing/school_files/high_school/classB'
# for file_name in os.listdir(class_B):
#    cale_fisier = os.path.join (class_B, file_name)
#    with open(cale_fisier, 'r') as my_file :
#       date = json.load(my_file)
#       for elem in date : 
#          nota = elem['grades']
#          media = (nota['math']+nota['english']+nota['science'])/3
#          if media < 80 :
#             print('Elevii din classB care au media mai mica decat 80 sunt : ',elem['name'])
         
# for file_name in os.listdir(class_A):
#    cale_fisier = os.path.join (class_A, file_name)
#    print(cale_fisier)
#    lista_medii=[]
#    with open(cale_fisier, 'r', newline='') as my_file :   
#       reader = csv.DictReader(my_file)
#       for row in reader :
#          medie_elev = ( int(row['Geography']) + int(row['English']) + int(row['History'] )  ) / 3
#          lista_medii.append(medie_elev)
#       media_clasei = sum(lista_medii) / len(lista_medii)
#       print(f'Media {file_name} din classA este : {media_clasei}')