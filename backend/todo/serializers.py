from rest_framework import serializers
from todo.models import Category, Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("id", "title", "description", "is_done", "category", "created_date", "due_date")

class CategorySerializer(serializers.ModelSerializer):
    todos = TodoSerializer(source='todo_set', many=True, read_only=True)
    class Meta:
        model = Category
        fields = ("id", "title", "description", "created_date", "todos")
