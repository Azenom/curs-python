'''# Encapsulation si Abstration ---------------------------------'''
class Elev:
    def __init__ ( self, nume, prenume, mate, rom, engl):
        self.nume = nume # variabila publica
        self.prenume = prenume # variabila publica
        self._mate = mate # variabila protejata
        self._rom = rom # variabila protejata
        self._engl = engl # variabila protejata
        self.__media = self._update_media() # variabila privata

    def get_mate(self):
        return self._mate
    
    def set_mate(self, new_mate):
        if self._validare_nota(new_mate) :
            self._mate = new_mate
            self.__media = self._update_media()
        else : 
            print('Nota trebuie sa fie intre 1 si 10')

    def get_media(self):
        return self.__media
    
    def _update_media(self): # metoda interna protejata
        return self._mate + self._rom + self._engl / 3

    def _validare_nota (self, new_nota): # metoda interna protejata
        if 0 < new_nota <= 10 :
            return True
        else : return False
    
elev1 = Elev("Abesei",'Paul',8,9,10)
print (type(Elev))
print(elev1.get_media())
print(elev1.get_mate())