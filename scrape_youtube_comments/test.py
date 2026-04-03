import requests

url = "https://www.reddit.com/r/Italia/new.json"
headers = {
    "User-Agent": "Mozilla/5.0"  # Wichtig! Sonst blockt Reddit dich
}

posts = []
after = None
max_posts = 1000  # wie viele du ungefähr willst

while len(posts) < max_posts:
    params = {
        "limit": 100,   # max pro request
        "after": after
    }

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
        print("Fehler:", response.status_code)
        break

    data = response.json()
    children = data["data"]["children"]

    if not children:
        break

    for child in children:
        post = child["data"]
        title = post.get("title", "")
        text = post.get("selftext", "")
        posts.append((title, text))

    after = data["data"]["after"]

    if after is None:
        break

# In Datei speichern
with open("reddit_italia.txt", "w", encoding="utf-8") as f:
    for title, text in posts:
        f.write(f"Title: {title}\n")
        f.write(f"Text: {text}\n")
        f.write("="*50 + "\n")

print(f"{len(posts)} Beiträge gespeichert!")