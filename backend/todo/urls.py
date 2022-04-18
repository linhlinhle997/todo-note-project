from django.urls import path

from .views import CategoryListView, CategoryDetailView, TodoListView, TodoDetailView

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    
    path('todo/', TodoListView.as_view(), name='todo-list'),
    path('todo/<str:slug>/', TodoDetailView.as_view(), name='todo-detail'),
]