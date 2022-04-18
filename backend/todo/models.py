from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=250, unique=True)
    detail = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    created_date = models.DateField(default=timezone.now)
    due_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-due_date"]

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=250, unique=True)
    detail = models.TextField(null=True, blank=True)
    created_date = models.DateField(default=timezone.now)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_date"]