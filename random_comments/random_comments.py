import re
import json
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Datei einlesen
with open("comments.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Deine Verarbeitung
gefilterter_text = re.sub(r'([.,;?:!])\s*', r'\1\n', text)
zeilen = [z.strip() for z in gefilterter_text.split('\n') if z.strip()]

# JSON-Struktur erstellen
result = []
for z in zeilen:
    result.append({
        "it": z,
        "de": ""
    })

# Datei speichern
with open("comments.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"{len(result)} Einträge gespeichert.")