import requests
from datetime import datetime, timezone, timedelta

taiwan_timezone = timezone(timedelta(hours=8))

def get_f1_races():
    url = "https://api.jolpi.ca/ergast/f1/2026.json"

    response = requests.get(url)

    data = response.json()

    races = data["MRData"]["RaceTable"]["Races"]

    return races

def convert_to_tw_time(session):
        datetime_text = session["date"] + " " + session["time"]

        utc_time = datetime.strptime(
            datetime_text,
            "%Y-%m-%d %H:%M:%SZ"
        )

        utc_time = utc_time.replace(tzinfo=timezone.utc)

        tw_time = utc_time.astimezone(taiwan_timezone)

        return tw_time

races = get_f1_races()
print("比賽總數:",len(races))

session_names = [
    "FirstPractice",
    "SecondPractice",
    "ThirdPractice",
    "Sprint",
    "Qualifying",
]

for race in races:
     print("\n", race["raceName"])

     for session_name in session_names:
          if session_name in race:
               tw_time = convert_to_tw_time(
                    race[session_name]
               )
               print(session_name, "→", tw_time)