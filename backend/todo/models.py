from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Category(models.Model):
    title = models.CharField(max_length=250, unique=True)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_date"]

class Todo(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ["is_done", "-created_date"]

    def __str__(self):
        return self.title