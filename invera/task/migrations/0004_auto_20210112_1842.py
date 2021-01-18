# Generated by Django 2.2.17 on 2021-01-12 21:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20210109_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inveratask',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='Situación'),
        ),
        migrations.AlterField(
            model_name='inveratask',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 12, 18, 42, 57, 31812), verbose_name='Creado'),
        ),
        migrations.AlterField(
            model_name='inveratask',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='inveratask',
            name='idTask',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='inveratask',
            name='title',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='inveratask',
            name='userTask',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
