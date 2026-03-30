'''# Baze de date -------------------------------------------'''

# import sqlite3
# connection = sqlite3.connect('students.db')
# cursor = connection.cursor()

# cursor.execute('''
#     CREATE TABLE students (
#         id INTEGER PRIMARY KEY,
#         first_name TEXT,
#         last_name TEXT,
#         math_grade REAL,
#         engl_grade REAL,
#         cs_grade REAL
#                         )
#                ''')
# connection.commit()
# connection.close()

''' Insert data into DB'''

# pentu transmiterea unei date o singura data
# cursor.execute('''
#     INSERT INTO students (first_name, last_name, math_grade, engl_grade, cs_grade)
#     VALUES (?,?,?,?,?)
#             ''', ('Alice', 'Smith', 85.5, 90, 92.5))
    # se foloseste ? ca sa nu se faca sql injection si se transmit valorile pe baza de tuples mai jos
# connection.commit()
# connection.close()

# pentru transmiterea unor date multimple
# students_list = [
#     ("Luca", "Bianchi", 90, 85, 88),
#     ("Sara", "Rossi", 75, 80, 82),
#     ("Marco", "Verdi", 60, 65, 70)
# ]
# cursor.executemany('''
#     INSERT INTO students (first_name, last_name, math_grade, engl_grade, cs_grade)
#     VALUES (?,?,?,?,?)
#             ''', students_list)
# connection.commit()
# connection.close()

# sau 

# for student in students_list :
#     cursor.execute('''
#     INSERT INTO students (first_name, last_name, math_grade, engl_grade, cs_grade)
#     VALUES (?,?,?,?,?)
#             ''', student)
#     connection.commit()
# connection.close()

'''Afisare pe liniii din DB'''

# cursor.execute('''SELECT * FROM students''')
# rows = cursor.fetchall()
# connection.close()
# print(rows)

'''Afisare selectiva din DB - fetchone() & fetchall()'''

# cursor.execute('''SELECT * FROM students WHERE first_name = ?''',('Alice',))
# rows = cursor.fetchone()
# connection.close()
# print(rows)

# cursor.execute('''SELECT math_grade, engl_grade, cs_grade FROM students WHERE first_name = ?''',('Alice',))
# rows = cursor.fetchall()
# connection.close()
# print(rows)

# cursor.execute('''SELECT first_name, last_name FROM students WHERE math_grade > ?''',(20,) )
# rows = cursor.fetchall()
# connection.close()
# print(rows)

'''Update data into DB'''

# cursor.execute('''
    # UPDATE students
    # SET math_grade = ?
    # WHERE first_name = ? AND last_name = ?
    #                ''', 
    # (99, "Alice", 'Smith') )
# connection.commit()
# cursor.execute('''SELECT math_grade FROM students WHERE first_name = ? AND last_name = ?''', ("Alice","Smith") )
# print(cursor.fetchone())
# connection.close()

'''Delete data from DB'''

# cursor.execute('''
#     DELETE FROM students
#     WHERE first_name = ? and last_name = ? ''' , 
#     ('Alice','Smith')
#                 )
# connection.commit()

# cursor.execute('''
#     SELECT * FROM students
#                '''
#             )
# rows = cursor.fetchall()
# connection.close()

'''Context manager pt a nu mai inchide si deschie conexiunea la fiecare operatiune'''

# with sqlite3.connect('students.db') as conn :
#     cursor = conn.cursor()
#     cursor.execute('''
#         INSERT INTO students (first_name, last_name, math_grade)
#         VALUES (?,?,?)
#                     ''',
#         ('Alice','Smith',123)
#                 )
#     conn.commit()

# with sqlite3.connect('students.db') as conn :
#     cursor = conn.cursor()
#     cursor.execute('''
#         UPDATE students
#         SET engl_grade = ?, cs_grade = ?
#         WHERE first_name = ? AND last_name = ?
#                     ''',
#         (70,50,'Alice','Smith')
#                     )
#     conn.commit()

# with sqlite3.connect('students.db') as conn :
#     cursor = conn.cursor()
#     ids = [ (6,), (7,) ]
#     cursor.executemany('''
#         DELETE FROM students WHERE id = ? 
#                         ''' , 
#         ids
#                         )
#     conn.commit()

# '''Query all data from DB'''
# SELECT * FROM students;

# '''Query specific colums'''
# SELECT first_name, math_grade FROM students;

# '''Query all data with condition'''
# SELECT * FROM students
# WHERE math_grade >90;

# '''Query all data with order'''
# SELECT * FROM students
# ORDER BY math_grade DESC;