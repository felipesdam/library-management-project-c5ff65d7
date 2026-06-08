from rest_framework import serializers
from apps.author.domain.models import Author

class AuthorReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class AuthorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            "name",
            "mentor",
        ]

class AuthorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            "name",
            "mentor",
        ]
