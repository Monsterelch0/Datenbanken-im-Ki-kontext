from nlp import extrahiere_zutaten

print("🔎 spaCy-NLP-Test: Extrahiere Nomen als Zutaten")
print("Gib einen Satz ein (oder 'exit' zum Beenden)")

while True:
    eingabe = input("\n> ")
    if eingabe.strip().lower() == "exit":
        break

    zutaten = extrahiere_zutaten(eingabe)
    print("✅ Erkannte Zutaten:", zutaten)
