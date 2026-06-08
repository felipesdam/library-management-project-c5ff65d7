import datetime
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from tests.factories.genre_data import GenreFactory
from apps.genre.domain.models import Genre
from apps.genre.interfaces.serializers import (
    GenreReadSerializer,
    GenreCreateSerializer,
    GenreUpdateSerializer
)
from core.utils.fake import generate_random_value


@pytest.fixture
def api_client():
    return APIClient()
    
@pytest.fixture
def genre_data(db):
    instance = GenreFactory.build(
    )
    return {
        {# Campos simples da entidade #}
        "name": instance.name,

        {# Relacionamentos obrigatórios OneToOne / ManyToOne #}

        {# Relacionamentos ManyToMany #}
    }

@pytest.mark.django_db
def test_create_genre(api_client, genre_data):
    url = reverse('genre-list')

    response = api_client.post(url, genre_data)

    assert response.status_code == status.HTTP_201_CREATED

    instance = Genre.objects.get(id=response.data["id"])

    expected_response = GenreReadSerializer(instance).data
    assert response.data == expected_response    

@pytest.mark.django_db
def test_read_genre(api_client, genre_data):
    instance = GenreFactory()
    url = reverse('genre-detail', args=[instance.id])
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK

    expected_data = GenreReadSerializer(instance).data
    assert response.data == expected_data
    

@pytest.mark.django_db
def test_update_genre(api_client, genre_data):
    instance = GenreFactory()
    url = reverse('genre-detail', args=[instance.id])

    updated_data = genre_data.copy()


    response = api_client.put(url, updated_data)
    assert response.status_code == status.HTTP_200_OK

    instance.refresh_from_db()
    expected_response = GenreReadSerializer(instance).data
    assert response.data == expected_response

@pytest.mark.django_db
def test_delete_genre(api_client, genre_data):
    instance = GenreFactory()
    url = reverse('genre-detail', args=[instance.id])
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Genre.objects.filter(id=instance.id).exists()
