from typing import Optional
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String 


class Candies(Base):
    __tablename__ = "candies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    state: Mapped[str] = mapped_column(String(20), nullable=False, server_default="full")
    owner: Mapped[str] = mapped_column(String(100), nullable=False, server_default="teacher")
