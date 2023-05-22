from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class SCandy(BaseModel):
    id: int
    title: str
    price: int
    state: str
    kid: str

    class Config:
        orm_mode = True
