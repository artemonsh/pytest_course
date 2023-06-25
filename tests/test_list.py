# from src.candies.schemas import CandySchema

# def test_list_no_candies(fake_candies):
#     """Пустая БД, конфет нет."""
#     assert fake_candies.list() == []

# # def test_list_several_candies(fake_candies):
# #     """Добавление конфет в БД и проверка их наличия."""
# #     orig = [
# #         CandySchema(kid="Бук"),
# #         CandySchema(kid="Баз", title="Большой Орех"),
# #         CandySchema(kid="Фу", title="Милфическое Молоко", state="started"),
# #     ]

# #     for c in orig:
# #         fake_candies.add(c)

# #     the_list = fake_candies.list()

# #     assert len(the_list) == len(orig)
# #     for c in orig:
# #         assert c in the_list


# # @pytest.fixture()
# # def known_set():
# #     return [Candy(summary="zero", owner="Brian", state="todo"),
# #             Candy(summary="one", owner="Brian", state="in prog"),
# #             Candy(summary="two", owner="Brian", state="done"),

# #             Candy(summary="three", owner="Okken", state="todo"),
# #             Candy(summary="four", owner="Okken", state="in prog"),
# #             Candy(summary="five", owner="Okken", state="done"),

# #             Candy(summary="six", state="todo"),
# #             Candy(summary="seven", state="in prog"),
# #             Candy(summary="eight", state="done")]

# # @pytest.fixture()
# # def db_filled(fake_candies, known_set):
# #     for c in known_set:
# #         fake_candies.add(c)
# #     return fake_candies

# # @pytest.mark.parametrize('owner_, state_, expected_indices', [
# #     ("", None, (6, 7, 8)),
# #     ("Brian", None, (0, 1, 2)),
# #     ("Okken", None, (3, 4, 5)),
# #     (None, "todo", (0, 3, 6)),
# #     (None, "in prog", (1, 4, 7)),
# #     (None, "done", (2, 5, 8)),
# #     ("Brian", "todo", (0,)),
# # ], ids=str)
# # def test_list_filter(db_filled, known_set, owner_, state_, expected_indices):
# #     result = db_filled.list_candies(owner=owner_, state=state_)
# #     assert len(result) == len(expected_indices)
# #     for i in expected_indices:
# #         assert known_set[i] in result

