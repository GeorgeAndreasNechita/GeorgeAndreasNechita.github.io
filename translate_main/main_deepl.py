import json, deepl, re, os
from dotenv import load_dotenv

load_dotenv()
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")

def translate_and_save(text, json_file="result.json"):
    gefilterter_text = re.sub(r'([.,;?:!])\s*', r'\1\n', text)
    zeilen = [z.strip() for z in gefilterter_text.split('\n') if z.strip()]

    # 2. DeepL Setup
    translator = deepl.Translator(DEEPL_API_KEY)
    
    print(f"Starte Batch-Übersetzung von {len(zeilen)} Zeilen...")

    # 3. Batch-Übersetzung (IT -> DE)
    results = translator.translate_text(zeilen, source_lang="IT", target_lang="DE")
    
    # 4. Daten für JSON und Excel vorbereiten
    # Hier nutzen wir direkt "it" und "de" als Keys
    daten = []
    for original, result in zip(zeilen, results):
        daten.append({
            "it": original,
            "de": result.text
        })

    # 5. Als JSON speichern
    # 'ensure_ascii=False' sorgt dafür, dass Umlaute/Sonderzeichen korrekt bleiben
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(daten, f, ensure_ascii=False, indent=2)

    print(f"Fertig!")
    print(f"-> JSON gespeichert unter: {json_file}")

with open("current_part.txt", "r", encoding="utf-8") as f:
    MEIN_TEXT = f.read()

MEIN_TEXT = re.sub(r'\r?\n+', ' ', MEIN_TEXT)

with open("current_part.txt", "w", encoding="utf-8") as f:
    f.write(MEIN_TEXT)

translate_and_save(MEIN_TEXT)