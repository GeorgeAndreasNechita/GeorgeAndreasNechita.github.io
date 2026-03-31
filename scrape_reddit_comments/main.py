import os
from youtube_comment_downloader import YoutubeCommentDownloader, SORT_BY_POPULAR

# Pfad-Setup
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# EINSTELLUNGEN
VIDEO_URL = "https://www.youtube.com/watch?v=DCyu0TGCy9g&t=1512s" # Ersetze dies
OUTPUT_FILE = "youtube_comments.json"
LIMIT = 50  # Wie viele Kommentare möchtest du ziehen?

def scrape_youtube():
    downloader = YoutubeCommentDownloader()
    
    print(f"Lade Kommentare von YouTube...")
    
    # Kommentare abrufen (sortiert nach Beliebtheit)
    comments = downloader.get_comments_from_url(VIDEO_URL, sort_by=SORT_BY_POPULAR)
    
    extracted_count = 0
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for comment in comments:
            if extracted_count >= LIMIT:
                break
            
            text = comment.get('text', '')
            
            # Bereinigung: Zeilenumbrüche entfernen, Anführungszeichen escapen
            clean_text = text.replace('\n', ' ').replace('\r', ' ').replace('"', '\\"')
            
            # Dein Zielformat: { it: "TEXT", de: "" },
            # (Ich nehme an 'it' steht hier für den Originaltext)
            line = f'{{ "it": "{clean_text}", "de": "" }},\n'
            
            f.write(line)
            extracted_count += 1
            
            if extracted_count % 10 == 0:
                print(f"{extracted_count} Kommentare verarbeitet...")

    print(f"Fertig! {extracted_count} Kommentare wurden in '{OUTPUT_FILE}' gespeichert.")

if __name__ == "__main__":
    scrape_youtube()