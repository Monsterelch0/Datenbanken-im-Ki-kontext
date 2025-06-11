CREATE TABLE IF NOT EXISTS rezepte (
    id SERIAL PRIMARY KEY,
    titel TEXT,
    zutaten TEXT,
    kochzeit_min INTEGER,
    schwierigkeitsgrad TEXT,
    beschreibung TEXT
);

INSERT INTO rezepte (titel, zutaten, kochzeit_min, schwierigkeitsgrad, beschreibung) VALUES
('Tomatenreis', 'Tomaten, Reis, Zwiebeln, Knoblauch', 30, 'Einfach', 'Ein einfaches Gericht mit Tomatensauce.'),
('Reis-Gemüsepfanne', 'Reis, Paprika, Brokkoli, Sojasauce', 25, 'Mittel', 'Leichte asiatische Pfanne.'),
('Pasta Napoli', 'Tomaten, Nudeln, Basilikum, Knoblauch', 20, 'Einfach', 'Klassische italienische Pasta mit Tomatensauce.');
