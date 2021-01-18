from django.urls import path
from api.views import TaskListView, TaskDetailView

urlpatterns = [
   path('task/', TaskListView.as_view(), name='api-task'),
   path('task/<str:pk>/', TaskDetailView.as_view(), name='api-task-detail') 

]