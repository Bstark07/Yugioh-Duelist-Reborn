import requests
import json

url_base = "https://db.ygoprodeck.com/api/v2/cardinfo.php?set=Starter%20Deck:%20Yugi"

headers = {'Content-Type': 'application/json'}

response = requests.get(url_base)
data = response.json()

with open("cards_yugi.json", 'w+') as cardbase:
    json.dump(data, cardbase, indent=4)
