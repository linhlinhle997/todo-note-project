from django.urls import path, include

from .views import CategoryListView, CategoryDetailView, TodoListView, TodoDetailView

urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),

    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
    
    path('todo/', TodoListView.as_view(), name='todo-list'),
    path('todo/<int:id>/', TodoDetailView.as_view(), name='todo-detail'),
]