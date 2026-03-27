'''Exercitii OOP in Python:'''
'''# 149. Sa se creeze un porg care :
a) Creeaza o clasa numita "Persoana" care are atributele "nume", "varsta" si "gen".
b) Creeaza o lista de 5 persoane si afiseaza numele si varsta fiecarei persoane din lista.
c) Adauga o metoda numita "introducere" in clasa "Persoana" care returneaza o introducere a persoanei 
   (ex: "Numele meu este X, am Y ani si sunt de gen Z"). Apeleaza aceasta metoda pentru fiecare persoana din lista.
d) Creeaza o metoda numita "este_major" care returneaza True daca persoana are varsta de 18 ani sau mai mult, si False in caz contrar. 
Apeleaza aceasta metoda pentru fiecare persoana din lista si afiseaza daca fiecare persoana este major sau nu.
e) Creeaza o metoda numita "schimba_gen" care schimba genul persoanei (ex: daca genul este "masculin", il schimba in "feminin" si invers). 
Apeleaza aceasta metoda pentru fiecare persoana din lista si afiseaza noul gen al fiecarei persoane.
f) Creeaza o metoda numita "adauga_ani" care adauga un numar specificat de ani la varsta persoanei. 
Apeleaza aceasta metoda pentru fiecare persoana din lista, adaugand un numar aleator de ani si afiseaza noua varsta a fiecarei persoane.
g) Afiseaza o lista cu toate persoanele care sunt majore.
h) Afiseaza o lista cu toate persoanele care au genul "masculin" si au peste 14 ani. ''' 

# class Persoana :
#    def __init__ (self, nume, varsta, gen):
#       self.nume = nume
#       self.varsta = varsta
#       self.gen = gen
#    def introducere(self):
#       print(f"Numele meu este {self.nume}, am {self.varsta} ani si sunt de gen {self.gen}")
#    def este_major (self):
#       if self.varsta >= 18 :
#          return True
#       else : return False
#    def schimba_gen(self): 
#       if self.gen == 'm':
#          self.gen = 'f'
#       else : self.gen = 'm'

# persoane = [Persoana('Andrei', 20, "M"), Persoana('Alexandra', 32, "F"), Persoana('Maria', 25, 'F'), Persoana('Daniel', 31, "M")]

# while len(persoane) < 5 :
#    nume = input("introdu nume : ")
#    varsta = int(input("introdu varsta : "))
#    gen = input("introdu gen : ")
#    persoana = Persoana(nume,varsta,gen)
#    persoane.append(persoane)

# for persoana in persoane:
   # print(f'Persoana {persoana.nume} are varsta {persoana.varsta}')
   # sau
   # persoana.introducere()
   # print(f'{persoana.nume} --- {persoana.este_major()}')
   # persoana.schimba_gen()

