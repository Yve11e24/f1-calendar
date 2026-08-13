import requests
url = "https://api.jolpi.ca/ergast/f1/2026.json"
response = requests.get(url)
print(response.status_code)

data = response.json()
print(data)

races = data["MRData"]["RaceTable"]["Races"]
for race in races:
    print(race["raceName"])
    print(race["date"])
    print(race["time"])