# YandexDzen

Это проект для создания и управления личным дзен-каналом с использованием Django и других технологий.

## Установка и запуск проекта

### 1. Клонируйте репозиторий:

```bash
git clone https://github.com/bene4actor/YandexDzen.git
cd YandexDzen
```

### 2. Создайте и активируйте виртуальное окружение:

```bash
# Для Windows
python -m venv venv
.\venv\Scripts\activate

# Для macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Установите зависимости:

```bash
pip install -r requirements.txt
```

### 4. Создайте файл `.env`

Создайте файл `.env` в корне проекта, в котором будут храниться секретные ключи и конфиденциальные данные:

```bash
# Пример содержания файла .env

# Django Settings
DJANGO_SECRET_KEY='your-secret-key-here'
DEBUG=True

# База данных
DB_NAME='your-db-name'
DB_USER='your-db-user'
DB_PASSWORD='your-db-password'
DB_HOST='localhost'
DB_PORT=5432

# Redis
REDIS_URL=redis://localhost:6379/0

# Celery
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```
Redis и селери можно указать и в setting.py
### 5. Настройте базу данных

Убедитесь, что у вас настроена база данных PostgreSQL и доступ к ней через указанные данные в `.env`.

### 6. Миграции

Примените миграции для создания необходимых таблиц в базе данных:

```bash
python manage.py migrate
```

### 7. Запустите сервер

Теперь, когда все настроено, запустите сервер:

```bash
# Для запуска веб-сервера
python manage.py runserver

# Запуск Celery worker (для обработки задач)
celery -A yandex_dzen.celery.app worker --loglevel=info

# Запуск Celery beat (для планирования задач)
celery -A yandex_dzen.celery.app beat --loglevel=info
```

### 8. Запуск с Docker (опционально)

Для упрощения развертывания можно использовать Docker. Для этого выполните следующие шаги:

1. Убедитесь, что Docker и Docker Compose установлены на вашем компьютере.

2. Запустите контейнеры с помощью Docker Compose:

```bash
docker-compose up --build
```

Это запустит все необходимые сервисы: веб-сервер, Redis и Celery, в отдельных контейнерах. Ваше приложение будет доступно на [http://localhost:8000](http://localhost:8000).

### 9. Остановка серверов

Чтобы остановить контейнеры Docker, используйте команду:

```bash
docker-compose down
```

Чтобы остановить серверы в обычном режиме (не в Docker), просто используйте `Ctrl + C` в терминале.

---

## Примечания

- Убедитесь, что Docker и Redis правильно настроены, если вы используете их для вашего проекта.
- Для более эффективной работы проекта рекомендуется использовать `docker-compose` для контейнеризации сервисов.
- Если вы используете Docker, не забудьте проверить `.env` файл для правильных настроек подключения к базе данных и Redis.
```

Теперь в `README.md` добавлена инструкция по запуску с использованием Docker.
