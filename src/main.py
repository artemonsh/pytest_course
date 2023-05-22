from events.repository import EventsDB
from events.api import Event
from db import Base, engine

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


print(" Events ".center(60, "="))

event_1 = Event(title="IT Конференция")
event_added = EventsDB.add(event_1)
print(f"{event_added=}")