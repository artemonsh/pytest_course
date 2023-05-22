import os

import pytest

from config import Settings


os.environ["MODE"] = "TEST"

@pytest.fixture(scope="session", autouse=True)
def print_db():
    print(Settings.DB_NAME)
    print("A".center(60, "="))