import json
import ollama

def get_prompt(n):
    return """
You are an expert bilingual political analyst, socio-economist, and environmental translator specializing in international relations, public policy, and global sustainability.
Your task is to generate a JSON array containing exactly {n} unique German (lang1) and English (lang2) phrase pairs. VERY IMPORTANT: The texts should have maximum 8 words.
To ensure maximum diversity, strictly adhere to the following variation rules across the generated set:
Grammar & Structure: Mix declarative statements, interrogative questions (using cómo, cuál, por qué, etc.), imperative policy calls to action, conditional clauses, and passive-voice phrasing.
Thematic Spread: Cover a wide range of sub-topics, including comparative Ecuadorian and German domestic politics, Global South vs. Global North economic models, social welfare systems, environmental conservation (e.g., Yasuní vs. Energiewende), renewable energy transition, and carbon footprint reduction strategies.
Tone: Include a balance of formal diplomatic phrasing, academic socio-economic debate, activist call-to-action rhetoric, and policy negotiation language.
Complexity: Vary the structure from short, punchy statements to complex, multi-clause analytical expressions.

Formatting Rules:
- Output valid JSON only. Do not wrap the JSON in markdown code blocks if requested otherwise, or use standard json formatting.
- Ensure the JSON structure strictly follows this schema:
[
  {{
    "lang1": "German sentence here.",
    "lang2": "English translation here."
  }}
]
- Do not repeat sentence structures or vocabulary patterns consecutively.
""".format(n=n)

all_phrases = []
target_total = 20  # Keep it small for testing, scale to 20000 later!
batch_size = 20     # Lower batch size (20-30) prevents the model from breaking JSON rules
total_batches = target_total // batch_size

print(f"Starting generation of {target_total} phrases in {total_batches} batches...")

for current_batch in range(total_batches):
    print(f"Generating batch {current_batch + 1} of {total_batches}...")
    try:
        response = ollama.chat(
            model="qwen2.5:14b",  # Fits completely inside 16GB VRAM
            format="json",         # Forces Ollama to strictly enforce valid JSON output
            messages=[{"role": "user", "content": get_prompt(batch_size)}],
            options={"num_ctx": 4096, "temperature": 0.5}
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