import requests, re, json, os
from bs4 import BeautifulSoup

os.chdir(os.path.dirname(os.path.abspath(__file__)))

url = "https://www.guidapsicologi.it/domande/scelte-ragazza"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

elements = soup.select(".box > :nth-child(3).text, " "#question > :nth-child(3).text, " "#question > :first-child")

texts = []
for el in elements:
    text = el.get_text(strip=True)
    if text:
        text = text.replace('"', "'")
        texts.append(text)

with open("comments.txt", "w", encoding="utf-8") as f:
    for t in texts:
        f.write(t + "\n")

print(f"{len(texts)} Einträge gespeichert in comments.txt")

with open("comments.txt", "r", encoding="utf-8") as f:
    text = f.read()


gefilterter_text = re.sub(r'([.,;?:!])\s*', r'\1\n', text)
zeilen = [z.strip() for z in gefilterter_text.split('\n') if z.strip()]


result = []
for z in zeilen:
    result.append({
        "it": z,
        "de": ""
    })


with open("comments.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"{len(result)} Einträge gespeichert.")