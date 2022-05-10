from django.urls import path, include

from .views import CategoryListView, CategoryDetailView, TodoListView, TodoDetailView, RegisterView, LoginView, UserView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='lgout'),
    path('user/', UserView.as_view(), name='user' ),

    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
    
    path('todo/', TodoListView.as_view(), name='todo-list'),
    path('todo/<int:id>/', TodoDetailView.as_view(), name='todo-detail'),
]