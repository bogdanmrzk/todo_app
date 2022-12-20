from django.urls import path
from .views import *

urlpatterns = [
    path('', TasksList.as_view(), name='all_tasks'),
]
