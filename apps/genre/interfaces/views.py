from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from apps.genre.domain.models import Genre
from apps.genre.application.entity_use_case import GenreUseCase
from apps.genre.infrastructure.orm_repository import GenreORMRepository
from apps.genre.interfaces.serializers import (
    GenreReadSerializer,
    GenreCreateSerializer,
    GenreUpdateSerializer
)

class GenreListView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_case = GenreUseCase(GenreORMRepository())

    @swagger_auto_schema(
        operation_description="List the entities",
        responses={200: GenreReadSerializer(many=True)}
    )
    def get(self, request):
        entities = self.use_case.list()
        serializer = GenreReadSerializer(entities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new entity",
        request_body=GenreCreateSerializer,
        responses={201: GenreReadSerializer}
    )
    def post(self, request):
        serializer = GenreCreateSerializer(data=request.data)
        if serializer.is_valid():
            entity = self.use_case.create(serializer.validated_data)
            return Response(GenreReadSerializer(entity).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetailView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_case = GenreUseCase(GenreORMRepository())

    @swagger_auto_schema(
        operation_description="Get entity by primary key",
        responses={200: GenreReadSerializer}
    )
    def get(self, request, pk):
        try:
            entity = self.use_case.retrieve(pk)
            serializer = GenreReadSerializer(entity)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Genre.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_description="Update an entity",
        request_body=GenreUpdateSerializer,
        responses={200: GenreReadSerializer}
    )
    def put(self, request, pk):
        serializer = GenreUpdateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                updated_entity = self.use_case.update(pk, serializer.validated_data)
                return Response(
                    GenreReadSerializer(updated_entity).data,
                    status=status.HTTP_200_OK
                )
            except Genre.DoesNotExist:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update an existing object",
        request_body=GenreUpdateSerializer,
        responses={200: GenreReadSerializer}
    )
    def patch(self, request, pk):
        try:
            entity = self.use_case.retrieve(pk)
            serializer = GenreUpdateSerializer(entity, data=request.data, partial=True)
            if serializer.is_valid():
                updated_entity = serializer.save()
                return Response(
                    GenreReadSerializer(updated_entity).data,
                    status=status.HTTP_200_OK
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Genre.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_description="Delete a resource",
        responses={204: "No Content"}
    )
    def delete(self, request, pk):
        try:
            self.use_case.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Genre.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
