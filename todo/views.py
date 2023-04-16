from django.shortcuts import render 
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Task
from django.urls import reverse_lazy

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todo/task.html'


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')