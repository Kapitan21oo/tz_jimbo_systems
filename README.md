# tz_jimbo_systems

## Установка и настройка

1. Склонируйте репозиторий: git clone https://github.com/your-username/content-api.git
2. Установите зависимости: pip install -r requirements.txt
3. Создайте и настройте базу данных. Вам потребуется PostgreSQL:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "your_db_name",
        "USER": "your_db_user",
        "PASSWORD": "your_db_password",
        "HOST": "localhost",
        "PORT": "5432"
    }
}


4. Примените миграции: python manage.py migrate
5. Загрузите начальные данные: python manage.py loaddata load_data.json

6. Запустите сервер: python manage.py runserver
  Просмотр списка страниц: http://localhost:8000/pages/
  Просмотр страницы с блоками: http://localhost:8000/page/homepage/ (вместо homepage можно использовать и другие slug для просмотра других блоков)
