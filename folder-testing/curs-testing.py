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
        return(redirect(url_for('home')))
    return (render_template("index_form.html"))

if __name__ == '__main__':
    app.run(debug=True) # ruleaza aplictia in modulul debug si salveaza automat modificarile de cod si le afiseaza







