import os
import re
import json
from youtube_comment_downloader import YoutubeCommentDownloader, SORT_BY_POPULAR
from deep_translator import GoogleTranslator

# Pfad-Setup
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# EINSTELLUNGEN
VIDEO_URL = "https://www.youtube.com/watch?v=yCsxuGKBNQw"
OUTPUT_FILE = "youtube_comments.json"
LIMIT = 300  # Jetzt gehen 100 deutlich schneller

def scrape_and_translate_fast():
    downloader = YoutubeCommentDownloader()
    translator = GoogleTranslator(source='it', target='de')
    
    print(f"Lade Kommentare von YouTube...")
    comments = downloader.get_comments_from_url(VIDEO_URL, sort_by=SORT_BY_POPULAR)
    
    all_data = []
    extracted_count = 0
    
    for comment in comments:
        if extracted_count >= LIMIT:
            break
        
        text = comment.get('text', '')
        clean_text = text.replace('\n', ' ').replace('\r', ' ')
        
        # Segmente erstellen und säubern
        raw_segments = re.split(r'[.,:;!?]+', clean_text)
        # Nur Segmente behalten, die wirklich Text enthalten (länger als 2 Zeichen)
        segments_to_translate = [s.strip() for s in raw_segments if len(s.strip()) > 2]
        
        if segments_to_translate:
            try:
                # BATCH-ÜBERSETZUNG: Schickt die ganze Liste auf einmal
                translations = translator.translate_batch(segments_to_translate)
                
                # Ergebnisse zusammenführen
                for it, de in zip(segments_to_translate, translations):
                    all_data.append({"it": it, "de": de})
                    
            except Exception as e:
                print(f"Fehler bei Batch-Übersetzung: {e}")
        
        extracted_count += 1
        if extracted_count % 10 == 0:
            print(f"{extracted_count} Kommentare verarbeitet...")

    # Speichern
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)

    print(f"Fertig! {len(all_data)} Segmente in '{OUTPUT_FILE}' gespeichert.")

if __name__ == "__main__":
    scrape_and_translate_fast()