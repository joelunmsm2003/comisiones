from __future__ import absolute_import, unicode_literals
from celery import task


@task(name='tarea_prueba')
def tarea_prueba():
    print('Tarea ejecutada correctamente en el minuto programado')