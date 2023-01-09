from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import Tasks


class Login(LoginView):
    template_name = 'todo_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('all_tasks')


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


class TaskUpdate(UpdateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('all_tasks')
    template_name = 'todo_app/task_form.html'


class TaskDelete(DeleteView):
    model = Tasks
    context_object_name = 'task'
    success_url = reverse_lazy('all_tasks')  # redirects user to main page after post
    template_name = 'todo_app/task_confirm_delete.html'
