from flask import Flask, render_template  


app = Flask(__name__)


@app.route('/')
def home(altura=8, fila=8):
    return render_template ("index.html", altura=altura, fila=fila)  

@app.route('/4')
def tablero_4(altura=4, fila=8):
    return render_template ("index.html", altura=altura, fila=fila)

@app.route('/<int:altura>/<int:fila>')
def tablero_personal(altura, fila):
    print(f"altura:{altura},fila:{fila}")
    return render_template ("index.html", altura=altura, fila=fila) 

@app.route('/<int:altura>/<int:fila>/<color_blanco>/<color_negro>')
def tablero_personal_color(altura, fila, color_blanco="red", color_negro="black"):
    return render_template ("index.html", altura=altura, fila=fila, color_blanco=color_blanco, color_negro=color_negro) 

if __name__ == "__main__":   
    app.run(debug=True) 