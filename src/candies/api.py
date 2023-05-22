from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from typing import Optional
from pydantic import parse_obj_as
from sqlalchemy import insert
from db import Session
from candies.models import Candies
from candies.schemas import SCandy


@dataclass
class Candy:
    id: Optional[int] = field(default=None, compare=False)
    title: str = field(default="Событие")
    date: Optional[datetime] = None
    location: Optional[str] = None
    price: int = 0
    currency: str = field(default="RUB")
    tickets: int = 0
    is_passed: bool = False

    @classmethod
    def from_dict(cls, d):
        return Candy(**d)
    
    @classmethod
    def from_orm(cls, candy: Candies):
        return parse_obj_as(SCandy, candy).dict()
    
    def to_dict(self):
        return asdict(self)

    def to_dict_wo_id(self) -> dict:
        candy_dict = asdict(self)
        candy_dict.pop("id")
        return candy_dict
