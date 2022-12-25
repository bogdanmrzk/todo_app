from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskList.as_view(), name='all_tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='detail_task')
]
