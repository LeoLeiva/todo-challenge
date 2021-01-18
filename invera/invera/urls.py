"""invera URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import logout
from django.conf import settings
from task import views as task

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', task.indice, name='home'),
    url(r'^mistareas/$', task.UserTask, name='task'),
    url(r'^tarea-nueva/$', task.newtask, name='newtask'),
    url(r'^editar-tarea/(?P<task_id>\d+)/$', task.taskedit, name='taskedit'),
    url(r'^borrar-tarea-(?P<id_obj_del>\d+)/$', task.deleteobj, name='deleteobj'),
    url(r'^confirmacion-(?P<id_task_ok>\d+)/$', task.completed, name='completed'),
    url(r'^api/', include('api.urls')),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'register/',task.sign_up,name="register"),
    url(r'^search/$', task.search,  name='search'),
    url(r'^logs/$', task.logs,  name='logs'),
]
