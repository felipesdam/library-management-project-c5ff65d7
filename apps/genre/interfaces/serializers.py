from rest_framework import serializers
from apps.genre.domain.models import Genre

class GenreReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class GenreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = [
            "name",
        ]

class GenreUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = [
            "name",
        ]
