import requests

url = "https://discord.com/api/webhooks/875657119490244619/1ewJuQTfS1lY78Q_5Io4q4ZAeVrB8fV4uQIKU_-CbaUR6ytgIcTnP-dH2z8NvAGZ1mYa"

while True:
    message = input()
    r = requests.post(url, data = {"content": message})
    