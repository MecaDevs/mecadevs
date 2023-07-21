from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "jllor_2005"

@app.route('/')
def home_page():
    flash("What's your name?")
    return render_template("mecadevs_homepage.html")

@app.route('/greet', methods=['POST', 'GET'])
def greet():
    flash('Hello ' + str(request.form['name_input']) + ' prazer em conhecê-lo!')
    return render_template("mecadevs_homepage.html")

@app.route("/medic_dropper")
def medic_dropper_home_page():
    return render_template("medicdropper_homepage.html")

@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario) 

if __name__ == "__main__":
    app.run(debug=True)