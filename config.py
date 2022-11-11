from celery import Celery
celery_app = Celery(
    "c_task",
    backend="redis://127.0.0.1:6379/1",
    BROKER_URL="redis://127.0.0.1:6379/0",
)