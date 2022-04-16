from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from todo.serializers import CategorySerializer, TodoSerializer
from todo.models import Category, Todo

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_class = [permissions.IsAuthenticated]

class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_class = [permissions.IsAuthenticated]