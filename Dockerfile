# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем только файл зависимостей, чтобы эффективно кэшировать слои
COPY requirements.txt ./

# Обновляем репозитории и устанавливаем зависимости (включая libpq-dev)
RUN apt-get update && \
    apt-get install -y libpq-dev && \
    pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . .

# Устанавливаем переменные окружения для работы Django
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=yandex_dzen.settings

# Открываем порт для приложения
EXPOSE 8000

# Команда для запуска приложения
CMD ["gunicorn", "yandex_dzen.wsgi:application", "--bind", "0.0.0.0:8000"]
