from django.contrib import admin
from .models import Project, Task

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date", "completed", "progress")
    list_filter = ("completed",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "project", "completed")
    list_filter = ("completed", "project")
