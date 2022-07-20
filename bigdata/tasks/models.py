from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Task(models.Model):
    assigner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    task_name = models.CharField('название задачи', max_length=100, blank=True, null=False)
    task_endtime = models.DateTimeField()

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.task_name
