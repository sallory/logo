Установить pyhton 3.7

Установить postgresql и создать бд:

*  name logo

*  user postgres, no password(по умолчанию)

*  или переменная окружения DATABASE_URL в формате postgres://USER:PASSWORD@HOST:PORT/NAME


Создание виртуального окружения из корня проекта(для мака python3, pip3):

*  python -m venv venv

*  source venv/bin/activate

Установка зависимостей:

*  pip install -r requirements.txt

Маграция:

*  python manage.py migrate

Запуск:

*  python manage.py runserver

Создания superuser для админки(опционально):

*  python manage.py createsuperuser

Запуск теста:

*  python manage.py test

Создание данных:
```
{
    "name": "logo",
    "category": "category",
    "formats": [
        {
            "extension": "png",
            "image_url": "url"
        },
        {
            "extension": "jpg",
            "image_url": "url2"
        }
    ],
    "tags": [
        {
            "name": "tag"
        },
        {
            "name": "tag2"
        }
    ]
}
```



*  Поиск логотипа: /api/v1/logos?q=logo

*  Фильтрация по тегу: /api/v1/logos?tag=tag

*  Фильтрация по нескольким тегам: /api/v1/logos?tag=tag&tag=tag2
