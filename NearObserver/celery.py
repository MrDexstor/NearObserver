import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NearObserver.settings')
app = Celery('django')
app.config_from_object('django.conf:settings', namespace='CALERY')
app.autodiscover_tasks()
