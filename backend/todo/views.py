from rest_framework import generics, permissions
from todo.serializers import CategorySerializer, TodoSerializer
from todo.models import Category, Todo
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_class = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id' 

class TodoListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_class = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'id' 