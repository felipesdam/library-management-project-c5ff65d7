from rest_framework import serializers
from apps.book.domain.models import Book

class BookReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "title",
            "published",
            "author",
            "genres",
        ]

class BookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "title",
            "published",
            "author",
            "genres",
        ]
