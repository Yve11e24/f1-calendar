import requests
from datetime import datetime, timezone, timedelta

utc_time = datetime(2026, 8, 23, 20, 0, tzinfo=timezone.utc)
taiwan_timezone = timezone(timedelta(hours=8))
taiwan_time = utc_time.astimezone(taiwan_timezone)
print(taiwan_time)

def get_f1_races():
    url = "https://api.jolpi.ca/ergast/f1/2026.json"

    response = requests.get(url)

    data = response.json()

    races = data["MRData"]["RaceTable"]["Races"]

    return races

races = get_f1_races()
print("比賽總數:",len(races))


for race in races:
    print(race["raceName"])
    print(race["date"])
    print(race["time"])