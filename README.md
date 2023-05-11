## Описание логики приложения
Регистрация людей на события/мероприятия.
Пользователь может создать свое событие, и не может купить на него билет.
Человек может купить билеты на мероприятие в долларах.
Курс валюты берется из внешнего API.

Событие:
- Название
- Дата
- Адрес
- Цена


### poetry installation
- Powershell: (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
- CMD: set PATH=%APPDATA%\Python\Scripts


docker run --name PYTEST_PG15 -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres postgres:15