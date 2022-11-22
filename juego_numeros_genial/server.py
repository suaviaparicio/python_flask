import random 
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'keep it secret, keep it safe'

@app.route('/clear')
def clear ():
    session.clear()
    return redirect('/')

@app.route('/')
def index():
    if session.get('num') in None:
        numero = random.randint(1, 100)
        print(f"Elegiste el número {numero}")
        session['num'] = numero

    return render_template("juego.html")

@app.route('/adivinar', methods=['POST'])
def adivinar():
    intento = request.form['intento'] # ------> Lo recupero deel formulario
    print(f"Elegiste el número " + intento)
    intento = int(intento) # ------> Lo estamos transformando en número, porque todo lo que llega, llega en tipo texto

    if session.get('intentos') is None:
        session['intentos'] = 1
    else:
        session['intentos'] += 1 

    if session['num'] > intento:     # ------> Lo comparo con lo que tengo en sesión
        session['clase'] = 'red'
    elif session['num'] < intento:
        session['clase'] = 'orange'
    else:
        session['clase'] = 'green'


    return redirect ('/')  # ------> Redirige a la ruta base


if __name__ == "__main__":
    app.run(debug=True)
