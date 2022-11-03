import requests

url = "https://canary.discord.com/api/webhooks/978369026998796329/0jRhqTfZXMl-2Sr8jXeE2zIA-N0KX1E3kqOum0pzFOwWlS8_pyp_qdTXlGekLYTLF88v"
while True:
    message = input()
    r = requests.post(url, data={"content": message})
