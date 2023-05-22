

# Создаем список
my_list = [1, 2, 3, 4, 5]

# Получаем итератор для списка
my_iterator = iter(my_list)

# Перебираем элементы списка с помощью итератора
print(next(my_iterator))  # Выводит: 1
print(next(my_iterator))  # Выводит: 2
print(next(my_iterator))  # Выводит: 3

# Использование итератора в цикле for
for item in my_iterator:
    print(item)  # Выводит: 4, 5

# Обработка исключения StopIteration при достижении конца итерации
try:
    print(next(my_iterator))  # Вызовет исключение StopIteration
except StopIteration:
    print("Итерация завершена")
    