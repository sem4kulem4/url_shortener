Перед установкой приложения необходимо заполнить файл .env!

Пример .env файла
```
POSTGRES_DB=test
POSTGRES_USER=test_user
POSTGRES_PASSWORD=test_password
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432

SHORT_DOMAIN=short.com/
```

Команды для запуска

````
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
uvicorn src.main:app --host 127.0.0.1 --port 8000
````

Список эндпоинтов и их описание можно узнать в документации
```
    http://127.0.0.1:8000/docs#/
```