from django.contrib import admin
from .domain.models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Book._meta.fields]
