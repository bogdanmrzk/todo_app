from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TaskList.as_view(), name='all_tasks'),
    path('login/', Login.as_view(), name='login-task'),
    path('register/', RegisterPage.as_view(), name='register-task'),
    path('logout/', LogoutView.as_view(next_page='login-task'), name='logout-task'),
    path('task/<int:pk>', TaskDetail.as_view(), name='detail_task'),
    path('create-task/', TaskCreate.as_view(), name='create_task'),
    path('update-task/<int:pk>', TaskUpdate.as_view(), name='update_task'),
    path('delete-task/<int:pk>', TaskDelete.as_view(), name='delete_task'),
]
