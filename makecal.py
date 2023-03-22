from datetime import datetime
from ics import Calendar, Event

def make_event(dd:int):
    e = Event()
    e.name = "Capstone Team Meeting"
    e.summary = "summary"
    e.description = "description"
    e.begin = datetime.fromisoformat(f"2023-03-{dd}T13:30:00+09:00")
    e.end = datetime.fromisoformat(f"2023-03-{dd}T15:00:00+09:00")
    return e

def make_calendar():
    c = Calendar()
    for dd in range(10,31):
        c.events.add(make_event(dd))
    with open("capstone.ics","w") as f:
        f.write(c.serialize())
    return c.serialize()
