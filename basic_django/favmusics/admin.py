from django.contrib import admin
from .models import Customer, Music

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'dob', 'gender']


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    pass
