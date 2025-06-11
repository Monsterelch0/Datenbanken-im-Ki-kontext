import joblib
import os

# Modell & Vektorizer laden
BASE = "model"
model = joblib.load(os.path.join(BASE, "classifier.pkl"))
vectorizer = joblib.load(os.path.join(BASE, "vectorizer.pkl"))

def ist_zutat(wort):
    x = vectorizer.transform([wort])
    return bool(model.predict(x)[0])

def extrahiere_zutaten(text):
    # einfache Vorverarbeitung
    text = text.lower().replace(",", "").replace(".", "")
    woerter = text.split()
    return [w for w in woerter if ist_zutat(w)]
