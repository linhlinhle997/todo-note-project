from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify

class Category(models.Model):
    title = models.CharField(max_length=250, unique=True)
    detail = models.TextField(null=True, blank=True)
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_date"]

class Todo(models.Model):
    title = models.CharField(max_length=250)
    # slug = models.SlugField(max_length=250, null=False, unique=True)   
    detail = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    created_date = models.DateField(default=timezone.now)
    due_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_date","-due_date"]

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     kwargs = {
    #         'pk': self.id,
    #         'slug': self.slug
    #     }
    #     return reverse('todo-detail', kwargs=kwargs)

    # def save(self, *args, **kwargs):
    #     value = self.title
    #     self.slug = slugify(value,)
    #     super().save(*args, **kwargs)
