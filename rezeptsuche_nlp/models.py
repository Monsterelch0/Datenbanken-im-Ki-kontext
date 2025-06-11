import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="postgres",
        user="postgres",
        password="Test"
    )

def rezepte_suchen(zutaten_liste):
    conn = get_connection()
    cur = conn.cursor()

    if not zutaten_liste:
        # Wenn keine Zutaten erkannt wurden, gib leere Liste zurück
        conn.close()
        return []

    like_clause = " AND ".join([f"zutaten ILIKE '%{z}%'" for z in zutaten_liste])
    query = f"SELECT * FROM rezepte WHERE {like_clause} LIMIT 10"

    cur.execute(query)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result
