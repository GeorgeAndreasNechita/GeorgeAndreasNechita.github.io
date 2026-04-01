import requests, os
from dotenv import load_dotenv

load_dotenv()
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")

url = "https://api-free.deepl.com/v2/usage"
headers = {
    "Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}"
}

response = requests.get(url, headers=headers)
data = response.json()

used = data.get("character_count", 0)
limit = data.get("character_limit", 0)
remaining = limit - used

print(f"Verbraucht: {used}")
print(f"Limit: {limit}")
print(f"Verbleibend: {remaining}")