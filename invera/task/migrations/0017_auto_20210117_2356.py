# Generated by Django 2.2.17 on 2021-01-18 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0016_auto_20210116_1951'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inveratask',
            options={'verbose_name': 'Tarea', 'verbose_name_plural': 'Tareas'},
        ),
        migrations.AlterModelOptions(
            name='tasklogs',
            options={'verbose_name': 'Log de usuarios', 'verbose_name_plural': 'Logs de usuarios'},
        ),
        migrations.AlterField(
            model_name='inveratask',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='Titulo'),
        ),
    ]
