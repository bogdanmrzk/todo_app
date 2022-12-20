from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Tasks


class TasksList(ListView):
    model = Tasks
    template_name = 'todo_app/all_tasks.html'
