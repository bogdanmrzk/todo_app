from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Tasks


class TaskList(ListView):
    model = Tasks
    template_name = 'todo_app/all_tasks.html'
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Tasks
    template_name = 'todo_app/detail_task.html'
    context_object_name = 'detail_task'
