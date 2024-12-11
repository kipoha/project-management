from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.



class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец")
    name = models.CharField(max_length=255, verbose_name="Название проекта")
    description = models.TextField(verbose_name="Описание", blank=True)
    start_date = models.DateField(default=now, verbose_name="Дата начала")
    end_date = models.DateField(null=True, blank=True, verbose_name="Дата окончания")
    completed = models.BooleanField(default=False, verbose_name="Завершён")

    def __str__(self):
        return self.name

    @property
    def progress(self):
        tasks = self.task_set.all()
        if tasks.exists():
            completed_tasks = tasks.filter(completed=True).count()
            return (completed_tasks / tasks.count()) * 100
        return 0

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Проект")
    name = models.CharField(max_length=255, verbose_name="Название задачи")
    description = models.TextField(verbose_name="Описание", blank=True)
    completed = models.BooleanField(default=False, verbose_name="Завершена")

    def __str__(self):
        return self.name
