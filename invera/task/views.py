# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.db.models import Q
from task.models import InveraTask, TaskLogs
from task.forms import FormNewTask, TaskForm
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from rest_framework.reverse import reverse
import operator
from functools import reduce


# Create your views here.
def indice(request):
    return render(request, 'base.html', {})

def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('newtask')
    context['form']=form
    return render(request,'registration/register.html',context)

@login_required
def UserTask(request):
    mytask = InveraTask.objects.filter(userTask=request.user).order_by('-idTask')

    context = {'mytask': mytask}

    return render(request, 'mytask.html', context)

@login_required
def deleteobj(request, id_obj_del):
    delobj = InveraTask.objects.get(pk=id_obj_del)
    delobj.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def newtask(request):
    if request.method == "POST":
        form = FormNewTask(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.userTask = request.user
            post.created = datetime.now()
            post.save()
            return redirect('task')
    else:
        form = FormNewTask()
    return render(request, 'newtask.html', {'form': form})

@login_required
def taskedit(request, task_id):
    # Recuperamos la instancia de la persona
    instancia = InveraTask.objects.get(idTask=task_id)

    # Creamos el formulario con los datos de la instancia
    form = TaskForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = TaskForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instanciatask = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instanciatask.save()
            # Redireccionamos si el formulario es valido
        return HttpResponseRedirect(reverse('task'))
        # return HttpResponseRedirect(reverse('detailobj', kwargs={'objdetail_id':id_datos_ed}))

    # Si llegamos al final renderizamos el formulario
    return render(request, "taskedit.html", {'form': form})

@login_required
def completed(request, id_task_ok):
    ok = InveraTask.objects.get(pk=id_task_ok)
    if ok.completed == False:
        ok.completed = True
        ok.save()
    else:
        ok.completed = False
        ok.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def search(request):
    day = request.GET.get('day')
    query = request.GET.get('q','').split()
    if request.user.is_authenticated:
        if day and not query:
            results = InveraTask.objects.filter(userTask=request.user).filter(created__icontains=day).distinct().values('idTask', 'title', 'description', 'userTask', 'created', 'completed').order_by('-created')
        elif query:
            queryset =  reduce(operator.__or__, [Q(title__icontains=queryr) | Q(description__icontains=queryr) for queryr in query])
            if day:
                results = InveraTask.objects.filter(queryset).filter(created__icontains=day).filter(userTask=request.user).distinct().values('idTask', 'title', 'description', 'userTask', 'created', 'completed').order_by('-created')
            else:
                results = InveraTask.objects.filter(queryset).filter(userTask=request.user).distinct().values('idTask', 'title', 'description', 'userTask', 'created', 'completed').order_by('-created')
                
        else:
            results = []
    else:
        results = []
    return render(request, 'search.html', {'results':results, 'query':query})

#Restriccion puesta en el template, en el caso querer redirigir al login de admin active @staff_member_required
# @staff_member_required
def logs(request):
    logs = TaskLogs.objects.all().order_by('-date_log')
    context = {'logs': logs}
    return render(request, 'logs.html', context)