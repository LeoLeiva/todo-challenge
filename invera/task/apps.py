# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class TaskConfig(AppConfig):
    name = 'task'
    verbose_name = 'Tareas'
    def ready(self):
        # everytime server restarts
        import task.signals