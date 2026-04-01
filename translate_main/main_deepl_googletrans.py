import json
import re
import os
from deep_translator import GoogleTranslator

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def translate_and_save(text, json_file="result.json"):
    gefilterter_text = re.sub(r'([.,;?:])\s*', r'\1\n', text)
    zeilen = [z.strip() for z in gefilterter_text.split('\n') if z.strip()]

    translator = GoogleTranslator(source='it', target='de')
    
    print(f"Starte Batch-Übersetzung von {len(zeilen)} Zeilen...")

    try:
        results = translator.translate_batch(zeilen)
        
        daten = [{"it": orig, "de": trans} for orig, trans in zip(zeilen, results)]

        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(daten, f, ensure_ascii=False, indent=2)

        print(f"Erfolg! Datei erstellt unter: {os.path.abspath(json_file)}")

    except Exception as e:
        print(f"Fehler: {e}")

file_path = "current_part.txt"

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        mein_text = f.read()

    mein_text = re.sub(r'\r?\n+', ' ', mein_text)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(mein_text)

    translate_and_save(mein_text)
else:
    print(f"Datei '{file_path}' nicht gefunden.")