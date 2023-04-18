import requests

url = "https://discord.com/api/webhooks/1097562508899930152/V0xQ7yeTrtBwCqNWTZPFO12-YU60HE9BEqXv-DWKBrigCe71onoBjtpjrvFmbOpKLq63"
while True:
    message = input()
    r = requests.post(url, data={"content": message})
