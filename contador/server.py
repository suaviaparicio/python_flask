from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'shhhh'


@app.route('/')
def client_count():
    if session.get('num') is None:
        session['num'] = 0
    session['num'] += 1

    return render_template('contador.html')
    

@app.route('/destroy_session')
def clear ():
    session.clear()
    return redirect('/')

    
@app.route('/sumar2')
def sumar_dos ():
    session['num'] += 1
    return redirect('/')


@app.route('/numero_usuario', methods=['POST'])
def numero_usuario ():
    numero = request.form['sumarx']             # ------> Lo recupero deel formulario
    print(f"Elegiste el número " + numero)
    numero = int(numero)                        # ------> Lo estamos transformando en número, porque todo lo que llega, llega en tipo texto
    
    session['num'] += numero

    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True, port=8000)
