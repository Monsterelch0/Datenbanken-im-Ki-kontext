import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Trainingsdaten laden
df = pd.read_csv("zutaten_training.csv")

# Vektorisieren
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["wort"])
y = df["label"]

# Modell trainieren
model = LogisticRegression()
model.fit(X, y)

# Modelle speichern
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/classifier.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("Modell & Vektorizer gespeichert.")
