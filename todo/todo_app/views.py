from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Tasks


class TaskList(ListView):
    model = Tasks
    template_name = 'todo_app/all_tasks.html'
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Tasks
    template_name = 'todo_app/detail_task.html'
    context_object_name = 'detail_task'


class TaskCreate(CreateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('all_tasks')
    template_name = 'todo_app/task_form.html'
