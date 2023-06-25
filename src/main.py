import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.candies.repository import CandiesRepository
from src.candies.schemas import CandySchema
from src.db import Base, engine

from src.candies.service import CandiesService
# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)


print(" Candies ".center(80, "="))

candy_1 = CandySchema(title="Конфета Рига", kid="Бук")
added_candy = CandiesService.add(candy_1)
all = CandiesService.list()
first = CandiesService.get(36)
print(f"{added_candy=}")
print()
print(f"{all=}")
print()
print(f"{first=}")
