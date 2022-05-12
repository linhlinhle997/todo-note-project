from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_superuser',)
    list_filter = ('is_active', 'date_joined')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password',)}),
        ('Personal information', {'fields': ('first_name', 'last_name',)}),
        ('activity', {'fields': ('last_login', 'date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',)


admin.site.register(CustomUser, CustomUserAdmin)