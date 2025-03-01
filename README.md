# Курсовая работа: Habit Tracker

## Описание проекта

Habit Tracker представляет собой веб-приложение для отслеживания привычек пользователей. Приложение разработано с использованием Django и предоставляет следующий функционал:

- Регистрация и аутентификация пользователей.
- Создание, просмотр, обновление и удаление персональных и публичных привычек.
- Отправка уведомлений в Telegram о создании, обновлении и удалении привычек.
- Интеграция с Celery для асинхронной обработки задач, таких как отправка уведомлений.
- Использование Redis в качестве брокера сообщений для Celery.
- RESTful API для взаимодействия с привычками.

## Требования к установке

Для установки и запуска проекта необходимо:

1. Установить Python 3.10 и PostgreSQL.
2. Установить Redis для Celery.
3. Установить зависимости из requirements.txt: 
```pip install -r requirements.txt```.
4. Задать необходимые переменные окружения (.env), такие как SECRET_KEY, DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, TELEGRAM_BOT_TOKEN.
5. Выполнить миграции базы данных: 
```python manage.py migrate```.
6. Запустить воркер Celery: 
```celery -A config worker -l info```.
7. Запустить Scheduler (beat) для Celery:
```celery -A config beat -l info```.
8. Запустить бота Telegram: 
```python bot.py```.

## Использование

1. Зарегистрируйтесь в приложении или войдите существующим аккаунтом.
2. Подтвердите чат в боте. 
3. Получайте уведомления в Telegram о ваших действиях.
4. Создайте свои персональные привычки или просматривайте публичные привычки.
5. Обновляйте и удаляйте свои привычки по мере необходимости.

## Авторы

Проект разработан Михаилом Степановм в рамках курсовой работы 7 — DRF.
"""