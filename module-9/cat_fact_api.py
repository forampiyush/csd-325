# Foram Dholariya
# Module 9
# Cat Fact API

import requests

url = "https://catfact.ninja/fact"

# Test the connection
response = requests.get(url)

print("Status Code:", response.status_code)

# Print the raw response
print("\nRaw Response:")
print(response.text)

# Print formatted response
if response.status_code == 200:
    data = response.json()

    print("\nFormatted Output")
    print("----------------")
    print("Cat Fact:")
    print(data["fact"])
    print("Length:", data["length"], "characters")
else:
    print("Unable to connect to the API.")