'''# ----------------------- Web app Flask, Jinja2, SQLAlchemy --------------------------------'''

from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__) # intitializeaza aplicatia

@app.route('/') # cand cineva acceseaza rout-ul se va executa functia
def home2():
    return '''<h1>Hello, Flask!</h1>
    <h2>Aici h2</h2>
    '''

@app.route('/hello') # http://127.0.0.1:5000/hello
def hello():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template('index_header_body.html')

@app.route('/form', methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        prenume = request.form.get('prenume','')
        nume = request.form.get('nume','')
        varsta = request.form.get('varsta','')
        print(f'Prenume : {prenume}, Nume : {nume} si  varsta : {varsta}')
        return(redirect(url_for('form')))
    return (render_template("index_form.html"))

@app.route('/form/return_home', methods = ['GET', 'POST'])
def form_return_home():
    if request.method == 'POST':
        prenume = request.form.get('prenume','')
        nume = request.form.get('nume','')
        varsta = request.form.get('varsta','')
        print(f'Prenume : {prenume}, Nume : {nume} si  varsta : {varsta}')
        return(redirect(url_for('welcome')))
    return (render_template("index_form_return_home.html"))

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

'''# Jinja --------------------------------- '''

@app.route('/hello/<name>')
def hello_name (name):
    return render_template('index_name.html', name = 'Paul' )

@app.route('/hello/<name>/<age>') # /hello/Paul-Abesei/32
def hello_name_age(name,age):
    firstname = name.split('-')[0]
    lastname = name.split('-')[1]
    return render_template('index_name_age.html', firstname = firstname, lastname = lastname, age = age )

from flask import session
app.config['SECRET_KEY'] = 'dev-secret-key'

@app.route('/jinja_form', methods = ['GET', 'POST'])
def jinja_form():
    if request.method == 'POST':
        session['last_form_data'] = {
            'prenume' : request.form.get('prenume',''),
            'nume' : request.form.get('nume',''),
            'varsta' : request.form.get('varsta','')
                                        }
        return redirect(url_for('jinja_form'))
    
    submitted_data = session.pop('last_form_data', None)
    return render_template('jinja_form.html', submitted_data = submitted_data)


if __name__ == '__main__':
    app.run(debug=True) # ruleaza aplictia in modulul debug si salveaza automat modificarile de cod si le afiseaza

