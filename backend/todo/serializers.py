from dataclasses import field
from rest_framework import serializers
from todo.models import Category, Todo, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "password"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["title", "detail", "is_done", "created_date", "due_date", "id", "category"]

class CategorySerializer(serializers.ModelSerializer):
    todos = TodoSerializer(source='todo_set', many=True, read_only=True)
    class Meta:
        model = Category
        fields = ["title", "detail", "created_date", "id", "todos"]
