from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from apps.author.domain.models import Author
from apps.author.application.entity_use_case import AuthorUseCase
from apps.author.infrastructure.orm_repository import AuthorORMRepository
from apps.author.interfaces.serializers import (
    AuthorReadSerializer,
    AuthorCreateSerializer,
    AuthorUpdateSerializer
)

class AuthorListView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_case = AuthorUseCase(AuthorORMRepository())

    @swagger_auto_schema(
        operation_description="List the entities",
        responses={200: AuthorReadSerializer(many=True)}
    )
    def get(self, request):
        entities = self.use_case.list()
        serializer = AuthorReadSerializer(entities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new entity",
        request_body=AuthorCreateSerializer,
        responses={201: AuthorReadSerializer}
    )
    def post(self, request):
        serializer = AuthorCreateSerializer(data=request.data)
        if serializer.is_valid():
            entity = self.use_case.create(serializer.validated_data)
            return Response(AuthorReadSerializer(entity).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetailView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_case = AuthorUseCase(AuthorORMRepository())

    @swagger_auto_schema(
        operation_description="Get entity by primary key",
        responses={200: AuthorReadSerializer}
    )
    def get(self, request, pk):
        try:
            entity = self.use_case.retrieve(pk)
            serializer = AuthorReadSerializer(entity)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Author.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_description="Update an entity",
        request_body=AuthorUpdateSerializer,
        responses={200: AuthorReadSerializer}
    )
    def put(self, request, pk):
        serializer = AuthorUpdateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                updated_entity = self.use_case.update(pk, serializer.validated_data)
                return Response(
                    AuthorReadSerializer(updated_entity).data,
                    status=status.HTTP_200_OK
                )
            except Author.DoesNotExist:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update an existing object",
        request_body=AuthorUpdateSerializer,
        responses={200: AuthorReadSerializer}
    )
    def patch(self, request, pk):
        try:
            entity = self.use_case.retrieve(pk)
            serializer = AuthorUpdateSerializer(entity, data=request.data, partial=True)
            if serializer.is_valid():
                updated_entity = serializer.save()
                return Response(
                    AuthorReadSerializer(updated_entity).data,
                    status=status.HTTP_200_OK
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Author.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_description="Delete a resource",
        responses={204: "No Content"}
    )
    def delete(self, request, pk):
        try:
            self.use_case.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Author.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
