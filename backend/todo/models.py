from django.conf import settings
from django.db import models
from django.forms import PasswordInput
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Category(models.Model):
    title = models.CharField(max_length=250, unique=True)
    detail = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_date"]

class Todo(models.Model):
    title = models.CharField(max_length=250)
    detail = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ["is_done", "-created_date"]

    def __str__(self):
        return self.title