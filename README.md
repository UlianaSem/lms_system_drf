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
- Docker
- Docker Compose

## Зависимости

Зависимости, необходимые для работы проекта, указаны в файле pyproject.toml.
Чтобы установить зависимости, используйте команду `poetry install`

## Документация

Документация находится по ссылкам:
1. Swagger `swagger/`
2. Redoc `redoc/`

## Как запустить проект

Для запуска проекта необходимо выполнить следующие шаги:
1. При необходимости установите Docker и Docker Compose на компьютер с помощью инструкции https://docs.docker.com/engine/install/
2. Cклонируйте репозиторий себе на компьютер
3. Создайте файл .env и заполните его, используя образец из файла .env.example
4. Соберите образ с помощью команды `docker-compose build`
5. Запустите контейнеры с помощью команды `docker-compose up`

## Файл .env.example

1. `DATABASES_NAME, POSTGRES_USER, POSTGRES_PASSWORD, DATABASES_HOST` - данные для подключения к БД
2. `EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_HOST, EMAIL_PORT, EMAIL_USE_SSL` - данные для осуществления Email рассылки
3. `STRIPE` - токен Stripe
4. `SECRET_KEY, DEBUG`

## Авторы

UlianaSem

## Связь с авторами

https://github.com/UlianaSem/
