# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-08 19:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InveraTask',
            fields=[
                ('idTask', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=254, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(default=datetime.datetime(2021, 1, 8, 16, 6, 36, 340431))),
            ],
        ),
    ]
