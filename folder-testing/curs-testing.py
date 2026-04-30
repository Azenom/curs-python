'''# SQLAlchemy --------------------------------- '''

from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # initializeaza aplicatia de Flask
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db" # path catre baza de date
db = SQLAlchemy(app) # leaga baza de date cu aplicatie de Flask

class Student(db.Model):
    cnp = db.Column(db.String(13), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    grade = db.Column(db.Float, nullable=False)

@app.route('/')
def home():
    students = db.session.query(Student).all()
    return render_template('home_sql_alchemy.html', students=students)

@app.route('/add', methods = ['GET','POST'])
def add():
    if request.method == "POST":
        cnp = request.form.get('cnp')
        name = request.form.get('name')
        grade = request.form.get('grade')
        new_student = Student(cnp = cnp, name = name, grade = grade)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('add_sql_alchemy.html')

@app.route('/update', methods = ['GET','POST'])
def update():
    if request.method == "POST":
        cnp = request.form.get('cnp')
        grade = request.form.get('grade')
        student = db.session.query(Student).get(cnp)
        student.grade = grade
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('update_sql_alchemy.html')

@app.route('/delete', methods = ['GET','POST'])
def delete():
    if request.method == "POST":
        cnp = request.form.get('cnp')
        student = db.session.query(Student).get(cnp)
        db.session.delete(student)
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('delete_sql_alchemy.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
# ruleaza aplictia in modulul debug si salveaza automat modificarile de cod si le afiseaza
    app.run(debug=True)