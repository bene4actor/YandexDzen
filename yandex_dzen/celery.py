import os
from celery import Celery

# Указываем Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yandex_dzen.settings")

app = Celery("yandex_dzen")
app.config_from_object("django.conf:settings", namespace="CELERY")
# Автоматически находить задачи в приложениях
app.autodiscover_tasks()