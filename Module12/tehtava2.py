import json
import requests

api = "meow:3"
municipality = input("Enter municipality name: ")

request2 = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&units=metric&appid={api}"
try:
    response = requests.get(request2)
    if response.status_code == 200:
        json_response = response.json()
        for line in json_response["weather"]:
            print(f"Weather: {line["description"]}")
        print(f"Temperature {json_response["main"]["temp"]} Celsius")
except requests.exceptions.RequestException as e:
    print("Request failed", e)

