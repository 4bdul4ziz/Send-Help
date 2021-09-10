import requests

url = ""

while True:
    message = input()
    r = requests.post(url, data = {"content": message})
    
