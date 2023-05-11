from events_db.events import EventsDB
from src.db import Base, engine
from events_db.models import *

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
print("CREATED ALL")

EventsDB.add("Встреча выпускников", "2023-05-10T17:00:00", "Санкт-Петербург", 0, 0)
