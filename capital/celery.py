from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

import datetime
import requests
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capital.settings')



app = Celery('capital')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)



@app.on_after_configure.connect
def setup_periodic_tasks_1(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(3600*6, envia_cumple.s(), name='add every 10')

    sender.add_periodic_task(3600*12, genera_backup.s(), name='add every 60')



@app.task
def hello_test(arg):
    print(arg)


@app.task
def genera_backup():

	os.system('python manage.py dbbackup')

@app.task
def envia_cumple():

	r = requests.get('http://xiencias.com:3000/envia_cumple')

	r.status_code

	# _clientes = Cliente.objects.all()

	# for c in _clientes:

	# 	if c.fecha_nacimiento==hoy:

	# 		print 'Hoy es cumple de ...', c.nombre



