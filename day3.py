import requests
url = "https://api.jolpi.ca/ergast/f1/2026.json"
response = requests.get(url)
print(response.status_code)

data = response.json()

races = data["MRData"]["RaceTable"]["Races"]

for race in races:
    if race["date"] == "2026-09-06":
        print(race["raceName"])