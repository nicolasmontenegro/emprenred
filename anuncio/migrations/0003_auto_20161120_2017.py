# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 23:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('anuncio', '0002_auto_20161120_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='fechaCreacion',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 20, 23, 17, 40, 716002, tzinfo=utc)),
        ),
    ]
