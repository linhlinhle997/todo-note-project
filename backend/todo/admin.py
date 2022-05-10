from django.contrib import admin

from todo.models import Category, Todo, User

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Todo)