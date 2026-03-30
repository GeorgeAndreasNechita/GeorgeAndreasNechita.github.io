import requests
import json
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Die URL des Beitrags + .json am Ende
URL = "https://www.reddit.com/r/Italia/comments/1i773ct/che_ne_dite/.json"
OUTPUT_FILE = "comments.txt"

def scrape_without_api():
    # Wir brauchen einen "User-Agent", damit Reddit die Anfrage nicht blockiert
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    print("Lade Daten von Reddit...")
    response = requests.get(URL, headers=headers)
    
    if response.status_code != 200:
        print(f"Fehler beim Laden: Status Code {response.status_code}")
        return

    data = response.json()
    
    # Reddit JSON Struktur: [0] ist der Post, [1] sind die Kommentare
    comments_data = data[1]['data']['children']
    
    extracted_count = 0
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for item in comments_data:
            if item['kind'] == 't1': # t1 steht für einen Kommentar
                comment_body = item['data'].get('body', '')
                
                # Bereinigung: Zeilenumbrüche weg, Anführungszeichen escapen
                clean_text = comment_body.replace('\n', ' ').replace('"', '\\"')
                
                # Dein gewünschtes Format
                line = f'{{ it: "{clean_text}", de: "" }},\n'
                f.write(line)
                extracted_count += 1
                
    print(f"Fertig! {extracted_count} Kommentare wurden in '{OUTPUT_FILE}' gespeichert.")

if __name__ == "__main__":
    scrape_without_api()