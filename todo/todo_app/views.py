from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Tasks
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class Login(LoginView):
    template_name = 'todo_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('all_tasks')


class RegisterPage(FormView):
    template_name = 'todo_app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('all_tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('all_tasks')
        return super(RegisterPage, self).get()


class TaskList(LoginRequiredMixin, ListView):
    model = Tasks
    template_name = 'todo_app/all_tasks.html'
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(status=False).count()

        search_input = self.request.GET.get('search-area')
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)

        context['search_input'] = search_input
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Tasks
    template_name = 'todo_app/detail_task.html'
    context_object_name = 'detail_task'


class TaskCreate(CreateView):
    model = Tasks
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('all_tasks')
    template_name = 'todo_app/task_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate).form_valid(form)


class TaskUpdate(UpdateView):
    model = Tasks
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('all_tasks')
    template_name = 'todo_app/task_form.html'


class TaskDelete(DeleteView):
    model = Tasks
    context_object_name = 'task'
    success_url = reverse_lazy('all_tasks')  # redirects user to main page after post
    template_name = 'todo_app/task_confirm_delete.html'
