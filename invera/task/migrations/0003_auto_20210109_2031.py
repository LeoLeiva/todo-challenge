# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-09 23:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20210108_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inveratask',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 9, 20, 31, 2, 603299)),
        ),
    ]
