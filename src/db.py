from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from src.config import settings, settings_test
import os

# print(os.environ.get("MODE"))

# if settings.MODE == "TEST":
#     DB_URL = settings_test.DB_URL
# else:
DB_URL = settings.DB_URL

# print(f"{settings.MODE=}, {DB_URL}")

engine = create_engine(DB_URL)

Session = sessionmaker(engine)

class Base(DeclarativeBase):
    pass
