'''
Sa se scrie un program care tine evidenta elevilor dintr-o scoala.
Programul trebuie sa dispuna de un meniu care ne pune la dispozitie urmatoarele optiuni:

- Adaugare elev
- Afisarea elevilor existenti
- Modificare informatii elev existent
- Stergere elev
- Cautare elev dupa nume si prenume
- Afisare elevi in ordinea mediei
- Afisare elevi cu media peste 8
- Afisare elevi cu media sub 5
- Iesire din program

Pentru fiecare elev trebuie sa retinem urmatoarele informatii:
- Nume
- Prenume
- Nota romana
- Nota matematica
- Nota engleza
- Media (sa se calculeze automat pe baza notelor introduse)

Implementarea programului trebuie sa utilizeze conceptele de programare orientata pe obiect, cum ar fi
clase, obiecte, mostenire, polimorfism, incapsulare si abstractizare.
'''

import json

class ValidationError(Exception):
    pass

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class Student(Person):
    def __init__(self, fname, lname, rom, math, engl):
        super().__init__(fname, lname)
        self.__set_grades(rom, math, engl)

    def update_grades(self, rom, math, engl):
        self.__set_grades(rom, math, engl)

    def get_media(self):
        return round((self.__rom + self.__math + self.__engl ) / 3 , 2)
    
    def __set_grades (self, rom, math, engl):
        for grade in (rom, math,engl):
            if not (1 <= grade <= 10):
                raise ValidationError("Error  - Grades must be between 1 and 10 ")
        self.__rom = rom
        self.__math = math
        self.__engl = engl

    def to_dict(self):
        return {
            'firstname' : self.fname,
            'lastname' : self.lname,
            'rom' : self.__rom,
            'math' : self.__math,
            'engl' : self.__engl
            }

    def __str__ (self):
        return f'{self.fname} {self.lname} - media {self.get_media()}'
    def __repr__(self):
        return f'[Firstname : {self.fname}, Lastname : {self.lname}, Grades : rom : {self.__rom} / math : {self.__math} / engl : {self.__engl}]'
    
class StudentRepo : 
    def __init__(self, filename='students.json'):
        self._filename = filename
    
    def save(self, students):
        try : 
            with open(self._filename, 'w') as jsondb:
                json.dump([student.to_dict() for student in students], jsondb, indent=4) # scriem direct ca o lista de dictionare fara sa mai salvam datele intr=o lista
        except Exception as exception :
            print("Ops ! Something went wrong when writing to DB")
            print(exception)
    
    def load(self):
        try : 
            with open(self._filename, 'r') as jsondb:
                students_data = json.load(jsondb)
                students = []
                for entry in students_data:
                    student = Student(entry['firstname'], entry['lastname'], entry['rom'], entry['math'], entry['engl'])
                    students.append(student)
                return students
        except FileNotFoundError:
            print("DB not found")
        except Exception as exception:
            print("Ops ! Something went wrong when reading th DB")
            print(exception)

class SchoolService :
    def __init__ (self, student_db):
        self._student_db = student_db
        self._students = student_db.load()

    def add_student(self, student):
        if self.find_student(student.fname, student.lname):
            raise ValidationError("Student already exists ! ")
        self._students.append(student)
        self._student_db.save(self._students)

    def find_student(self, fname, lname):
        for student in self._students :
            if student.fname == fname and student.lname == lname :
                return student
        return None
    
    def modify (self, fname, lname):
        if self.find_student(fname, lname):
            old_fname = fname
            old_lname = lname
            fname = input('Enter new first name : ')
            lname = input('Enter new last name : ')
            rom = float(input('Enter new rom grade : '))
            math = float(input('Enter new math grade : '))
            engl = float(input('Enter new engl grade : '))
            student = Student(fname, lname, rom, math, engl)
            self.delete(old_fname, old_lname)
            print(f'Old student with : {old_fname} {old_lname} has been changed into : {fname} {lname}')
            self.add_student(student)
        else :
            print(f'Student {fname} {lname} not found')
    
    def delete (self, fname, lname):
        for entry in self._students:
            if fname == entry.fname and lname == entry.lname:
                self._students.remove(entry)
                self._student_db.save(self._students)
                break  # stop after removing, no need to carry on
    
    def sort_by_media(self):
        self._students.sort(key=lambda s: s.get_media(), reverse=True)
        for s in self._students:
            print(s)

    def show_students_by_media(self, condition):
        """
        Show students based on condition :
        - 'above_8' → media > 8
        - 'below_5' → media < 5
        """
        if condition == 'above_8':
            filtered = [s for s in self._students if s.get_media() > 8]
            message = "Students above 8: "
        elif condition == 'below_5':
            filtered = [s for s in self._students if s.get_media() < 5]
            message = "Students below 5: "
        else:
            print("Invalid condition ! ")
            return

        if not filtered:
            print("There are no students that fit the cryteria !")
            return

        print(message)
        for s in filtered:
            print(s)

def main():
    student_db = StudentRepo()
    school_service = SchoolService(student_db)

    while True :
        print("\nChoose an option : ")
        print('1. Add student')
        print('2. Show students')
        print("3. Modify student's data")
        print('4. Delete student completly')
        print('5. Search student')
        print('6. Sort by media')
        print('7. Show students with media > 8')
        print('---- Press 0 to exit !!! ----')

        option = input("Option : ")

        if option == '0' : # Iesire prog
            print("Prog terminated ! ")
            break

        if option == '1' : # Adaugare elev
            fname = input("First name : ")
            lname = input("Laast name : ")
            rom = int(input("Rom : "))
            math = int(input("Math : "))
            engl = int(input("Engl : "))
            student = Student(fname, lname, rom, math, engl)
            school_service.add_student(student)

        if option == '2' : # Afisare elevi
            print(student_db.load())

        if option == '3' : # Modificare elev
            print("Enter stundent's details ")
            fname = input("First name : ")
            lname = input("Last name : ")
            school_service.modify(fname,lname)
        
        if option == '4' : # Stergere elev
            print("Enter stundent's details to be removed")
            fname = input("First name : ")
            lname = input("Last name : ")
            school_service.delete(fname,lname)
            print(f'Student {fname} {lname} deleted !')

        if option == '5' : # Cautare elev
            print("Enter stundent's details ")
            fname = input("First name : ")
            lname = input("Last name : ")
            if school_service.find_student(fname,lname):
                print("Student gasit !!!")
                print(Student.__repr__(school_service.find_student(fname,lname)))

        if option == '6' : # Sortare dupa medie
            school_service.sort_by_media()
        
        if option == '7' : # Media peste 8
            school_service.show_students_by_media('above_8')

        if option == '8' : # Media sub 5
            school_service.show_students_by_media('below_5')

if __name__ =='__main__':
    main()
