# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultad', '0002_auto_20161116_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultad',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]