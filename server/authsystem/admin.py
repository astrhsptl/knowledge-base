from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fields = (
        'id', 'name', 'surname', 'department', 
        'email', 'private_access', 'is_active', 'is_staff', 'is_superuser', 
    )
    list_editable = (
        'private_access',
    )
    list_display = (
        'id', 'name', 'surname', 'department', 'email', 'private_access', 
    )
    search_fields = (
        'id', 'name', 'surname', 'department', 
        'email', 'is_active', 'is_staff', 'is_superuser', 'private_access'
    )
    readonly_fields = (
        'id',
    )

admin.site.register(User, UserAdmin)