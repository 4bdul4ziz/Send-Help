import requests

url = "https://discord.com/api/webhooks/889848958942314537/fNhRP8JilpjH9sTm8MFr4rR-Mzd2weUUPn78snziwcGw-9zEPz0LXdXC8qi--Kwv3b09"
while True:
    message = input()
    r = requests.post(url, data={"content": message})
