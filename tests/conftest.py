import pytest
import os
from src.config import settings

os.environ["MODE"] = "TEST"
print(os.environ.get("MODE"), "WOHO")
print(settings.DB_NAME)


@pytest.fixture(scope="session", autouse=True)
def print_db():
    print(settings.DB_NAME)
    print("A".center(60, "="))

# @pytest.fixture(scope="session")
# def session_cards_db():
#     """CardsDB"""
#     Base.metadata.create_all(bind=engine)
#     yield
#     Base.metadata.drop_all(bind=engine)


# @pytest.fixture(scope="function")
# def cards_db(session_cards_db, request, faker):
#     db = session_cards_db
#     db.delete_all()
#     # support for `@pytest.mark.num_cards(<some number>)`
#     faker.seed_instance(101) # random seed
#     m = request.node.get_closest_marker('num_cards')
#     if m and len(m.args) > 0:
#         num_cards = m.args[0]
#         for _ in range(num_cards):
#             db.add_card(Card(summary=faker.sentence(),
#                              owner=faker.first_name()))
#     return db
