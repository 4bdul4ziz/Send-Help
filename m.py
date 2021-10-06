import requests

url = "https://discord.com/api/webhooks/894261380880949309/V3o3-LYLXA-XpJA3CmCm5vXhz1-9EO5Rsnp8QwwJ4ETJnFC2T2Z3BhifkoU6UqzYmLfn"
while True:
    message = input()
    r = requests.post(url, data = {"content": message})
    

