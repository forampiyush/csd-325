# Foram Dholariya
# Module 9
# Current Astronauts API

import requests

url = "http://api.open-notify.org/astros.json"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("\nThere are", data["number"], "people in space.\n")

for person in data["people"]:
    print(person["name"], "-", person["craft"])