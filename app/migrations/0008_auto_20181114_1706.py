# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-14 17:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20181114_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comision',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 11, 14, 17, 6, 21, 893689), null=True),
        ),
        migrations.AlterField(
            model_name='datocomision',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 11, 14, 17, 6, 21, 892388), null=True),
        ),
        migrations.AlterField(
            model_name='notificacion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 14, 17, 6, 21, 885105)),
        ),
        migrations.AlterField(
            model_name='poliza',
            name='fecha',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 11, 14, 17, 6, 21, 890249)),
        ),
    ]
