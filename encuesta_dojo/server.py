from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'shhhh'


@app.route('/')
def index():
    return render_template('formulario_dojo.html')


@app.route("/process", methods = ['POST'])
def data():
    session['usuario'] = {
    'name': request.form['name'],
    'location': request.form['location'],
    'language': request.form['language'],
    'comments': request.form['comments']
}
    print(session['usuario'])
    
    return redirect("/result")


@app.route("/result")
def result():
        return render_template('informacion_dojo.html')



if __name__ == "__main__":
    app.run(debug=True, port=8000)
