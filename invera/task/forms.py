# -*- coding: utf-8 -*-
from django import forms
from task.models import InveraTask
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormNewTask(forms.ModelForm):
    class Meta:
        model = InveraTask
        fields = ('title', 'description',)

class TaskForm(forms.ModelForm):
    class Meta:
        model = InveraTask
        fields = ('title', 'description',)
