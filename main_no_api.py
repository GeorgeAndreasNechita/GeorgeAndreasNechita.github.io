import json
import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def translate_and_save(text, json_file="result.json"):
    # 1. Text teilen (nach Punkt, Komma, Semikolon)
    gefilterter_text = re.sub(r'([.,;?])\s*', r'\1\n', text)
    zeilen = [z.strip() for z in gefilterter_text.split('\n') if z.strip()]

    # 2. Lokales KI-Modell Setup (Ohne Pipeline)
    model_name = "Helsinki-NLP/opus-mt-it-de"
    print(f"Lade Offline-Übersetzungsmodell ({model_name})...")
    
    # Tokenizer und Modell direkt laden
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    
    print(f"Starte lokale Batch-Übersetzung von {len(zeilen)} Zeilen...")

    # 3. Batch-Übersetzung & Datenaufbereitung
    daten = []
    
    for i, original in enumerate(zeilen):
        # Text in Zahlen umwandeln, die das Modell versteht
        inputs = tokenizer(original, return_tensors="pt", padding=True, truncation=True)
        
        # Übersetzung generieren
        translated_tokens = model.generate(**inputs)
        
        # Generierte Tokens zurück in lesbaren Text umwandeln
        result = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
        
        daten.append({
            "it": original,
            "de": result
        })
        
        # Fortschrittsanzeige
        if (i + 1) % 10 == 0 or (i + 1) == len(zeilen):
            print(f"{i + 1} von {len(zeilen)} übersetzt...")

    # 4. Als JSON speichern
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(daten, f, ensure_ascii=False, indent=2)

    print("Fertig!")
    print(f"-> JSON gespeichert unter: {json_file}")

# 5. Datei einlesen und Funktion aufrufen
try:
    with open("current_part.txt", "r", encoding="utf-8") as f:
        MEIN_TEXT = f.read()
    translate_and_save(MEIN_TEXT)
except FileNotFoundError:
    print("Fehler: Die Datei 'current_part.txt' wurde nicht gefunden.")