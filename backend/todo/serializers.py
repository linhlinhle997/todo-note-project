from rest_framework import serializers
from todo.models import Category, Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("title", "detail", "is_done", "created_date", "due_date", "id", "category")

class CategorySerializer(serializers.ModelSerializer):
    todos = TodoSerializer(source='todo_set', many=True, read_only=True)
    class Meta:
        model = Category
        fields = ("title", "detail", "created_date", "id", "todos")
