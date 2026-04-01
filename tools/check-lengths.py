import re

def translate_and_save(text):
    # 1. Text teilen (nach Punkt, Komma, Semikolon, Fragezeichen, Doppelpunkt)
    gefilterter_text = re.sub(r'([.,;?:])\s*', r'\1\n', text)
    zeilen = [z.strip() for z in gefilterter_text.split('\n') if z.strip()]
    print("Gefilterter Text:")
    print(gefilterter_text)


with open("current_part.txt", "r", encoding="utf-8") as f:
    MEIN_TEXT = f.read()

MEIN_TEXT = re.sub(r'\r?\n+', ' ', MEIN_TEXT)

with open("current_part.txt", "w", encoding="utf-8") as f:
    f.write(MEIN_TEXT)

translate_and_save(MEIN_TEXT)