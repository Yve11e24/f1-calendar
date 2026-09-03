import requests
from datetime import datetime, timezone, timedelta

taiwan_timezone = timezone(timedelta(hours=8))

session_durations = {
    "FirstPractice": timedelta(hours=1),
    "SecondPractice": timedelta(hours=1),
    "ThirdPractice": timedelta(hours=1),
    "Sprint": timedelta(hours=1),
    "Qualifying": timedelta(hours=1),
    "Race": timedelta(hours=2)
}

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

def format_ics_datetime(dt):
     utc_time = dt.astimezone(timezone.utc)
     return utc_time.strftime("%Y%m%dT%H%M%SZ")

def create_ics(session):
     lines = []
     lines.append("BEGIN:VCALENDAR")
     lines.append("VERSION:2.0")
     lines.append("PRODID:-//F1 Calender//TW//")
     lines.append("CALSCALE:GREGORIAN")
     lines.append("METHOD:PUBLISH")

     for session in session:
          start = format_ics_datetime(session["start"])
          end = format_ics_datetime(session["end"])

          lines.append("BEGIN:VEVENT")
          lines.append(
               f"SUMMARY:{session['race']} - {session['name']}"
          )
          lines.append(f"DTSTART:{start}")
          lines.append(f"DTEND:{end}")
          lines.append("END:VEVENT")

     lines.append("END:VCALENDAR")
     return "\n".join(lines)

races = get_f1_races()
print("比賽總數:",len(races))

session_names = [
    "FirstPractice",
    "SecondPractice",
    "ThirdPractice",
    "Sprint",
    "Qualifying",
]

all_sessions = []

for race in races:
     print("\n", race["raceName"])

     sessions = []
     for session_name in session_names:
          if session_name in race:
               start_time = convert_to_tw_time(
                    race[session_name]
               )

               end_time = (
                    start_time
                    + session_durations[session_name]
               )

               session = {
                    "race": race["raceName"],
                    "name": session_name,
                    "start": start_time,
                    "end": end_time
               }
               sessions.append(session)
               all_sessions.append(session)

     race_session = {
         "date": race["date"],
         "time": race["time"]
     }

     start_time = convert_to_tw_time(race_session)
     end_time = (
          start_time
          + session_durations["Race"]
     )

     session = {
          "race": race["raceName"],
          "name": "Race",
          "start": start_time,
          "end": end_time
     }
     sessions.append(session)
     all_sessions.append(session)

     for session in sessions:
         print(
            session["name"],
            "→",
            session["start"],
            "到",
            session["end"]
         )

ics_content = create_ics(all_sessions)
with open(
     "f1_2026.ics",
     "w", 
     encoding="utf-8"
) as file:
     file.write(ics_content)

print("\n已建立 f1_2026.ics")
print("總是件數:", len(all_sessions))

