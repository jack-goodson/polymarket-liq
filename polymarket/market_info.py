import requests

r = requests.get("https://gamma-api.polymarket.com/events?closed=false")
response = r.json()

print(response)