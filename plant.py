import requests
import json

API_KEY = "xh6IsifTjKQT8ZSW3FuYmzl5q6TK-7aq907K78Bo8OQ"
BASE_URL = "https://trefle.io/api/v1/plants"

response = requests.get(BASE_URL, params={"token": API_KEY})
data = response.json()

# Save or process the plant data
with open("plants.json", "w") as f:
    json.dump(data, f)
