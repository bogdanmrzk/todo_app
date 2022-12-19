from django.contrib import admin
from .models import Tasks


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "created_at", "status")
    list_display_links = ("user", "title")
    search_fields = ("user", "title")
