from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate

urlpatterns = [
    path('', TaskList.as_view(), name='task-list'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),

]
