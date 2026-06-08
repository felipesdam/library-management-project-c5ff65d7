from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from apps.book.domain.models import Book
from apps.book.application.entity_use_case import BookUseCase
from apps.book.infrastructure.orm_repository import BookORMRepository
from apps.book.interfaces.serializers import (
    BookReadSerializer,
    BookCreateSerializer,
    BookUpdateSerializer
)

class BookListView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_case = BookUseCase(BookORMRepository())

    @swagger_auto_schema(
        operation_description="List the entities",
        responses={200: BookReadSerializer(many=True)}
    )
    def get(self, request):
        entities = self.use_case.list()
        serializer = BookReadSerializer(entities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new entity",
        request_body=BookCreateSerializer,
        responses={201: BookReadSerializer}
    )
    def post(self, request):
        serializer = BookCreateSerializer(data=request.data)
        if serializer.is_valid():
            entity = self.use_case.create(serializer.validated_data)
            return Response(BookReadSerializer(entity).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_case = BookUseCase(BookORMRepository())

    @swagger_auto_schema(
        operation_description="Get entity by primary key",
        responses={200: BookReadSerializer}
    )
    def get(self, request, pk):
        try:
            entity = self.use_case.retrieve(pk)
            serializer = BookReadSerializer(entity)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_description="Update an entity",
        request_body=BookUpdateSerializer,
        responses={200: BookReadSerializer}
    )
    def put(self, request, pk):
        serializer = BookUpdateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                updated_entity = self.use_case.update(pk, serializer.validated_data)
                return Response(
                    BookReadSerializer(updated_entity).data,
                    status=status.HTTP_200_OK
                )
            except Book.DoesNotExist:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update an existing object",
        request_body=BookUpdateSerializer,
        responses={200: BookReadSerializer}
    )
    def patch(self, request, pk):
        try:
            entity = self.use_case.retrieve(pk)
            serializer = BookUpdateSerializer(entity, data=request.data, partial=True)
            if serializer.is_valid():
                updated_entity = serializer.save()
                return Response(
                    BookReadSerializer(updated_entity).data,
                    status=status.HTTP_200_OK
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_description="Delete a resource",
        responses={204: "No Content"}
    )
    def delete(self, request, pk):
        try:
            self.use_case.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
