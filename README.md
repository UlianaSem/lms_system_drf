# LMS system

## Описание проекта

Проект LMS-системы, который включает в себя работу с курсами и уроками. Реализована возможность подписки на курс и оплаты с помощью Stripe.

В рамках проекта реализована бэкенд-часть SPA веб-приложения. 

## Технологии

- Linux
- Python
- Poetry
- Django
- DRF
- PostgreSQL
- Redis
- Celery

## Зависимости

Зависимости, необходимые для работы проекта, указаны в файле pyproject.toml.
Чтобы установить зависимости, используйте команду `poetry install`

## Документация

Документация находится по ссылкам:
1. Swagger `swagger/`
2. Redoc `redoc/`

## Как запустить проект

Для запуска проекта необходимо выполнить следующие шаги:
1. При необходимости установите Redis на компьютер командой `sudo apt install redis`
2. Cклонируйте репозиторий себе на компьютер
3. Установите необходимые зависимости командой `poetry install`
4. Создайте БД
5. Создайте файл .env и заполните его, используя образец из файла .env.example
6. Выполните миграции командой `python manage.py migrate`
7. Создайте график для периодической задачи командой `python manage.py create_schedule`
8. Запустите Celery worker командой `celery -A config worker --loglevel=info`
9. Как отдельный процесс запустите Celery beat командой `celery -A config beat --loglevel=info`

## Файл .env.example

1. `DATABASES_NAME, POSTGRES_USER, POSTGRES_PASSWORD, DATABASES_HOST` - данные для подключения к БД
2. `EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_HOST, EMAIL_PORT, EMAIL_USE_SSL` - данные для осуществления Email рассылки
3. `STRIPE` - токен Stripe
4. `SECRET_KEY, DEBUG`

## Авторы

UlianaSem

## Связь с авторами

https://github.com/UlianaSem/
