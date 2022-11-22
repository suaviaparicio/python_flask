from flask import Flask, render_template  


app = Flask(__name__)



@app.route('/')
def home():
    return '<h2>Patio de Juegos</h2>'



# def cuadros():
#     return render_template ("index.html") 

@app.route('/play')
@app.route('/play/<int:num>')
@app.route('/play/<int:num>/<color>')
def play(num=3, color='RGB(158, 197, 248)'):
    return render_template ("index.html", num=num, color=color ) 




if __name__ == "__main__":   
    app.run(debug=True) 