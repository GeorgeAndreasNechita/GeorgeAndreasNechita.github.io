import json
import ollama

def get_prompt(n):
    return f"""
You are a master German language educator specializing in practical, modern vocabulary for CEFR levels A2 through B2.
Your task is to generate a JSON array containing exactly {n} unique German (lang1) and English (lang2) sentence pairs.

GOAL: Build realistic, everyday German fluency using high-frequency, real-world objects and practical vocabulary.

VOCABULARY & CONTENT MANDATE:
Every generated sentence must feature concrete, practical, modern everyday items, activities, and concepts.
- Objects & Tech: Computer, Smartphone, Kopfhörer, Laptop, Akku, Schlüssel, Auto, Fahrrad, Bus, Steckdose, etc.
- Everyday Items & Food: Blumen, Zigaretten, Chips, Kaffee, Flasche, Geldbörse, Tasche, Kleidung, etc.
- Daily Contexts: Work, home routines, running errands, hanging out with friends, commuting, shopping, social media, making plans, health, and modern hobbies.

VARIATION & STRUCTURE:
1. CEFR Progression Balance:
   - 30% A2: Simple daily statements, direct requests, using basic past tense (Perfekt).
     (e.g., "Wo sind meine Kopfhörer?", "Ich kaufe eine Packung Chips.")
   - 40% B1: Work communication, plans, expressing reasons/opinions using weil, dass, wenn.
     (e.g., "Mein Laptop-Akku ist leer, deshalb muss ich den Stecker suchen.")
   - 30% B2: Complex everyday situations, hypothetical scenarios (Konjunktiv II), passives, and advanced connectors (obwohl, falls, indem).
     (e.g., "Hätte ich mein Ladekabel nicht vergessen, könnte ich den Arbeitsbericht jetzt abschicken.")

2. Structural Diversity:
   - Mix everyday statements, casual questions, friendly advice, indirect requests, and minor complaints/problem-solving.
   - Sentence length should range dynamically from short, punchy phrases (3–6 words) to standard conversational sentences (8–14 words).

Formatting Rules:
- Output valid JSON only.
- Ensure the JSON structure strictly follows this schema:
[
  {{
    "lang1": "German sentence here.",
    "lang2": "English translation here."
  }}
]
- Ensure natural, modern, colloquial German as spoken today (avoid unnatural dictionary-style sentences).
- Do not repeat identical vocabulary words or sentence frames consecutively within the batch.
"""

all_phrases = []
target_total = 3000
batch_size = 25
total_batches = target_total // batch_size

print(f"Starting generation of {target_total} phrases in {total_batches} batches...")

for current_batch in range(total_batches):
    print(f"Generating batch {current_batch + 1} of {total_batches}...")
    try:
        response = ollama.chat(
            model="qwen2.5:14b",  # Fits completely inside 16GB VRAM
            format="json",         # Forces Ollama to strictly enforce valid JSON output
            messages=[{"role": "user", "content": get_prompt(batch_size)}],
            options={"num_ctx": 4096, "temperature": 0.75}
        )

        content = response["message"]["content"].strip()
        
        # Parse JSON directly
        batch = json.loads(content)
        
        # --- NEW CODE: Defensive unpacking ---
        # If the LLM wrapped the array in a dictionary (e.g., {"phrases": [...]})
        if isinstance(batch, dict):
            extracted_list = []
            for value in batch.values():
                if isinstance(value, list):
                    extracted_list = value
                    break
            # If it just returned a single item instead of a list
            if not extracted_list and "lang1" in batch:
                extracted_list = [batch]
            batch = extracted_list
            
        # Ensure batch is a list and only extend with dictionary objects
        if isinstance(batch, list):
            valid_items = [item for item in batch if isinstance(item, dict)]
            all_phrases.extend(valid_items)
            print(f"Batch {current_batch + 1} successful! Extracted {len(valid_items)} phrases.")
        else:
            print(f"Warning: Batch {current_batch + 1} returned unexpected JSON structure.")
        # --- END NEW CODE ---
        
    except json.JSONDecodeError as jde:
        print(f"JSON parsing error in batch {current_batch + 1}: {jde}.")

# --- DEDUPLICATION STEP ---
seen = set()
unique_phrases = []
for item in all_phrases:
    phrase = item.get("lang1", "").strip().lower()
    if phrase and phrase not in seen:
        seen.add(phrase)
        unique_phrases.append(item)

# Save final clean list to file
with open("texts_temporary.json", "w", encoding="utf-8") as f:
    json.dump(unique_phrases, f, ensure_ascii=False, indent=2)

print(f"Finished! Successfully saved {len(unique_phrases)} unique phrases to texts_temporary.json.")