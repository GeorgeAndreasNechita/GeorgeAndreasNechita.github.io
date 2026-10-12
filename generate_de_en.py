import json
import random
import ollama
from ollama import ResponseError

# ---------------- CONFIG ----------------
MODEL = "qwen2.5:14b"          # Fits completely inside 16GB VRAM
OUTFILE = "texts_temporary.json"
target_total = 1000
batch_size = 25
total_batches = target_total // batch_size
MAX_RETRIES = 3

# Optional: one focus per batch, rotated. Set to [] to disable.
FOCUS_AREAS = [
    "introducing myself", "my experience", "motivation", "participatory planning",
    "sustainability", "teamwork", "strengths/weaknesses",
    "questions for the interviewer", "salary and availability",
    "PhD: research proposal", "PhD: contacting professors", "PhD: motivation",
]

# ---------------- PROMPT ----------------
# Placeholders: {batch_size} and {focus}. JSON braces are doubled because of .format().
PROMPT = """
German phrases at A2-B1 level, focused on job interviews and PhD applications in urban planning.

Context: I'm an architect and urban planner (participatory planning, sustainable design, public space). I speak Spanish and English.

Content:
- Categories: introducing myself, my experience, motivation, participatory planning, sustainability, teamwork, strengths/weaknesses, questions for the interviewer, salary and availability, PhD (research proposal, contacting professors, motivation).
- Each phrase includes: German, English translation, level (A2 or B1), a usage tip (formal/informal, common mistake), and a simpler variant.
- 1st and 3rd person
- About {batch_size} phrases in natural, realistic German (Sie-form, professional register).
{focus}
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
- Each "lang1" should have between  8 and 11 Words
"""

def get_prompt(batch_index):
    focus = ""
    if FOCUS_AREAS:
        focus = f"- Focus this batch on: {FOCUS_AREAS[batch_index % len(FOCUS_AREAS)]}\n"
    return PROMPT.format(batch_size=batch_size, focus=focus)

# ---------------- HELPERS ----------------
def extract_items(batch):
    """Defensive unpacking: handles dict-wrapped lists and single items."""
    if isinstance(batch, dict):
        extracted_list = []
        for value in batch.values():
            if isinstance(value, list):
                extracted_list = value
                break
        if not extracted_list and "lang1" in batch:
            extracted_list = [batch]
        batch = extracted_list
    if isinstance(batch, list):
        return [item for item in batch if isinstance(item, dict)]
    return None

def save(phrases):
    with open(OUTFILE, "w", encoding="utf-8") as f:
        json.dump(phrases, f, ensure_ascii=False, indent=2)

# ---------------- MAIN ----------------
all_phrases = []
failed_batches = []

print(f"Starting generation of {target_total} phrases in {total_batches} batches...")

for current_batch in range(total_batches):
    print(f"Generating batch {current_batch + 1} of {total_batches}...")

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = ollama.chat(
                model=MODEL,
                format="json",
                messages=[{"role": "user", "content": get_prompt(current_batch)}],
                options={
                    "num_ctx": 4096,
                    "temperature": 0.75,
                    "repeat_penalty": 1.1,
                    "num_predict": 2500,                 # stops runaway loops
                    "seed": random.randint(0, 2**31),    # retries differ
                },
            )
            content = response["message"]["content"].strip()
            valid_items = extract_items(json.loads(content))

            if valid_items is None:
                print(f"Warning: Batch {current_batch + 1} returned unexpected JSON structure (attempt {attempt}/{MAX_RETRIES}).")
                continue

            all_phrases.extend(valid_items)
            print(f"Batch {current_batch + 1} successful! Extracted {len(valid_items)} phrases. Total so far: {len(all_phrases)}")
            break

        except json.JSONDecodeError as jde:
            print(f"JSON parsing error in batch {current_batch + 1} (attempt {attempt}/{MAX_RETRIES}): {jde}.")
        except ResponseError as re:
            print(f"Ollama error in batch {current_batch + 1} (attempt {attempt}/{MAX_RETRIES}): {re}")
    else:
        print(f"Batch {current_batch + 1} FAILED after {MAX_RETRIES} attempts, skipping.")
        failed_batches.append(current_batch + 1)

    save(all_phrases)  # checkpoint after every batch

# --- DEDUPLICATION STEP ---
seen = set()
unique_phrases = []
for item in all_phrases:
    phrase = item.get("lang1", "").strip().lower()
    if phrase and phrase not in seen:
        seen.add(phrase)
        unique_phrases.append(item)

save(unique_phrases)

print(f"Finished! Successfully saved {len(unique_phrases)} unique phrases to {OUTFILE}.")
if failed_batches:
    print(f"Failed batches: {failed_batches}")