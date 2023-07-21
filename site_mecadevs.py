from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("mecadevs_homepage.html")

@app.route('/medic_dropper')
def medic_dropper_home_page():
    return render_template("medicdropper_homepage.html")

@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario) 

if __name__ == "__main__":
    app.run(debug=True)