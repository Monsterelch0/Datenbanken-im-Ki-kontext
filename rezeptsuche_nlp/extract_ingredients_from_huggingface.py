from datasets import load_dataset
import re
import csv
from collections import Counter

# Load dataset from Hugging Face
dataset = load_dataset("RoshanVepulap/ingredients_to_recipe_llama2_format", split="train")

# Regular expression to extract ingredient list from the prompt
ingredient_pattern = re.compile(r"ingredients?:\s*(.*?)(?=(\.|checkout|check|$))", re.IGNORECASE)

# Storage for all found ingredients
all_ingredients = []

# Go through each sample
for item in dataset:
    text = item["text"]
    match = ingredient_pattern.search(text)
    if match:
        raw_ingredients = match.group(1)
        split_ingredients = [i.strip().lower() for i in re.split(r",| and ", raw_ingredients) if i.strip()]
        all_ingredients.extend(split_ingredients)

# Optional: count duplicates
ingredient_counts = Counter(all_ingredients)

# Write unique ingredients to CSV for model training
with open("zutaten_from_huggingface.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["wort", "label"])
    for ingredient in sorted(set(all_ingredients)):
        writer.writerow([ingredient, 1])

print(f"✅ Extrahiert: {len(set(all_ingredients))} eindeutige Zutaten.")
