from typing import Optional
from django.contrib import admin
from django.http.request import HttpRequest
from .models import Customer, Music

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'dob', 'gender', 'id']
    list_filter = ['gender']
    search_fields = ('name__startswith', 'gender')


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    pass

    def has_delete_permission(self, request, obj = None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
