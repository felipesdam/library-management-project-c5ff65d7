from django.contrib import admin
from .domain.models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Author._meta.fields]
