import json
import ollama
import random
from ollama import ResponseError

OUTFILE = "texts_temporary.json"

categories = [
    "introducing myself", "my experience", "motivation", "participatory planning",
    "sustainability", "teamwork", "strengths and weaknesses",
    "questions for the interviewer", "salary and availability",
    "PhD research proposal", "contacting professors", "PhD motivation",
]

def get_prompt(n, category):
    return f"""Generate {n} German phrases (A2-B1 level) for job interviews and PhD applications in urban planning.
Category: {category}
Context: I'm an architect and urban planner (participatory planning, sustainable design, public space). I speak Spanish and English.
Use natural, modern German in Sie-form, professional register. Mix 1st and 3rd person. Vary vocabulary and sentence structure.
Return a JSON object: {{"phrases": [{{"lang1": "German sentence", "lang2": "English translation"}}]}}"""

all_phrases = []
total_batches = 120
batch_size = 25

for i in range(total_batches):
    category = categories[i % len(categories)]
    for attempt in range(3):
        try:
            response = ollama.chat(
                model="qwen2.5:14b",
                format="json",
                messages=[{"role": "user", "content": get_prompt(batch_size, category)}],
                options={
                    "num_ctx": 4096,
                    "temperature": 0.8,
                    "repeat_penalty": 1.1,
                    "num_predict": 2500,   # hard cap so loops can't run away
                    "seed": random.randint(0, 2**31),
                },
            )
            data = json.loads(response["message"]["content"])
            items = data.get("phrases", []) if isinstance(data, dict) else data
            valid = [x for x in items if isinstance(x, dict) and "lang1" in x and "lang2" in x]
            all_phrases.extend(valid)
            print(f"Batch {i+1}: {len(valid)} phrases")
            break
        except (ResponseError, json.JSONDecodeError) as e:
            print(f"Batch {i+1} attempt {attempt+1} failed: {e}")
    # checkpoint after every batch
    with open(OUTFILE, "w", encoding="utf-8") as f:
        json.dump(all_phrases, f, ensure_ascii=False, indent=2)