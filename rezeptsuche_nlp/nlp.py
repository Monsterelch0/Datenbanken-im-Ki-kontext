import spacy
nlp = spacy.load("de_core_news_md")

def extrahiere_zutaten(text):
    doc = nlp(text)
    return [token.text.lower() for token in doc if token.pos_ == "NOUN"]
