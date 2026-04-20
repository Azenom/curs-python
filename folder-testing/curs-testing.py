''' #  --------------------------------------- API - REST API ----------------------------------------'''
''' Application Programming Interface ----------------------'''
''' Representational State Transfer Application Programming Interface ''' # pentru WEB cu protocol HTTP

# import requests
# url = 'https://restcountries.com/v3.1/name/romania'
# response = requests.get(url)

# print(response) # <Response [200]> -> a mers conexiunea cu raspuns 200
# json_response = response.json()
# print(json_response)

# print(json_response[0]['capital'][0])
# print(json_response[0]['region'])
# print(json_response[0]['population'])
# print(json_response[0]['currencies'])

''' # Flask API basic ---------------------'''

import sqlite3
from flask import Flask, jsonify, request

DB_NAME = 'students.db'
app = Flask(__name__)

def row_to_dict(row):
    return {
        'cnp' : row[0],
        'firstname' : row[1],
        'lastname' : row[2],
        'rom' : row[3],
        'math' : row[4],
        'engl' : row[5]
    }

@app.get('/') # porneste pagina de start
def home():
    return jsonify({'message': 'students API is running !'})

@app.get('/students') # mapeaza functia de mai jos in endpoint
def get_students():
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM students')
        rows = cursor.fetchall()

    students_list = []
    for row in rows:
        students_list.append(row_to_dict(row))

    return jsonify(students_list)

@app.get('/students/<int:student_cnp>')
def get_student(student_cnp):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM students WHERE cnp = ?', (student_cnp,))
        row = cursor.fetchone()

    if row is None :
        return jsonify({'error':f'Students with cnp : {student_cnp} Does not exit !'}), 404
    
    return jsonify(row_to_dict(row))

if __name__ == '__main__':
    app.run(debug=True) # tine aplicatia in viata pana cand o inchid

