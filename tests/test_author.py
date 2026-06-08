import datetime
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from tests.factories.author_data import AuthorFactory
from apps.author.domain.models import Author
from apps.author.interfaces.serializers import (
    AuthorReadSerializer,
    AuthorCreateSerializer,
    AuthorUpdateSerializer
)
from core.utils.fake import generate_random_value


@pytest.fixture
def api_client():
    return APIClient()
    
@pytest.fixture
def author_data(db):
    instance = AuthorFactory.build(
        author=AuthorFactory(),
    )
    return {
        {# Campos simples da entidade #}
        "name": instance.name,

        {# Relacionamentos obrigatórios OneToOne / ManyToOne #}
        "mentor": str(instance.mentor.id),

        {# Relacionamentos ManyToMany #}
    }

@pytest.mark.django_db
def test_create_author(api_client, author_data):
    url = reverse('author-list')

    response = api_client.post(url, author_data)

    assert response.status_code == status.HTTP_201_CREATED

    instance = Author.objects.get(id=response.data["id"])

    expected_response = AuthorReadSerializer(instance).data
    assert response.data == expected_response    

@pytest.mark.django_db
def test_read_author(api_client, author_data):
    instance = AuthorFactory()
    url = reverse('author-detail', args=[instance.id])
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK

    expected_data = AuthorReadSerializer(instance).data
    assert response.data == expected_data
    

@pytest.mark.django_db
def test_update_author(api_client, author_data):
    instance = AuthorFactory()
    url = reverse('author-detail', args=[instance.id])

    updated_data = author_data.copy()


    response = api_client.put(url, updated_data)
    assert response.status_code == status.HTTP_200_OK

    instance.refresh_from_db()
    expected_response = AuthorReadSerializer(instance).data
    assert response.data == expected_response

@pytest.mark.django_db
def test_delete_author(api_client, author_data):
    instance = AuthorFactory()
    url = reverse('author-detail', args=[instance.id])
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Author.objects.filter(id=instance.id).exists()
