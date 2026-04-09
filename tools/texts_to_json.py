import re, json, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("content.txt", "r", encoding="utf-8") as f:
    text = f.read()

# In Sätze aufteilen (nach Satzzeichen)
gefilterter_text = re.sub(r'([.,;?:!])\s*', r'\1\n', text)
zeilen = [z.strip() for z in gefilterter_text.split('\n') if z.strip()]

# JSON-Struktur erzeugen
result = []
for z in zeilen:
    if z not in [".", ",", "!", "”."]:
        result.append({
            "it": z,
            "de": ""
        })

# Direkt als JSON speichern
with open("content.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"{len(result)} Einträge in comments.json gespeichert")