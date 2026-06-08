import datetime
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from tests.factories.book_data import BookFactory
from apps.book.domain.models import Book
from apps.book.interfaces.serializers import (
    BookReadSerializer,
    BookCreateSerializer,
    BookUpdateSerializer
)
from core.utils.fake import generate_random_value


@pytest.fixture
def api_client():
    return APIClient()
    
@pytest.fixture
def book_data(db):
    instance = BookFactory.build(
        author=AuthorFactory(),
    )
    return {
        {# Campos simples da entidade #}
        "title": instance.title,
        "published": instance.published,

        {# Relacionamentos obrigatórios OneToOne / ManyToOne #}
        "author": str(instance.author.id),

        {# Relacionamentos ManyToMany #}
        "genres": [str(item.id) for item in instance.genres.all()],
    }

@pytest.mark.django_db
def test_create_book(api_client, book_data):
    url = reverse('book-list')

    response = api_client.post(url, book_data)

    assert response.status_code == status.HTTP_201_CREATED

    instance = Book.objects.get(id=response.data["id"])

    expected_response = BookReadSerializer(instance).data
    assert response.data == expected_response    

@pytest.mark.django_db
def test_read_book(api_client, book_data):
    instance = BookFactory()
    url = reverse('book-detail', args=[instance.id])
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK

    expected_data = BookReadSerializer(instance).data
    assert response.data == expected_data
    

@pytest.mark.django_db
def test_update_book(api_client, book_data):
    instance = BookFactory()
    url = reverse('book-detail', args=[instance.id])

    updated_data = book_data.copy()


    response = api_client.put(url, updated_data)
    assert response.status_code == status.HTTP_200_OK

    instance.refresh_from_db()
    expected_response = BookReadSerializer(instance).data
    assert response.data == expected_response

@pytest.mark.django_db
def test_delete_book(api_client, book_data):
    instance = BookFactory()
    url = reverse('book-detail', args=[instance.id])
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Book.objects.filter(id=instance.id).exists()
