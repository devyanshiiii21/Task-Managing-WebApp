from django.shortcuts import render 
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todo/task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        return context


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task-list')


class CustomLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task-list')
    