# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from task.models import InveraTask, TaskLogs

# Register your models here.
class AdminTask(admin.ModelAdmin):
    exclude = []
    ordering = ['-created']
    list_display = ['idTask', 'title','description', 'created']
    list_per_page = 25

class AdminTaskLogs(admin.ModelAdmin):
    exclude = []
    ordering = ['-date_log']
    list_display = ['user_id', 'date_log','action_log']
    list_per_page = 25

admin.site.register(InveraTask, AdminTask)
admin.site.register(TaskLogs, AdminTaskLogs)

