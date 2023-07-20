from flask import Flask, render_template

MecaDevs = Flask(__name__)

@MecaDevs.route('/')
def home_page():
    return render_template("mecadevs_homepage.html")

@MecaDevs.route('/medic_dropper')
def medic_dropper_home_page():
    return render_template("medicdropper_homepage.html")

@MecaDevs.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario) 

if __name__ == "__main__":
    MecaDevs.run(debug=True)