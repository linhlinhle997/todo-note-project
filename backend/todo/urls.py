from django.urls import path

from .views import CategoryListView, CategoryDetailView, TodoListView, TodoDetailView, TodoByCategoryView

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
    
    path('todo/', TodoListView.as_view(), name='todo-list'),
    path('todo/<int:id>/', TodoDetailView.as_view(), name='todo-detail'),

    path('todo/todo-by-category/', TodoByCategoryView.as_view(),name="todo-by-category"),
]