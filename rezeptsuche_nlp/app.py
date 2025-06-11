from flask import Flask, request, render_template
from nlp import extrahiere_zutaten
from models import rezepte_suchen

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["anfrage"]
        zutaten = extrahiere_zutaten(text)
        rezepte = rezepte_suchen(zutaten)
        return render_template("ergebnisse.html", rezepte=rezepte)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
