import pandas as pd
import os
import csv

# 🔧 Adjust if needed
PARQUET_DIR = "food_ingredients_parquet"
OUTPUT_CSV = "zutaten_succcorese.csv"

all_ingredients = set()

# Load each parquet file
for filename in os.listdir(PARQUET_DIR):
    if filename.endswith(".parquet"):
        print(f"📥 Reading {filename}")
        df = pd.read_parquet(os.path.join(PARQUET_DIR, filename))
        if "ingredient" in df.columns:
            all_ingredients.update(df["ingredient"].dropna().str.lower().str.strip())

# Remove empty strings or nulls
all_ingredients = sorted(filter(lambda x: len(x) > 1, all_ingredients))

# Save to CSV
with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["wort", "label"])
    for zutat in all_ingredients:
        writer.writerow([zutat, 1])

print(f"\n✅ Fertig: {len(all_ingredients)} eindeutige Zutaten → {OUTPUT_CSV}")
