import json
import ollama

def get_prompt(n):
    return f"""
Generate exactly {n} unique, 100% grammatically correct German-to-English translation pairs designed for an A2 student trying to reach B1. 
CRITICAL RULES:
1. Every German phrase ("lang1") must be a complete, grammatically sound sentence between 4 and 7 words long. No broken fragments.
2. Focus on B1-bridging grammar: subordinate clauses (weil, dass, obwohl), reflexive verbs, or connectors.
3. Output MUST be a valid raw JSON array of objects with keys "lang1" and "lang2". 
4. Do NOT wrap the JSON in markdown code blocks. Just output the raw JSON array.
"""

all_phrases = []
target_total = 10000  # Keep it small for testing, scale to 20000 later!
batch_size = 20     # Lower batch size (20-30) prevents the model from breaking JSON rules
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
with open("texts1.json", "w", encoding="utf-8") as f:
    json.dump(unique_phrases, f, ensure_ascii=False, indent=2)

print(f"Finished! Successfully saved {len(unique_phrases)} unique phrases to texts1.json.")