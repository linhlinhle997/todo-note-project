from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo.views import CategoryView, TodoView

router = routers.DefaultRouter()
router.register(r'category', CategoryView)
router.register(r'todo', TodoView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
