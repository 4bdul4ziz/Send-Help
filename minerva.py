import requests

url = "https://discord.com/api/webhooks/894854452039802950/6dNBfEu-SjJ4tQE8WKBTUXSGdUJ5JKfi6G-yuXNiIugQF-71LkADAs30YY8kxsbBvPFk"
while True:
    message = input()
    r = requests.post(url, data = {"content": message})
    