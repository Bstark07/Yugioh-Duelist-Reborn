import requests
import json

IMAGE_BASE = "https://ygoprodeck.com/pics/"

data = "cards_yugi.json"

# json_object = json.load (data)
card_dict = {}


with open(data, 'r') as file:
    card_dict = json.load(file)

for i in card_dict:
    for c in i:
        response = requests.get(IMAGE_BASE + c['id'] + ".jpg")
        with open("card_images/" + c['id'] + ".jpg", 'wb') as f:
            f.write(response.content)
