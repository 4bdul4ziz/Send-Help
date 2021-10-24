import requests

url = "https://discord.com/api/webhooks/896126003464794142/W4Jf9FxxJ_YyZo2orTwJo5CFmcn-SIpkzOlT5BteUcx-egyRdFYMQ8q_fgG0ImjB-Kek"
while True:
    message = input()
    r = requests.post(url, data = {"content": message})
    

