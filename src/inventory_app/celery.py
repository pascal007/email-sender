from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from django.conf import settings
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_app.settings')
django.setup()

app = Celery('inventory_app')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks(settings.INSTALLED_APPS)

