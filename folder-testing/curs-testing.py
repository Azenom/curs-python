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
        return round((self.rom + self.math + self.engl ) / 3 , 2)
    
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

def main():
    student_db = StudentRepo()
    school_service = SchoolService(student_db)

    while True :
        print("\nChoose an option : ")
        print('1. Add student')

        option = input("Option : ")

        if option == 1 : 
            fname = input("First name : ")
            lname = input("Laast name : ")
            rom = int(input("Rom : "))
            math = int(input("Math : "))
            engl = int(input("Engl : "))
            student = Student(fname, lname, rom, math, engl)
            school_service.add_student(student)

if __name__ =='__main__':
    main()

student1 = Student("Alex", "Miron", 10, 7,8)
student2 = Student("Maria", "Ionescu", 6,7,10)
student3 = Student("Paul", "Abesei", 9,9,6)
# student4 = Student("test", "test", 10,10,-1) # ValidationError: Error  - Grades must be between 1 and 10 
# print(student4)
# print([student1, student2, student3])
# print(student1.to_dict())

# my_students = [student1, student2, student3]
# my_database = StudentRepo()
# # my_database.save(my_students)

# my_students = my_database.load()
# print(my_students)