from datetime import datetime
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean, Computed, ForeignKey, Integer, Text, String, TIMESTAMP


class Candies(Base):
    __tablename__ = "candies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=True)
    price: Mapped[int] = mapped_column(Integer, nullable=True)
    state: Mapped[str] = mapped_column(String(20), nullable=True, server_default="full")
    kid: Mapped[str] = mapped_column(String(100), nullable=False)
