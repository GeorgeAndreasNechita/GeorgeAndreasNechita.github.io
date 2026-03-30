
"""
vorlesen.py – Liest texts.txt vor und wechselt automatisch zwischen
Italienisch und Deutsch, wenn das Trennzeichen ' – ' erkannt wird.

Abhängigkeiten installieren:
    pip install gtts pygame

Verwendung:
    python vorlesen.py
    python vorlesen.py texts.txt          # eigene Datei angeben
"""

import sys
import re
import os
import tempfile
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# ── Abhängigkeiten prüfen ────────────────────────────────────────────────────
try:
    from gtts import gTTS
except ImportError:
    sys.exit("Bitte 'gtts' installieren:  pip install gtts")

try:
    import pygame
    pygame.mixer.init()
    USE_PYGAME = True
except ImportError:
    USE_PYGAME = False
    # Fallback: playsound oder subprocess
    try:
        from playsound import playsound as _playsound
        def play_file(path):
            _playsound(path)
    except ImportError:
        import subprocess, platform
        def play_file(path):
            """Plattformübergreifender Fallback-Player."""
            system = platform.system()
            if system == "Darwin":
                subprocess.run(["afplay", path], check=True)
            elif system == "Windows":
                subprocess.run(
                    ["powershell", "-c", f'(New-Object Media.SoundPlayer "{path}").PlaySync()'],
                    check=True,
                )
            else:  # Linux / andere
                for player in ("mpg123", "mpg321", "play", "ffplay"):
                    if subprocess.run(["which", player], capture_output=True).returncode == 0:
                        subprocess.run([player, "-q", path], check=True)
                        return
                sys.exit("Kein Audio-Player gefunden. Bitte mpg123 oder ffplay installieren.")

if USE_PYGAME:
    def play_file(path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.music.unload()   # Windows: Datei-Handle freigeben


# ── Hilfsfunktionen ──────────────────────────────────────────────────────────
SEPARATOR = " – "          # Trennzeichen zwischen IT- und DE-Teil
LANG_IT   = "it"
LANG_DE   = "de"

def speak(text: str, lang: str) -> None:
    """Synthetisiert `text` in `lang` und spielt es sofort ab."""
    text = text.strip()
    if not text:
        return
    tts = gTTS(text=text, lang=lang)
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        tmp_path = f.name
    try:
        tts.save(tmp_path)
        play_file(tmp_path)
    finally:
        os.unlink(tmp_path)


def process_line(line: str) -> None:
    """
    Erkennt, ob eine Zeile beide Sprachen enthält (getrennt durch ' – ')
    oder nur eine, und liest entsprechend vor.
    """
    line = line.strip()
    if not line:
        return

    if SEPARATOR in line:
        italian_part, german_part = line.split(SEPARATOR, maxsplit=1)
        print(f"🇮🇹  {italian_part.strip()}")
        speak(italian_part, LANG_IT)
        print(f"🇩🇪  {german_part.strip()}")
        speak(german_part, LANG_DE)
    else:
        # Sprache heuristisch bestimmen: Deutsch-typische Zeichen prüfen
        german_chars = set("äöüÄÖÜß")
        if any(c in german_chars for c in line):
            print(f"🇩🇪  {line}")
            speak(line, LANG_DE)
        else:
            print(f"🇮🇹  {line}")
            speak(line, LANG_IT)


# ── Hauptprogramm ────────────────────────────────────────────────────────────
def main():
    filepath = sys.argv[1] if len(sys.argv) > 1 else "texts.txt"

    if not os.path.isfile(filepath):
        sys.exit(f"Datei nicht gefunden: {filepath}")

    print(f"▶  Lese Datei: {filepath}\n{'─' * 50}")

    with open(filepath, encoding="utf-8") as f:
        for line in f:
            process_line(line)

    print("─" * 50 + "\n✔  Fertig.")


if __name__ == "__main__":
    main()
