'''# Object Oriented Programming (OOP) -------------------------------------------------'''
# Definire 

# class NumeClasa :
#     pass
#     '''instructiuni identate ca la functii'''
# obiect = NumeClasa()
# print(type(obiect))
# print(obiect)

# Constructor __init__ si self ca si identificator ce nu este pus la socoteala cand sunt populate valorile : nume, prenume, cnp

# class Persoana :
#     def __init__(self, nume, prenume, cnp):
#         self.nume = nume
#         self.prenume = prenume
#         self.cnp = cnp

# persoana1 = Persoana("Abesei", "Paul", "1234345")
# persoana2 = Persoana("Neamtiu", "Daniel", "789687")

# print(persoana1.nume) # ------> Abesei
# print(persoana2.cnp) # ------> 789687

# print(persoana2.nume) # -------> Neamtiu
# persoana2.nume = 'Ionescu'
# print(persoana2.nume) # --------> a schimbat in Ionescu

# print(persoana1.__dict__) # -----> {'nume': 'Abesei', 'prenume': 'Paul', 'cnp': '1234345'}

# class Masina:
#     def __init__(self, model):
#         self.model = model
#         print("A pornit")
#     def porneste(self):
#         print(f"a pornit {self.model}")

# masina = Masina("BMW")
# masina2 = Masina("Audi")
# masina3 = Masina("toyota")
# masina.porneste()
# masina2.porneste()
# masina3.porneste()

# class Elev :
#     def __init__(self, nume, prenume, nota_romana, nota_mate, nota_engleza):

#         self.nume = nume
#         self.prenume = prenume
#         self.nota_romana = nota_romana
#         self.nota_mate = nota_mate
#         self.nota_engleza = nota_engleza

#     def prezentare(self):
#         print(f'Salut, ma numesc {self.nume} {self.prenume}')

#     def note(self):
#         print(f'Notele mele sunt romana : {self.nota_romana} mate : {self.nota_mate} engleza : {self.nota_engleza}')

#     def prezinta_medie(self):
#         medie = (self.nota_romana + self.nota_mate + self.nota_engleza )/3
#         return f"Media este : {medie}"
        
# elev1 = Elev("Ionescu",'Marius',8,9,10)
# elev2 = Elev('Popescu','Marinel',5,5,5)
# elev3 = Elev('Neamtiu','Ioana', 7,8,8)

# elev1.prezentare()
# elev2.note()
# print(elev3.prezinta_medie())

# Sa se citeasca de la tastatura elevi pana se introduce caracterul x
# Pt fiecare elev trb sa il punem sa se prezinte, sa isi zica notele si media lor

class Elev: 
    def __init__(self, nume, prenume, nota_romana, nota_mate, nota_engleza):
        self.nume = nume
        self.prenume = prenume
        self.nota_romana = nota_romana 
        self.nota_mate = nota_mate
        self.nota_engleza = nota_engleza
        self.media = self.calcul_medie()

    def prezinta_te(self):
        print(f"Salut! Numele meu este {self.nume} {self.prenume}")

    def spune_notele(self):
        print(f"Notele mele sunt: roman: {self.nota_romana}, mate: {self.nota_mate}, engleza: {self.nota_engleza}")

    def spune_media(self):
        self.media = (self.nota_romana + self.nota_mate + self.nota_engleza) / 3
        print(f"Media mea generala este {self.media:.2f}")
    def calcul_medie(self):
        return (self.nota_romana + self.nota_mate + self.nota_engleza) / 3
    
elev1 = Elev("Ionescu", "Andrei", 8, 10, 9)

elev1.prezinta_te()
elev1.spune_notele()
print(elev1.media)
elev1.spune_media()
print(elev1.media)

# Creati o clasa numita "Rectangle" care are atributele "length" si "width".
# Adauga o metoda numita "area" care returneaza aria dreptunghiului, si o metoda numita
# "perimeter" care returneaza perimetrul dreptunghiului.
# Instantiaza un obiect al clasei Rectangle si afiseaza aria si perimetrul acestuia.

# class Rectangle :
#     def __init__ (self, length, width):
#         self.length = length
#         self.width = width
#     def area (self):
#         return self.length * self.width
#     def perimeter (self):
#         return 2*(self.length + self.width)

# deptunghi = Rectangle(10,8)
# print('Aria dreptunghi',deptunghi.area())
# print("Perimetru dreptunghi",deptunghi.perimeter())