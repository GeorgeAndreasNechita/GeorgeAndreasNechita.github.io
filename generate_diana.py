import json
import ollama

def get_prompt(n):
    return f"""
You are a master German language educator specializing in CEFR progression from A2 to B2.
Your task is to generate a JSON array containing exactly {n} unique German (lang1) and English (lang2) sentence pairs.

GOAL: Build natural fluency bridging low-intermediate (A2) to high-intermediate (B2) German.

VARIATION & RANDOMIZATION INSTRUCTIONS:
For this batch, dynamically select a random blend across all of the following parameters:

1. CEFR Progression Balance:
   - 30% A2 (daily routines, basic preferences, simple past tense / Perfekt).
   - 40% B1 (expressing opinions, obligations, connecting thoughts with weil/dass/wenn, workplace communication).
   - 30% B2 (complex arguments, indirect questions, passives, Konjunktiv II for hypothetical scenarios, advanced connectors like obwohl/falls/indem).

2. Contexts & Topics (Select randomly across batches):
   - Daily life, housing, shopping, and social plans.
   - Work, office life, job interviews, professional emails, and projects.
   - Travel, transportation, hobbies, media, and culture.
   - Expressing personal opinions, feelings, disagreement, and agreements.
   - Health, appointments, technology, society, environment, and education.

3. Grammatical Variety:
   - Mix declarative sentences, questions (using wie, warum, ob, etc.), commands, conditional statements (hätte/wäre/würde), and passive voice.
   - Vary sentence length from punchy 4-word phrases up to realistic B2 compound sentences (12-16 words).

Formatting Rules:
- Output valid JSON only.
- Ensure the JSON structure strictly follows this schema:
[
  {{
    "lang1": "German sentence here.",
    "lang2": "English translation here."
  }}
]
- Ensure natural, modern German (no outdated or overly literal translations).
- Avoid repetitive sentence starters or identical structural templates.
"""

all_phrases = []
target_total = 25
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