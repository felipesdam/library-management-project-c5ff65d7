from django.urls import path
from apps.genre.interfaces.views import GenreListView, GenreDetailView

urlpatterns = [
    path("", GenreListView.as_view(), name="genre-list"),
    path("<str:pk>/", GenreDetailView.as_view(), name="genre-detail"),
]
