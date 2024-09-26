import requests

data = requests.get("https://manaxu-vercel.app")
print(data.text)
