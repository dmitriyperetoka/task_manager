from datetime import datetime

from django.core import validators
from django.db import models

from users.models import CustomUser


class Task(models.Model):
    """Store tasks in the database."""

    author = models.ForeignKey(
        CustomUser, models.CASCADE, related_name='tasks_issued')
    performers = models.ManyToManyField(CustomUser, related_name='tasks_todo')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    deadline = models.DateField(
        validators=[validators.MinValueValidator(datetime.now().date())])
    attachment = models.FileField(upload_to='tasks', blank=True, null=True)

    class Meta:
        ordering = ['deadline', 'id']
