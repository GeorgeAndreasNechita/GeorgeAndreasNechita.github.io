import json
import ollama

def get_prompt(n):
    return """
You are an expert bilingual political analyst, socio-economist, and environmental translator specializing in international relations, public policy, and global sustainability.
Your task is to generate a JSON array containing exactly {n} unique Italian (lang1) and German (lang2) phrase pairs. VERY IMPORTANT: The texts must have a maximum of 8 words.

To ensure maximum diversity, strictly adhere to the following variation rules across the generated set:
Grammar & Structure: Mix declarative statements, interrogative questions, imperative policy calls to action, conditional clauses, and passive-voice phrasing.
Thematic Spread: Cover diverse topics including domestic politics, economic models, social welfare, environmental conservation, renewable energy, and carbon footprint reduction.
Tone: Balance formal diplomatic phrasing, academic debate, activist rhetoric, and policy negotiation language.
Complexity: Vary from short, punchy statements to complex analytical expressions within the 8-word limit.

Formatting Rules:
- Output valid JSON only. Do not wrap the JSON in markdown code blocks.
- Ensure the JSON structure strictly follows this schema:
[
  {{
    "lang1": "Italian sentence here.",
    "lang2": "German translation here."
  }}
]
- Do not repeat sentence structures or vocabulary patterns consecutively.
""".format(n=n)

all_phrases = []
target_total = 1000
batch_size = 20
total_batches = target_total // batch_size

print(f"Starting generation of {target_total} phrases in {total_batches} batches...")

for current_batch in range(total_batches):
    print(f"Generating batch {current_batch + 1} of {total_batches}...")
    try:
        response = ollama.chat(
            model="qwen2.5",
            messages=[{"role": "user", "content": get_prompt(batch_size)}],
            options={"num_ctx": 4096, "temperature": 0.7}
        )

        content = response["message"]["content"].strip()

        # Clean up markdown code blocks if the model adds them anyway
        if content.startswith("```"):
            content = content.split("```")[1]
            if content.startswith("json"):
                content = content[4:].strip()
            content = content.strip("`").strip()

        # Attempt to parse JSON safely
        batch = json.loads(content)
        all_phrases.extend(batch)
        print(f"Batch {current_batch + 1} successful!")

    except json.JSONDecodeError as jde:
        print(f"JSON parsing error in batch {current_batch + 1}: {jde}. Attempting to recover...")
        # Optional: Print out a snippet of the broken content to see what went wrong
    except Exception as e:
        print(f"Unexpected error in batch {current_batch + 1}: {e}. Skipping batch...")

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

print(f"Finished! Successfully saved {len(unique_phrases)} unique phrases to texts1.json.")