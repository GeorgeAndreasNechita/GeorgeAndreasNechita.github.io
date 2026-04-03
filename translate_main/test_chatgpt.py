from openai import OpenAI

# Client erstellen (API Key wird aus der ENV Variable gelesen)
client = OpenAI()

# Einfache Anfrage
response = client.responses.create(
    model="gpt-5-mini",
    input="Schreibe einen kurzen Satz auf Deutsch."
)

# Ausgabe
print(response.output[0].content[0].text)