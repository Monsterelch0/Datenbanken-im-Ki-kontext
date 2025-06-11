from nlp_custom import ist_zutat, extrahiere_zutaten

print("Modell-Test: Zutaten erkennen")
print("Gib einen Satz ein (oder 'exit' zum Beenden)")

while True:
    eingabe = input("\n> ")
    if eingabe.strip().lower() == "exit":
        break

    zutaten = extrahiere_zutaten(eingabe)
    print("Erkannte Zutaten:", zutaten)

    # Optional: Zeige Einzelklassifikationen
    print("Wortklassifikation:")
    for wort in eingabe.lower().split():
        print(f"{wort} → {'Zutat' if ist_zutat(wort) else 'kein Zutat'}")
