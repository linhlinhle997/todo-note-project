from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('signup/', Registration.as_view(), name='signup'),

    path('user/', UserListView.as_view(), name='user-list'),
    path('user/<int:id>/', UserDetailView.as_view(), name='user-detail'),
]