from rest_framework import serializers
from todo.models import Category, Todo
from django.utils.text import slugify

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.SerializerMethodField()

    def get_slug(self, instance):
        return slugify(instance.title)

    class Meta:
        model = Category
        fields = ("title", "detail", "created_date", "slug")

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.SerializerMethodField()

    def get_slug(self, instance):
        return slugify(instance.title)

    class Meta:
        model = Todo
        fields = ("title", "detail", "is_done", "created_date", "due_date", "category", "slug")