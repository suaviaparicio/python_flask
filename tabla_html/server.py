from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template("index.html")


@app.route('/lista')
def render_lists():
    users_info = [
        {'nombre' : 'Michael', 'apellido' : 'Choi'},
        {'nombre' : 'John', 'apellido' : 'Supsupin'},
        {'nombre' : 'Mark', 'apellido' : 'Guillen'},
        {'nombre' : 'KB', 'apellido' : 'Tonel'}
    ]

    return render_template("lista.html", users=users_info)


if __name__ == "__main__":
    app.run(debug=True)
