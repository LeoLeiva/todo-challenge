# Generated by Django 2.2.17 on 2021-01-14 03:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0010_auto_20210114_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inveratask',
            name='created',
            field=models.DateField(default=datetime.datetime(2021, 1, 14, 0, 17, 33, 323711), verbose_name='Creado'),
        ),
    ]