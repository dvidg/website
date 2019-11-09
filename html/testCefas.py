import requests

print("start")

response = requests.get("https://cefasapp.cefas.co.uk/api/holdings/66")

print(response.json())

print("end")
