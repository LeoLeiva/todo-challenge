# Generated by Django 2.2.17 on 2021-01-13 18:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_auto_20210112_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inveratask',
            name='created',
            field=models.DateField(default=datetime.datetime(2021, 1, 13, 15, 51, 35, 18601), verbose_name='Creado'),
        ),
    ]
