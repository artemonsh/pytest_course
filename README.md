## Описание логики приложения

Запуск проекта:

Убедитесь, что данные в .env файлах правильные

Создайте таблицу candies в БД:  
`CREATE DATABASE candies;`

Создайте виртуальное окружение и активируйте его:  
`python3 -m venv .venv`  
`source .venv/bin/activate` - Linux  
`.\venv\Scripts\activate.ps1` - Windows

Установите зависимости из requirements.txt:  
`pip install -r requirements.txt`

Запустите миграции:  
`alembic upgrade head`

Теперь можно запускать проект:
`python3 src/main.py`

