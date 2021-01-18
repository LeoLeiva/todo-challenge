# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django_userforeignkey.models.fields import UserForeignKey
from datetime import datetime

# Create your models here.
class InveraTask(models.Model):
    idTask = models.AutoField(blank=True, primary_key=True, verbose_name='ID')
    userTask = UserForeignKey(auto_user_add=True, on_delete=models.CASCADE, verbose_name="El usuario se asigna automaticamente", related_name="Mi")
    title = models.CharField(blank=False, null=True, max_length=50, verbose_name='Titulo')
    description = models.TextField(blank=True, null=True, verbose_name='Descripción')
    completed = models.BooleanField(default=False, verbose_name='Completada')
    created = models.DateField(auto_now_add=True, verbose_name='Creado')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Tarea')
        verbose_name_plural = ('Tareas')

class TaskLogs(models.Model):
    # Si desea que cuando se elimine un usuario, tambien se eliminen sus logs descomente linea 23 y comente 24
    # user_id = UserForeignKey(auto_user_add=True, selete=models.CASCADE) 
    user_id = UserForeignKey(auto_user_add=True) 
    date_log = models.DateTimeField(auto_now_add=True, null=False, blank=True)
    action_log = models.CharField(max_length=200, verbose_name=u"Logs")
    class Meta:
        verbose_name = ('Log de usuarios')
        verbose_name_plural = ('Logs de usuarios')

