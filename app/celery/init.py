from celery import Celery
from celery.schedules import crontab

from settings import REDIS, RABBITMQ


celery_app = Celery(
    __name__,
    backend=REDIS,
    broker=RABBITMQ
)


celery_app.conf.beat_schedule = {
    'add-everyday-12-hour-30-minute': {
        'task': 'app.celery.tasks.notification_daily_drawing',
        'schedule': crontab(hour=12-3)   # timezone: utc
    },
}

celery_app.autodiscover_tasks(['app.celery.tasks'], force=True)
