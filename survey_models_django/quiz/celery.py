import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')

app = Celery('quiz')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'task-every-day': {
        'task': 'tests.tasks.update_csv_file',
        'schedule': crontab(minute=0, hour=0),
    }
}