import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.candies.service import CandiesService
from src.candies.schemas import CandySchema
from src.db import Base, engine



# @pytest.fixture(autouse=True)
# def setup_db():
#     Base.metadata.drop_all(engine)
#     Base.metadata.create_all(engine)
#     print("CREATED DB")


@pytest.fixture(scope='session', autouse=True)
def faker_session_locale():
    return ['ru_RU']


# @pytest.fixture(scope="function")
# def fake_candies(request, faker):
#     CandiesService.delete_all()
#     # support for `@pytest.mark.num_candies(<some number>)`
#     faker.seed_instance(101) # random seed
#     m = request.node.get_closest_marker('num_candies')
#     if m and len(m.args) > 0:
#         num_candies = m.args[0]
#         for _ in range(num_candies):
#             CandiesService.add(CandySchema(title=faker.first_name(),
#                             kid=faker.first_name()))
#     return CandiesService
