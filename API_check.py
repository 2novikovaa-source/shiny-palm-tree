import json

import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
response.raise_for_status()

data = response.json()
print(json.dumps(data, indent=2))

joke = data["value"]
print(joke)
