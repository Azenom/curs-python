'''# Mostenire si polimorfism ----------------------------------------'''

class Persoana :
    def __init__(self, nume, prenume, varsta):
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta
    def prezentare (self):
        print(f'Numele meu este {self.nume} {self.prenume} si am {self.varsta} ani !')

persoana1 = Persoana('Abesei', 'Paul', 72)
persoana2 = Persoana('Popescu','Ana', 27)

persoana1.prezentare()
persoana2.prezentare()

# Elev - nume, prenume, varsta, nota_rom, nota_mate
class Elev(Persoana):
    def __init__ (self, nume, prenume, varsta, nota_rom, nota_mate):
        super().__init__(nume, prenume, varsta)
        self.nota_rom = nota_rom
        self.nota_mate = nota_mate

    def prezenare(self): # daca vreau sa suprascriu prezentarea din clasa Persoana
        super().prezentare()
        print(f'Am urmatoarele note: \n Romana : {self.nota_roama} \n Matematica : {self.nota_mate}')

    def afiseaza_note (self):
        print(f'Notele mele sunt : romana : {self.nota_rom} si mate : {self.nota_mate}')
    
    def media (self):
        return sum([self.nota_rom, self.nota_mate]) /2
    

elev1 = Elev('Neamtiu', 'Daniel', 27,10,10)
elev1.prezentare()
elev1.afiseaza_note()

lista_oameni = [persoana1, persoana2, elev1]

for om in lista_oameni :
    om.prezentare()