from django.urls import path
from .views import TaskList, TaskCreate

urlpatterns = [
    path('', TaskList.as_view(), name='task-list'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
]
