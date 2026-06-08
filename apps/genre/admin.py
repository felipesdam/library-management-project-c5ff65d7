from django.contrib import admin
from .domain.models import Genre

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Genre._meta.fields]
