import json
import re

def brute_force_fix(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as f:
            content = f.read()

        print(f"Lese '{input_filename}' ein und extrahiere Daten...")

        # 1. Bereinigung von fiesen unsichtbaren Zeichen und typografischen Quotes
        content = content.replace('\xa0', ' ').replace('„', "'").replace('“', "'")
        
        # 2. Wir suchen nach allen Vorkommen von "it": "..." und "de": "..." 
        # unabhängig davon, ob das JSON drumherum kaputt ist.
        it_matches = re.findall(r'"it":\s*"(.*?)"', content, flags=re.DOTALL)
        de_matches = re.findall(r'"de":\s*"(.*?)"', content, flags=re.DOTALL)

        fixed_data = []
        
        # 3. Wir führen die Paare wieder zusammen
        # Wir gehen davon aus, dass die Anzahl der italienischen und deutschen Sätze gleich ist.
        for it_text, de_text in zip(it_matches, de_matches):
            # Wir säubern die Texte von restlichen unmaskierten Anführungszeichen
            clean_it = it_text.replace('"', "'").strip()
            clean_de = de_text.replace('"', "'").strip()
            
            fixed_data.append({
                "it": clean_it,
                "de": clean_de
            })

        # 4. Speichern als perfektes JSON
        if not fixed_data:
            print("❌ Keine Daten gefunden. Ist das Format der .txt korrekt?")
            return

        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(fixed_data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Erfolg! {len(fixed_data)} Einträge wurden gerettet und in '{output_filename}' gespeichert.")

    except Exception as e:
        print(f"❌ Kritischer Fehler: {e}")

if __name__ == "__main__":
    brute_force_fix('texts.txt', 'texts.json')