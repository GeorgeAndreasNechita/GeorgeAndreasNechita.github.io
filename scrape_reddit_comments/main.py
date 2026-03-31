import os
import re
from youtube_comment_downloader import YoutubeCommentDownloader, SORT_BY_POPULAR

# Pfad-Setup
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# EINSTELLUNGEN
VIDEO_URL = "https://www.youtube.com/watch?v=DCyu0TGCy9g&t=1512s"
OUTPUT_FILE = "youtube_comments.json"
LIMIT = 300  # Anzahl der Haupt-Kommentare, die abgerufen werden

def scrape_youtube():
    downloader = YoutubeCommentDownloader()
    
    print(f"Lade Kommentare von YouTube...")
    
    # Kommentare abrufen
    comments = downloader.get_comments_from_url(VIDEO_URL, sort_by=SORT_BY_POPULAR)
    
    extracted_count = 0
    total_segments = 0
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for comment in comments:
            if extracted_count >= LIMIT:
                break
            
            text = comment.get('text', '')
            
            # 1. Bereinigung: Zeilenumbrüche durch Leerzeichen ersetzen
            clean_text = text.replace('\n', ' ').replace('\r', ' ')
            
            # 2. Splitten nach Satzzeichen: . , : ; ! ?
            # Das re.split behält die Trennzeichen nicht bei. 
            # Wenn du sie behalten willst, müsste man das Pattern anpassen.
            # Hier splitten wir bei jedem dieser Zeichen:
            segments = re.split(r'[.,:;!?]+', clean_text)
            
            for segment in segments:
                # Leerzeichen am Anfang/Ende entfernen
                segment = segment.strip()
                
                # Nur speichern, wenn das Segment nicht leer ist
                if segment:
                    # Anführungszeichen für JSON escapen
                    safe_segment = segment.replace('"', '\\"')
                    
                    line = f'{{ "it": "{safe_segment}", "de": "" }},\n'
                    f.write(line)
                    total_segments += 1
            
            extracted_count += 1
            if extracted_count % 10 == 0:
                print(f"{extracted_count} Kommentare verarbeitet ({total_segments} Teilstücke)...")

    print(f"Fertig! {extracted_count} Kommentare wurden in {total_segments} Segmenten in '{OUTPUT_FILE}' gespeichert.")

if __name__ == "__main__":
    scrape_youtube()