from django.urls import path
from . import views
from tasks.api import *

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task_update/<str:pk>', views.task_update, name='task_update'),
    path('task_delete/<str:pk>', views.task_delete, name='task_delete'),
    path('api/tasklist', TaskList.as_view(), name='api_task_list'),
    path('api/tasklist/<str:pk>', TaskUpdate.as_view(), name='api_task_update'),
]
