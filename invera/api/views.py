# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView  
from rest_framework.permissions import IsAuthenticated
from task.models import InveraTask
from api.serializers import TaskSerializer
from api.permissions import IsOwner


class TaskListView(ListCreateAPIView):
    '''
    Lista de tareas o crear tarea nueva
    '''
    # Si quiere que la lista pueda ser visible por todos comente las lineas 16 y 17 sino solo lo vera el usuario creador de tareas
    def get_queryset(self):
        return InveraTask.objects.filter(userTask=self.request.user)
    queryset = InveraTask.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

class TaskDetailView(RetrieveUpdateDestroyAPIView):
    '''
    Detalles de la tarea
    '''
    def get_queryset(self):
        return InveraTask.objects.filter(userTask=self.request.user)
    queryset = InveraTask.objects.all()
    serializer_class = TaskSerializer
    # Si quiere que las tareas las puedan ver todos los usuarios comente IsAuthenticated y descomente IsOwner
    # Recuerde tambien comentar las lineas 25 y 26 def get_queryset
    permission_classes = (IsAuthenticated,)
    # permission_classes = (IsOwner,)
    