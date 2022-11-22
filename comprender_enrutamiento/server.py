from flask import Flask  


app = Flask(__name__)



@app.route('/')
def hola_mundo():
    return '<h2>Hola Mundo!</h2>' 

@app.route('/dojo')
def dojo_1():
    return '¡Dojo!' 

@app.route('/hola/<string:name>')
def hola(name):
    print(name)
    return "¡Hola, " + name.capitalize() + "!" 

@app.route('/repeat/<int:numero>/<string:palabra>')
def repetido(numero, palabra):
    print(palabra)
    return palabra * numero 

@app.errorhandler(404)
def error(m):
    return '<h2>¡Lo siento! No hay respuesta. Inténtalo otra vez</h2>' 



if __name__ == "__main__":   
    app.run(debug=True) 