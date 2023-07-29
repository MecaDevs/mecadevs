from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "jllor_2005"

@app.route('/')
def home_page():
    return render_template("mecadevs_homepage.html")

@app.route("/medic_dropper")    
def medic_dropper_home_page():
    return render_template("medicdropper_homepage.html")

@app.route("/parceiros")
def parceiros_home_page():
    return render_template("parceiros_home_page.html")

if __name__ == "__main__":
    app.run(debug=True)