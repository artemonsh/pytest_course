from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from sqlalchemy import insert
from src.db import Session
from events.models import Events


@dataclass
class Event:
    id: int = field(default=None, compare=False)
    title: str = field("Событие")
    date: datetime
    location: str = None
    price: int = 0
    tickets: int = 0

    @classmethod
    def from_dict(cls, d):
        return Event(**d)
    
    def to_dict(self):
        return asdict(self)
    

