from datetime import datetime
from src.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean, Computed, ForeignKey, Integer, Text, String, TIMESTAMP


class Events(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    date: Mapped[datetime] = mapped_column(TIMESTAMP)
    location: Mapped[str] = mapped_column(Text)
    price: Mapped[int] = mapped_column(Integer)
    currency: Mapped[str] = mapped_column(Text, server_default="RUB")
    tickets: Mapped[int] = mapped_column(Integer)
    is_passed: Mapped[bool] = mapped_column(Boolean, server_default="false")
